# 📚 Lenteramu Flask Application Documentation

---

## Table of Contents

1. [Introduction](#introduction)
2. [Architecture Overview](#architecture-overview)
3. [Folder Structure](#folder-structure)
4. [Features](#features)
5. [Blueprints & Routing](#blueprints--routing)
6. [Database & Models](#database--models)
7. [AI Modules](#ai-modules)
8. [Templates & UI](#templates--ui)
9. [API Endpoints](#api-endpoints)
10. [Error Handling](#error-handling)
11. [Setup & Installation](#setup--installation)
12. [Development Guide](#development-guide)
13. [Troubleshooting](#troubleshooting)
14. [License & Contact](#license--contact)

---

## 1. Introduction

Lenteramu is a modern, modular learning platform powered by Flask and AI. It provides personalized learning, adaptive feedback, and comprehensive analytics for students, teachers, and administrators.

---

## 2. Architecture Overview

- **Backend**: Python Flask, SQLAlchemy ORM, Flask-Migrate
- **Frontend**: Jinja2 templates, CSS/JS (custom & third-party)
- **AI Integration**: Custom modules for adaptive feedback and learning process
- **Blueprints**: Modular routing for each user role
- **Database**: MySQL (configurable)

---

## 3. Folder Structure

```
Lenteramu/
│
├── app.py                  # Main Flask app, config, blueprint registration
├── models.py               # SQLAlchemy models
├── routes/
│   ├── admin.py            # Admin routes (Blueprint)
│   ├── guru.py             # Teacher routes (Blueprint)
│   └── siswa.py            # Student routes (Blueprint)
├── ai/
│   ├── adaptive_feedback.py # AI feedback module
│   └── learning_process.py  # AI learning process module
├── templates/
│   ├── admin/              # Admin templates
│   ├── guru/               # Teacher templates
│   ├── siswa/              # Student templates
│   └── ...                 # Other templates (landing, error, etc.)
├── static/                 # Static assets (CSS, JS, images)
├── requirements.txt        # Python dependencies
└── dokumentasi_new.md      # Application documentation
```

---

## 4. Features

- **Authentication & Role Management**: Demo login for student, teacher, admin
- **Modular Dashboards**: Role-based dashboards and workflows
- **AI Personalization**: Content recommendations and adaptive feedback
- **Monitoring & Reporting**: Real-time system stats, surveys, analytics
- **Error Handling**: Custom error pages (404, 500, 403)
- **API Endpoints**: For dashboard refresh, notifications, progress, etc.

---

## 5. Blueprints & Routing

- **Blueprints**: Each role (admin, guru, siswa) has its own blueprint for clean separation and maintainability.
- **Main Routes**: Landing, login, logout, error handlers, API endpoints
- **Protected Routes**: Session-based authentication, context processor for user info
- **Example Registration**:
  ```python
  app.register_blueprint(admin_bp)
  app.register_blueprint(guru_bp)
  app.register_blueprint(siswa_bp)
  ```

---

## 6. Database & Models

- **ORM**: SQLAlchemy
- **Migration**: Flask-Migrate
- **Models**: User, StudentProfile, TeacherProfile, Subject, Course, LearningActivity, StudentProgress, AIRecommendation, SystemMetrics, UserFeedback
- **Config**: MySQL (default), can be changed via environment variable

---

## 7. AI Modules

- **ai/adaptive_feedback.py**: Adaptive feedback system for personalized learning
- **ai/learning_process.py**: AI-driven learning process, recommendations, model training & monitoring
- **Integration**: Called in routes for assessment, recommendations, and feedback

---

## 8. Templates & UI

- **Jinja2 Templates**: Organized by role and feature
- **Modern UI**: Custom CSS, responsive design, role-based navigation
- **Error Pages**: Custom templates for 404, 500, 403
- **Dashboard**: Dynamic data rendering for each role

---

## 9. API Endpoints

- `/api/dashboard/refresh/<role>`: Refresh dashboard data
- `/api/notifications/<role>`: Get latest notifications
- `/api/student/progress/<int:student_id>`: Student progress
- `/api/teacher/classes`: Teacher's classes
- `/api/admin/system-stats`: Real-time system stats
- `/ai/train-model`: Train AI model
- `/ai/monitor-model`: Monitor AI model
- `/ai/generate-recommendations/<int:student_id>`: AI recommendations
- `/assessment/submit`: Submit assessment & get feedback
- `/feedback/monitor/<int:user_id>`: Monitor & adjust learning

---

## 10. Error Handling

- **404**: Not Found (custom page)
- **500**: Internal Server Error (custom page, DB rollback)
- **403**: Forbidden (custom page)
- **Context Processor**: Ensures `user` variable always available in templates

---

## 11. Setup & Installation

1. **Clone repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure database** (edit `config.py` or set `DATABASE_URL` env)
4. **Initialize database**:
   ```bash
   flask db upgrade
   python app.py
   ```
5. **Run application**:
   ```bash
   python app.py
   ```

---

## 12. Development Guide

- **Add new routes**: Use Blueprint for modularity
- **Extend models**: Edit `models.py` and run migrations
- **Customize templates**: Edit files in `templates/`
- **Static assets**: Place CSS/JS/images in `static/`
- **Testing**: Use Flask test client or pytest

---

## 13. Troubleshooting

- **BuildError**: Check endpoint names in `url_for`, use `role.endpoint` for Blueprint
- **UndefinedError**: Ensure all context variables are passed to templates
- **ImportError**: Use absolute imports for modules
- **Database Error**: Check connection string and migration status

---

## 14. License & Contact

- **License**: MIT
- **Contact**: dikadwi (GitHub), Tim Lenteramu

---

> **Lenteramu**: Empowering personalized learning with AI. For more info, see each module's docstring and comments in the codebase.
