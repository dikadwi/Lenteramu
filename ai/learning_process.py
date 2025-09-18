from models import db, User, StudentProfile, LearningActivity, StudentProgress, AIRecommendation
from datetime import datetime
import json
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd
import numpy as np


class QLearningRecommender:
    """Q-learning RL sederhana untuk rekomendasi materi/tugas siswa"""

    def __init__(self, actions, student_id, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.actions = actions  # list of possible actions (materi/tugas id)
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate
        self.student_id = student_id
        self.q_table = self._load_q_table()

    def _q_key(self, state, action):
        # Serialize state-action to string for DB
        return json.dumps({'state': state, 'action': action})

    def _load_q_table(self):
        q_table = {}
        # Load from AIRecommendation DB
        from models import AIRecommendation
        for rec in AIRecommendation.query.filter_by(user_id=self.student_id, recommendation_type='sequence').all():
            try:
                key = rec.reasoning  # serialized state-action
                q_table[(tuple(json.loads(key)['state']),
                         json.loads(key)['action'])] = rec.match_score
            except Exception:
                continue
        return q_table

    def _save_q_value(self, state, action, value):
        from models import AIRecommendation, db
        key = self._q_key(state, action)
        rec = AIRecommendation.query.filter_by(user_id=self.student_id, course_id=int(
            action), recommendation_type='sequence', reasoning=key).first()
        if not rec:
            rec = AIRecommendation(user_id=self.student_id, course_id=int(
                action), recommendation_type='sequence', match_score=value, reasoning=key, is_active=True)
            db.session.add(rec)
        else:
            rec.match_score = value
        db.session.commit()

    def get_state(self, student):
        # State: (VARK, MSLQ, AMS, Engagement)
        vark = student.learning_style or 'visual'
        mslq = getattr(student, 'mslq_level', 'medium') or 'medium'
        ams = getattr(student, 'ams_type', 'intrinsic') or 'intrinsic'
        eng = getattr(student, 'engagement_level', 'medium') or 'medium'
        return (vark, mslq, ams, eng)

    def choose_action(self, state):
        # Epsilon-greedy
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)
        q_values = [self.q_table.get((state, a), 0) for a in self.actions]
        max_q = max(q_values)
        best_actions = [a for a, q in zip(
            self.actions, q_values) if q == max_q]
        return np.random.choice(best_actions)

    def update(self, state, action, reward, next_state):
        old_q = self.q_table.get((state, action), 0)
        next_qs = [self.q_table.get((next_state, a), 0) for a in self.actions]
        max_next_q = max(next_qs) if next_qs else 0
        new_q = old_q + self.alpha * (reward + self.gamma * max_next_q - old_q)
        self.q_table[(state, action)] = new_q
        self._save_q_value(state, action, new_q)

    def get_best_actions(self, state, topk=3):
        q_values = [(a, self.q_table.get((state, a), 0)) for a in self.actions]
        q_values.sort(key=lambda x: x[1], reverse=True)
        return [a for a, _ in q_values[:topk]]


# AI Learning Process Implementation


class AILearningProcess:

    def batch_train_qlearning(self, episodes=300, alpha=0.1, gamma=0.9):
        """Batch training Q-learning untuk seluruh siswa dan Course (materi/tugas)"""
        from models import Course
        students = StudentProfile.query.all()
        actions = [str(c.id) for c in Course.query.filter(
            Course.content_type.in_(['article', 'practice', 'quiz'])).all()]
        for ep in range(episodes):
            for student in students:
                ql = QLearningRecommender(
                    actions, student_id=student.user_id, alpha=alpha, gamma=gamma)
                progresses = StudentProgress.query.filter_by(
                    student_id=student.id).order_by(StudentProgress.created_at).all()
                for i, prog in enumerate(progresses):
                    state = ql.get_state(student)
                    action = str(prog.course_id)
                    reward = 1 if prog.progress_percentage == 100 else 0
                    next_state = state
                    ql.update(state, action, reward, next_state)
        return True

    def get_qlearning_recommender(self, student):
        from models import Course
        course_ids = [str(c.id) for c in Course.query.filter(
            Course.content_type.in_(['article', 'practice', 'quiz'])).all()]
        return QLearningRecommender(course_ids, student_id=student.user_id)

    """Implementasi Alur Proses Pembelajaran AI sesuai dokumen"""

    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.performance_metrics = {}

    def data_collection(self):
        """1. Pengumpulan Data (Data Collection)"""
        try:
            # Kumpulkan data dari database
            students = StudentProfile.query.all()
            activities = LearningActivity.query.all()
            progress = StudentProgress.query.all()

            data = []
            for student in students:
                student_activities = [
                    a for a in activities if a.user_id == student.user_id]
                student_progress = [
                    p for p in progress if p.student_id == student.id]

                # Fitur pembelajaran
                avg_score = np.mean(
                    [a.score for a in student_activities if a.score]) if student_activities else 0
                total_time = sum([
                    (a.end_time - a.start_time).total_seconds() / 3600
                    for a in student_activities
                    if a.end_time and a.start_time
                ]) if student_activities else 0
                completion_rate = len(
                    [p for p in student_progress if p.progress_percentage == 100]) / max(len(student_progress), 1)

                # Encode learning style
                style_mapping = {'visual': 1, 'auditory': 2,
                                 'kinesthetic': 3, 'reading': 4}
                pace_mapping = {'slow': 1, 'normal': 2, 'fast': 3}

                data.append({
                    'student_id': student.id,
                    'learning_style': style_mapping.get(student.learning_style, 1),
                    'learning_pace': pace_mapping.get(student.learning_pace, 2),
                    'avg_score': avg_score,
                    'total_time': total_time,
                    'completion_rate': completion_rate,
                    'performance_category': self._categorize_performance(avg_score, completion_rate)
                })

            return pd.DataFrame(data)

        except Exception as e:
            print(f"Error in data collection: {e}")
            return pd.DataFrame()

    def data_preprocessing(self, data):
        """2. Praproses Data (Data Preprocessing)"""
        if data.empty:
            return None, None

        # Bersihkan data
        data = data.fillna(0)
        data = data.drop_duplicates()

        # Pisahkan features dan target
        features = ['learning_style', 'learning_pace',
                    'avg_score', 'total_time', 'completion_rate']
        X = data[features]
        y = data['performance_category']

        # Normalisasi fitur
        X_scaled = self.scaler.fit_transform(X)

        return X_scaled, y

    def model_training(self, X, y):
        """3. Pelatihan Model (Model Training)"""
        if X is None or y is None:
            return False

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)

        # Train model dengan hyperparameter optimization
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            random_state=42
        )

        self.model.fit(X_train, y_train)

        # Cross-validation
        cv_scores = cross_val_score(self.model, X_train, y_train, cv=5)

        self.performance_metrics['cv_mean'] = cv_scores.mean()
        self.performance_metrics['cv_std'] = cv_scores.std()

        return True

    def model_validation(self, X, y):
        """4. Validasi dan Evaluasi Model (Model Validation and Evaluation)"""
        if self.model is None:
            return False

        # Split untuk validasi
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)

        # Prediksi
        y_pred = self.model.predict(X_test)

        # Hitung metrik evaluasi
        self.performance_metrics.update({
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted', zero_division=0),
            'recall': recall_score(y_test, y_pred, average='weighted', zero_division=0),
            'f1_score': f1_score(y_test, y_pred, average='weighted', zero_division=0)
        })

        return True

    def model_deployment(self):
        """5. Implementasi dan Integrasi Model (Model Deployment and Integration)"""
        if self.model is None:
            return False

        try:
            # Simpan model
            model_path = 'ai/trained_model.pkl'
            scaler_path = 'ai/scaler.pkl'

            joblib.dump(self.model, model_path)
            joblib.dump(self.scaler, scaler_path)

            # Simpan metrics ke database
            metrics_data = SystemMetrics(
                metric_name='model_performance',
                metric_value=self.performance_metrics.get('accuracy', 0) * 100,
                metric_unit='percentage'
            )
            db.session.add(metrics_data)
            db.session.commit()

            return True

        except Exception as e:
            print(f"Error in model deployment: {e}")
            return False

    def model_monitoring(self):
        """6. Monitoring dan Pembaruan Model (Model Monitoring and Retraining)"""
        try:
            # Monitor concept drift
            current_data = self.data_collection()
            if not current_data.empty:
                X, y = self.data_preprocessing(current_data)
                if X is not None and self.model is not None:
                    # Cek performa pada data baru
                    accuracy = self.model.score(X, y)

                    # Jika performa turun di bawah threshold, trigger retraining
                    if accuracy < 0.8:
                        print("Concept drift detected. Retraining required.")
                        return {'status': 'retrain_needed', 'accuracy': accuracy}
                    else:
                        return {'status': 'model_healthy', 'accuracy': accuracy}

            return {'status': 'insufficient_data'}

        except Exception as e:
            print(f"Error in model monitoring: {e}")
            return {'status': 'error', 'message': str(e)}

    def _categorize_performance(self, avg_score, completion_rate):
        """Helper method untuk kategorisasi performa siswa"""
        if avg_score >= 80 and completion_rate >= 0.8:
            return 'high_performer'
        elif avg_score >= 60 and completion_rate >= 0.6:
            return 'average_performer'
        else:
            return 'needs_support'

    def generate_recommendations(self, student_id):
        """Generate personalized recommendations (Q-learning + CBF)"""
        try:
            from models import Course
            student = StudentProfile.query.get(student_id)
            if not student:
                return []

            # Hitung fitur state
            activities = LearningActivity.query.filter_by(
                user_id=student.user_id).all()
            progress = StudentProgress.query.filter_by(
                student_id=student.id).all()
            avg_score = np.mean(
                [a.score for a in activities if a.score]) if activities else 0
            completion_rate = len(
                [p for p in progress if p.progress_percentage == 100]) / max(len(progress), 1)
            student.avg_score = avg_score
            student.completion_rate = completion_rate

            # Q-learning RL: pilih materi/tugas prioritas (pakai Course, bukan LearningActivity)
            ql = self.get_qlearning_recommender(student)
            state = ql.get_state(student)
            best_ids = ql.get_best_actions(state, topk=3)

            # Ambil Course sesuai best_ids
            course_objs = Course.query.filter(Course.id.in_(
                [int(i) for i in best_ids if str(i).isdigit()])).all() if best_ids else []
            cbf_results = []
            for c in course_objs:
                # Contoh: filter berdasarkan minat siswa (jika ada field interest)
                if hasattr(student, 'interest') and student.interest:
                    if student.interest.lower() in (c.title or '').lower():
                        cbf_results.append(c)
                else:
                    cbf_results.append(c)

            # Fallback: jika Q-table kosong, tampilkan 3 course demo teratas
            if not cbf_results:
                cbf_results = Course.query.order_by(
                    Course.id.asc()).limit(3).all()

            # Format rekomendasi
            recommendations = []
            for c in cbf_results:
                recommendations.append({
                    'type': c.content_type,
                    'judul': c.title,
                    'deskripsi': c.description or '',
                    'tipe': c.content_type,
                    'link': f"/siswa/features/materi" if c.content_type == 'article' else (f"/siswa/features/tugas" if c.content_type == 'practice' else f"/siswa/features/kuis")
                })

            # Jika kosong, fallback ke rule-based
            if not recommendations:
                if avg_score < 70:
                    recommendations.append({
                        'type': 'remedial',
                        'judul': 'Materi Dasar Penguatan',
                        'deskripsi': 'Skor rata-rata perlu ditingkatkan',
                        'tipe': 'remedial',
                        'link': '#'
                    })
                if completion_rate < 0.7:
                    recommendations.append({
                        'type': 'motivation',
                        'judul': 'Strategi Penyelesaian Tugas',
                        'deskripsi': 'Tingkat penyelesaian perlu diperbaiki',
                        'tipe': 'motivation',
                        'link': '#'
                    })

            return recommendations
        except Exception as e:
            print(f"Error generating recommendations: {e}")
            return []

# Factory function untuk AI Learning Process


def create_ai_learning_process():
    return AILearningProcess()
