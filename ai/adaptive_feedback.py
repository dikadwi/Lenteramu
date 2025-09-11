# Adaptive Feedback and Assessment System
from datetime import datetime
from models import db, User, StudentProfile, LearningActivity, StudentProgress, Course, UserFeedback
import json


class AdaptiveFeedbackSystem:
    """Implementasi Diagram Alur Umpan Balik dan Penilaian"""

    def __init__(self):
        self.feedback_templates = {
            'excellent': {
                'message': 'Luar biasa! Anda menunjukkan pemahaman yang sangat baik.',
                'recommendations': ['Lanjutkan ke materi tingkat lanjut', 'Bantu teman yang kesulitan']
            },
            'good': {
                'message': 'Bagus! Anda sudah memahami konsep dengan baik.',
                'recommendations': ['Perkuat dengan latihan tambahan', 'Review materi sekali lagi']
            },
            'average': {
                'message': 'Cukup baik, namun masih ada ruang untuk perbaikan.',
                'recommendations': ['Ulangi materi yang sulit', 'Minta bantuan guru']
            },
            'needs_improvement': {
                'message': 'Perlu lebih banyak latihan untuk menguasai materi.',
                'recommendations': ['Kembali ke materi dasar', 'Ikuti tutorial tambahan']
            }
        }

    def collect_assessment_data(self, user_id, course_id, assessment_result):
        """1. Pengumpulan Data Hasil Evaluasi (Assessment Data Collection)"""
        try:
            # Simpan hasil evaluasi
            activity = LearningActivity(
                user_id=user_id,
                course_id=course_id,
                activity_type='quiz_attempt',
                start_time=datetime.utcnow(),
                end_time=datetime.utcnow(),
                score=assessment_result.get('score', 0),
                completed=assessment_result.get('completed', False)
            )

            db.session.add(activity)

            # Update progress
            student = StudentProfile.query.filter_by(user_id=user_id).first()
            if student:
                progress = StudentProgress.query.filter_by(
                    student_id=student.id,
                    course_id=course_id
                ).first()

                if not progress:
                    progress = StudentProgress(
                        student_id=student.id,
                        course_id=course_id,
                        progress_percentage=0
                    )
                    db.session.add(progress)

                # Update progress percentage
                new_progress = min(100, progress.progress_percentage + 10)
                progress.progress_percentage = new_progress
                progress.last_accessed = datetime.utcnow()

                if assessment_result.get('score', 0) >= 80:
                    progress.grade = 'A'
                elif assessment_result.get('score', 0) >= 70:
                    progress.grade = 'B'
                elif assessment_result.get('score', 0) >= 60:
                    progress.grade = 'C'
                else:
                    progress.grade = 'D'

            db.session.commit()

            return {
                'status': 'success',
                'activity_id': activity.id,
                'progress_updated': True
            }

        except Exception as e:
            db.session.rollback()
            return {'status': 'error', 'message': str(e)}

    def analyze_student_performance(self, user_id):
        """2. Analisis Performa Siswa (Student Performance Analysis)"""
        try:
            student = StudentProfile.query.filter_by(user_id=user_id).first()
            if not student:
                return None

            # Ambil aktivitas pembelajaran
            activities = LearningActivity.query.filter_by(
                user_id=user_id).all()
            progress_records = StudentProgress.query.filter_by(
                student_id=student.id).all()

            # Analisis statistik
            scores = [a.score for a in activities if a.score is not None]
            avg_score = sum(scores) / len(scores) if scores else 0

            # Analisis pola belajar
            completed_courses = len(
                [p for p in progress_records if p.progress_percentage == 100])
            total_courses = len(progress_records)
            completion_rate = completed_courses / total_courses if total_courses > 0 else 0

            # Identifikasi kekuatan dan kelemahan
            subject_performance = {}
            for progress in progress_records:
                course = Course.query.get(progress.course_id)
                if course and course.subject:
                    subject_name = course.subject.name
                    if subject_name not in subject_performance:
                        subject_performance[subject_name] = []
                    subject_performance[subject_name].append(
                        progress.progress_percentage)

            # Hitung rata-rata per mata pelajaran
            subject_averages = {}
            for subject, scores in subject_performance.items():
                subject_averages[subject] = sum(scores) / len(scores)

            # Kategorisasi performa
            if avg_score >= 90:
                performance_category = 'excellent'
            elif avg_score >= 80:
                performance_category = 'good'
            elif avg_score >= 70:
                performance_category = 'average'
            else:
                performance_category = 'needs_improvement'

            return {
                'user_id': user_id,
                'avg_score': avg_score,
                'completion_rate': completion_rate,
                'completed_courses': completed_courses,
                'total_courses': total_courses,
                'subject_performance': subject_averages,
                'performance_category': performance_category,
                'strengths': [subject for subject, score in subject_averages.items() if score >= 80],
                'weaknesses': [subject for subject, score in subject_averages.items() if score < 70]
            }

        except Exception as e:
            print(f"Error in performance analysis: {e}")
            return None

    def generate_adaptive_feedback(self, performance_analysis):
        """3. Pemberian Umpan Balik Adaptif (Adaptive Feedback Generation)"""
        if not performance_analysis:
            return None

        category = performance_analysis['performance_category']
        template = self.feedback_templates.get(
            category, self.feedback_templates['average'])

        # Personalisasi feedback
        feedback = {
            'message': template['message'],
            'score_feedback': f"Skor rata-rata Anda: {performance_analysis['avg_score']:.1f}",
            'progress_feedback': f"Tingkat penyelesaian: {performance_analysis['completion_rate']*100:.1f}%",
            'recommendations': template['recommendations'],
            'strengths': performance_analysis.get('strengths', []),
            'areas_for_improvement': performance_analysis.get('weaknesses', []),
            'next_steps': self._generate_next_steps(performance_analysis),
            'created_at': datetime.utcnow().isoformat()
        }

        return feedback

    def integrate_with_ui(self, user_id, feedback):
        """4. Integrasi dengan Antarmuka Pengguna (Integration with User Interface)"""
        try:
            # Simpan feedback ke database untuk ditampilkan di UI
            feedback_record = UserFeedback(
                user_id=user_id,
                feedback_type='system',
                rating=None,
                comments=json.dumps(feedback)
            )

            db.session.add(feedback_record)
            db.session.commit()

            return {
                'status': 'success',
                'feedback_id': feedback_record.id,
                'ui_data': {
                    'show_popup': True,
                    'feedback': feedback,
                    'display_duration': 10  # seconds
                }
            }

        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def recommend_additional_content(self, performance_analysis):
        """5. Rekomendasi Konten Pembelajaran Tambahan"""
        if not performance_analysis:
            return []

        recommendations = []

        # Rekomendasi berdasarkan kelemahan
        for weak_subject in performance_analysis.get('weaknesses', []):
            recommendations.append({
                'type': 'remedial',
                'subject': weak_subject,
                'title': f'Penguatan Materi {weak_subject}',
                'description': f'Materi tambahan untuk memperkuat pemahaman {weak_subject}',
                'priority': 'high',
                'estimated_time': '30 menit'
            })

        # Rekomendasi berdasarkan kekuatan
        for strong_subject in performance_analysis.get('strengths', []):
            recommendations.append({
                'type': 'advanced',
                'subject': strong_subject,
                'title': f'Materi Lanjutan {strong_subject}',
                'description': f'Tingkatkan kemampuan {strong_subject} dengan materi lanjutan',
                'priority': 'medium',
                'estimated_time': '45 menit'
            })

        # Rekomendasi umum berdasarkan completion rate
        if performance_analysis['completion_rate'] < 0.7:
            recommendations.append({
                'type': 'study_strategy',
                'title': 'Strategi Manajemen Waktu Belajar',
                'description': 'Tips untuk meningkatkan konsistensi belajar',
                'priority': 'high',
                'estimated_time': '20 menit'
            })

        return recommendations

    def monitor_and_adjust(self, user_id):
        """6. Pemantauan Hasil dan Penyesuaian Pembelajaran"""
        try:
            # Monitor interaksi dengan rekomendasi
            recent_activities = LearningActivity.query.filter(
                LearningActivity.user_id == user_id,
                LearningActivity.created_at >= datetime.utcnow().replace(day=1)
            ).all()

            # Hitung improvement
            monthly_scores = [a.score for a in recent_activities if a.score]

            if len(monthly_scores) >= 2:
                improvement = monthly_scores[-1] - monthly_scores[0]
                trend = 'improving' if improvement > 0 else 'declining' if improvement < 0 else 'stable'
            else:
                trend = 'insufficient_data'

            # Adjust recommendations berdasarkan trend
            adjustment_needed = trend == 'declining'

            return {
                'user_id': user_id,
                'trend': trend,
                'improvement': improvement if len(monthly_scores) >= 2 else 0,
                'adjustment_needed': adjustment_needed,
                'recent_activity_count': len(recent_activities),
                'average_recent_score': sum(monthly_scores) / len(monthly_scores) if monthly_scores else 0
            }

        except Exception as e:
            print(f"Error in monitoring: {e}")
            return None

    def _generate_next_steps(self, performance_analysis):
        """Helper untuk generate langkah selanjutnya"""
        next_steps = []

        if performance_analysis['completion_rate'] < 0.5:
            next_steps.append('Fokus menyelesaikan kursus yang sudah dimulai')

        if performance_analysis['avg_score'] < 70:
            next_steps.append('Review ulang materi dasar')

        if performance_analysis.get('weaknesses'):
            next_steps.append(
                f"Perkuat pemahaman di: {', '.join(performance_analysis['weaknesses'])}")

        if not next_steps:
            next_steps.append('Lanjutkan pembelajaran dengan konsisten')

        return next_steps

# Factory function


def create_adaptive_feedback_system():
    return AdaptiveFeedbackSystem()
