# LENTERAMU Platform Configuration Template
# Copy this file to config.py and modify the values

import os
from datetime import timedelta


class Config:
    """Base configuration class"""

    # =============================================================================
    # SECRET KEY CONFIGURATION
    # =============================================================================
    # IMPORTANT: Change this to a random secret key in production!
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'lenteramu-development-secret-key-change-in-production'

    # =============================================================================
    # DATABASE CONFIGURATION
    # =============================================================================
    # MySQL Database Configuration
    # Format: mysql+pymysql://username:password@host:port/database_name

    # Development Database (Local)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://lenteramu_user:your_password@localhost:3306/lenteramu'

    # Production Database (Update for production)
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://prod_user:prod_password@prod_host:3306/lenteramu_prod'

    # Database Configuration Options
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # Set to True for SQL query debugging
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
        'pool_timeout': 20,
        'max_overflow': 0
    }

    # =============================================================================
    # SESSION CONFIGURATION
    # =============================================================================
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_KEY_PREFIX = 'lenteramu:'
    SESSION_COOKIE_NAME = 'lenteramu_session'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

    # =============================================================================
    # APPLICATION CONFIGURATION
    # =============================================================================
    # Flask Application Settings
    DEBUG = True  # Set to False in production
    TESTING = False

    # Application Info
    APP_NAME = 'LENTERAMU'
    APP_VERSION = '1.0.0'
    APP_DESCRIPTION = 'Learning Enhancement Through Adaptive Intelligence for Meaningful Understanding'

    # =============================================================================
    # AI/ML CONFIGURATION
    # =============================================================================
    # Machine Learning Settings
    AI_MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models')
    AI_TRAINING_DATA_PATH = os.path.join(
        os.path.dirname(__file__), 'data', 'training')

    # AI Learning Process Settings
    AI_LEARNING_PROCESS_ENABLED = True
    AI_AUTO_RETRAIN = True
    AI_RETRAIN_INTERVAL_HOURS = 24
    AI_MIN_TRAINING_SAMPLES = 100

    # Recommendation Engine Settings
    RECOMMENDATION_THRESHOLD = 0.7
    MAX_RECOMMENDATIONS_PER_USER = 10
    RECOMMENDATION_REFRESH_INTERVAL = 3600  # seconds

    # Adaptive Feedback Settings
    FEEDBACK_CONFIDENCE_THRESHOLD = 0.6
    MAX_FEEDBACK_LENGTH = 500
    FEEDBACK_PERSONALIZATION_LEVEL = 'high'  # low, medium, high

    # =============================================================================
    # PERFORMANCE CONFIGURATION
    # =============================================================================
    # Pagination Settings
    USERS_PER_PAGE = 20
    ACTIVITIES_PER_PAGE = 10
    RECOMMENDATIONS_PER_PAGE = 5

    # Cache Settings
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300

    # File Upload Settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png',
                          'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}

    # =============================================================================
    # SECURITY CONFIGURATION
    # =============================================================================
    # Security Headers
    SECURITY_HEADERS = {
        'X-Frame-Options': 'SAMEORIGIN',
        'X-Content-Type-Options': 'nosniff',
        'X-XSS-Protection': '1; mode=block'
    }

    # Password Security
    MIN_PASSWORD_LENGTH = 8
    REQUIRE_PASSWORD_COMPLEXITY = True

    # Rate Limiting
    RATE_LIMIT_ENABLED = True
    RATE_LIMIT_GENERAL = "100 per minute"
    RATE_LIMIT_AUTH = "5 per minute"
    RATE_LIMIT_AI = "10 per minute"

    # =============================================================================
    # LOGGING CONFIGURATION
    # =============================================================================
    # Logging Settings
    LOG_LEVEL = 'INFO'  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    LOG_FILE = 'logs/lenteramu.log'
    LOG_MAX_BYTES = 10 * 1024 * 1024  # 10MB
    LOG_BACKUP_COUNT = 5

    # =============================================================================
    # EMAIL CONFIGURATION (Optional)
    # =============================================================================
    # Email Settings for notifications
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in [
        'true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[LENTERAMU] '
    MAIL_SENDER = 'LENTERAMU Admin <noreply@lenteramu.id>'

    # =============================================================================
    # EXTERNAL SERVICES CONFIGURATION
    # =============================================================================
    # Redis Configuration (if using Redis for caching/sessions)
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'

    # Analytics & Monitoring
    GOOGLE_ANALYTICS_ID = os.environ.get('GOOGLE_ANALYTICS_ID')
    SENTRY_DSN = os.environ.get('SENTRY_DSN')  # Error tracking

    # =============================================================================
    # DEVELOPMENT CONFIGURATION
    # =============================================================================
    @staticmethod
    def init_app(app):
        """Initialize application with configuration"""
        pass


class DevelopmentConfig(Config):
    """Development environment configuration"""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Show SQL queries in console
    LOG_LEVEL = 'DEBUG'

    # Development Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql+pymysql://lenteramu_user:dev_password@localhost:3306/lenteramu_dev'


class ProductionConfig(Config):
    """Production environment configuration"""
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True  # Require HTTPS
    LOG_LEVEL = 'WARNING'

    # Production Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://prod_user:prod_password@prod_host:3306/lenteramu_prod'

    # Enhanced Security for Production
    SECURITY_HEADERS.update({
        'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
        'Content-Security-Policy': "default-src 'self'"
    })

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # Log to syslog in production
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)


class TestingConfig(Config):
    """Testing environment configuration"""
    TESTING = True
    WTF_CSRF_ENABLED = False

    # In-memory database for testing
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    # Disable AI processing during tests
    AI_LEARNING_PROCESS_ENABLED = False
    AI_AUTO_RETRAIN = False


# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

# =============================================================================
# EXAMPLE ENVIRONMENT VARIABLES (.env file)
# =============================================================================
"""
Create a .env file in your project root with these variables:

# Database Configuration
DATABASE_URL=mysql+pymysql://lenteramu_user:your_password@localhost:3306/lenteramu
DEV_DATABASE_URL=mysql+pymysql://lenteramu_user:dev_password@localhost:3306/lenteramu_dev

# Application Security
SECRET_KEY=your-super-secret-key-here
FLASK_ENV=development

# Email Configuration (Optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# External Services (Optional)
REDIS_URL=redis://localhost:6379/0
GOOGLE_ANALYTICS_ID=GA_TRACKING_ID
SENTRY_DSN=your-sentry-dsn

# AI/ML Configuration
AI_MODEL_PATH=./models
RECOMMENDATION_THRESHOLD=0.7
"""

# =============================================================================
# DATABASE INITIALIZATION EXAMPLE
# =============================================================================
"""
To set up the database, run these MySQL commands:

mysql -u root -p

CREATE DATABASE lenteramu CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE lenteramu_dev CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE lenteramu_test CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'lenteramu_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON lenteramu.* TO 'lenteramu_user'@'localhost';
GRANT ALL PRIVILEGES ON lenteramu_dev.* TO 'lenteramu_user'@'localhost';
GRANT ALL PRIVILEGES ON lenteramu_test.* TO 'lenteramu_user'@'localhost';

FLUSH PRIVILEGES;
exit;
"""
