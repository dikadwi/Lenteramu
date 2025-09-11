# Database models untuk LENTERAMU
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Enum('siswa', 'guru', 'admin'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    # Relationships
    student_profile = db.relationship(
        'StudentProfile', backref='user', uselist=False)
    teacher_profile = db.relationship(
        'TeacherProfile', backref='user', uselist=False)
    learning_activities = db.relationship('LearningActivity', backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'role': self.role,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_active': self.is_active
        }


class StudentProfile(db.Model):
    __tablename__ = 'student_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    grade_level = db.Column(db.String(10), nullable=False)
    school_name = db.Column(db.String(100), nullable=False)
    learning_style = db.Column(
        db.Enum('visual', 'auditory', 'kinesthetic', 'reading'), default='visual')
    learning_pace = db.Column(
        db.Enum('slow', 'normal', 'fast'), default='normal')
    preferred_subjects = db.Column(db.Text)  # JSON string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    progress_records = db.relationship('StudentProgress', backref='student')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'student_id': self.student_id,
            'grade_level': self.grade_level,
            'school_name': self.school_name,
            'learning_style': self.learning_style,
            'learning_pace': self.learning_pace,
            'preferred_subjects': self.preferred_subjects
        }


class TeacherProfile(db.Model):
    __tablename__ = 'teacher_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    teacher_id = db.Column(db.String(20), unique=True, nullable=False)
    school_name = db.Column(db.String(100), nullable=False)
    subjects = db.Column(db.Text)  # JSON string
    experience_years = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'teacher_id': self.teacher_id,
            'school_name': self.school_name,
            'subjects': self.subjects,
            'experience_years': self.experience_years
        }


class Subject(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    description = db.Column(db.Text)
    grade_level = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    courses = db.relationship('Course', backref='subject')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'description': self.description,
            'grade_level': self.grade_level
        }


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    subject_id = db.Column(db.Integer, db.ForeignKey(
        'subjects.id'), nullable=False)
    difficulty_level = db.Column(
        db.Enum('beginner', 'intermediate', 'advanced'), default='beginner')
    content_type = db.Column(
        db.Enum('video', 'article', 'quiz', 'practice'), nullable=False)
    content_url = db.Column(db.String(255))
    duration_minutes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    # Relationships
    learning_activities = db.relationship('LearningActivity', backref='course')
    progress_records = db.relationship('StudentProgress', backref='course')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'subject_id': self.subject_id,
            'difficulty_level': self.difficulty_level,
            'content_type': self.content_type,
            'content_url': self.content_url,
            'duration_minutes': self.duration_minutes,
            'is_active': self.is_active
        }


class LearningActivity(db.Model):
    __tablename__ = 'learning_activities'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.id'), nullable=False)
    activity_type = db.Column(
        db.Enum('view', 'complete', 'quiz_attempt', 'practice'), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    score = db.Column(db.Float)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'course_id': self.course_id,
            'activity_type': self.activity_type,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'score': self.score,
            'completed': self.completed
        }


class StudentProgress(db.Model):
    __tablename__ = 'student_progress'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'student_profiles.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.id'), nullable=False)
    progress_percentage = db.Column(db.Float, default=0.0)
    last_accessed = db.Column(db.DateTime, default=datetime.utcnow)
    completion_date = db.Column(db.DateTime)
    grade = db.Column(db.String(5))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'progress_percentage': self.progress_percentage,
            'last_accessed': self.last_accessed.isoformat() if self.last_accessed else None,
            'completion_date': self.completion_date.isoformat() if self.completion_date else None,
            'grade': self.grade
        }


class AIRecommendation(db.Model):
    __tablename__ = 'ai_recommendations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.id'), nullable=False)
    recommendation_type = db.Column(
        db.Enum('content', 'difficulty', 'timing', 'sequence'), nullable=False)
    match_score = db.Column(db.Float, nullable=False)
    reasoning = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    # Relationships
    user = db.relationship('User', backref='recommendations')
    course = db.relationship('Course', backref='recommendations')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'course_id': self.course_id,
            'recommendation_type': self.recommendation_type,
            'match_score': self.match_score,
            'reasoning': self.reasoning,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_active': self.is_active
        }


class SystemMetrics(db.Model):
    __tablename__ = 'system_metrics'

    id = db.Column(db.Integer, primary_key=True)
    metric_name = db.Column(db.String(100), nullable=False)
    metric_value = db.Column(db.Float, nullable=False)
    metric_unit = db.Column(db.String(20))
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'metric_name': self.metric_name,
            'metric_value': self.metric_value,
            'metric_unit': self.metric_unit,
            'recorded_at': self.recorded_at.isoformat() if self.recorded_at else None
        }


class UserFeedback(db.Model):
    __tablename__ = 'user_feedback'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    feedback_type = db.Column(
        db.Enum('system', 'content', 'feature', 'bug'), nullable=False)
    rating = db.Column(db.Integer)  # 1-5 scale
    comments = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', backref='feedbacks')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'feedback_type': self.feedback_type,
            'rating': self.rating,
            'comments': self.comments,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
