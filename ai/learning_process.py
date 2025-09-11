# AI Learning Process Implementation
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
import joblib
import json
from datetime import datetime
from models import db, User, StudentProfile, LearningActivity, StudentProgress, AIRecommendation


class AILearningProcess:
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
        """Generate personalized recommendations"""
        try:
            student = StudentProfile.query.get(student_id)
            if not student:
                return []

            # Dapatkan data siswa untuk prediksi
            activities = LearningActivity.query.filter_by(
                user_id=student.user_id).all()
            progress = StudentProgress.query.filter_by(
                student_id=student.id).all()

            # Hitung fitur
            avg_score = np.mean(
                [a.score for a in activities if a.score]) if activities else 0
            completion_rate = len(
                [p for p in progress if p.progress_percentage == 100]) / max(len(progress), 1)

            # Generate recommendations berdasarkan performa
            recommendations = []

            if avg_score < 70:
                recommendations.append({
                    'type': 'remedial',
                    'title': 'Materi Dasar Penguatan',
                    'reason': 'Skor rata-rata perlu ditingkatkan'
                })

            if completion_rate < 0.7:
                recommendations.append({
                    'type': 'motivation',
                    'title': 'Strategi Penyelesaian Tugas',
                    'reason': 'Tingkat penyelesaian perlu diperbaiki'
                })

            # Rekomendasi berdasarkan learning style
            style_recommendations = {
                'visual': 'Video Tutorial dan Infografis',
                'auditory': 'Podcast dan Audio Lessons',
                'kinesthetic': 'Praktik dan Simulasi',
                'reading': 'E-book dan Artikel'
            }

            if student.learning_style in style_recommendations:
                recommendations.append({
                    'type': 'content',
                    'title': style_recommendations[student.learning_style],
                    'reason': f'Sesuai dengan gaya belajar {student.learning_style}'
                })

            return recommendations

        except Exception as e:
            print(f"Error generating recommendations: {e}")
            return []

# Factory function untuk AI Learning Process


def create_ai_learning_process():
    return AILearningProcess()
