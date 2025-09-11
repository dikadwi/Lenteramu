# 🎓 LENTERAMU - Platform Pembelajaran Adaptif Berbasis AI

<div align="center">

![LENTERAMU Logo](https://img.shields.io/badge/LENTERAMU-AI%20Learning%20Platform-blue?style=for-the-badge&logo=graduation-cap)

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange?style=flat-square&logo=mysql)](https://mysql.com)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.0-yellow?style=flat-square&logo=scikit-learn)](https://scikit-learn.org)

**Learning Enhancement Through Adaptive Intelligence for Meaningful Understanding**

[🚀 Demo](#demo) • [📖 Dokumentasi](#dokumentasi) • [🛠️ Instalasi](#instalasi) • [🤝 Kontribusi](#kontribusi)

</div>

---

## 📋 **TENTANG LENTERAMU**

LENTERAMU adalah platform pembelajaran adaptif yang memanfaatkan kecerdasan buatan untuk memberikan pengalaman belajar yang dipersonalisasi. Platform ini dirancang untuk siswa, guru, dan administrator dengan fitur-fitur canggih yang mengoptimalkan proses pembelajaran.

### ✨ **Fitur Utama**

- 🧠 **AI-Powered Learning**: Sistem pembelajaran berbasis kecerdasan buatan
- 🎯 **Adaptive Feedback**: Umpan balik yang menyesuaikan dengan kemampuan siswa
- 📊 **Real-time Analytics**: Analisis performa pembelajaran secara real-time
- 👥 **Multi-Role Support**: Mendukung siswa, guru, dan administrator
- 🎨 **Modern UI/UX**: Interface modern dengan glass morphism design
- 📱 **Responsive Design**: Kompatible dengan semua perangkat

---

## 🏗️ **ARSITEKTUR SISTEM**

```
LENTERAMU Platform Architecture
┌─────────────────────────────────────────────────────────────┐
│                    Frontend Layer                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐  │
│  │   HTML5     │ │    CSS3     │ │    JavaScript      │  │
│  │  Templates  │ │ Glass       │ │  Interactive       │  │
│  │  (Jinja2)   │ │ Morphism    │ │  Features          │  │
│  └─────────────┘ └─────────────┘ └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                    Backend Layer                           │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐  │
│  │    Flask    │ │ SQLAlchemy  │ │   Session Mgmt     │  │
│  │   Routes    │ │     ORM     │ │  Authentication    │  │
│  │   & APIs    │ │             │ │                    │  │
│  └─────────────┘ └─────────────┘ └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                  Database Layer                            │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐  │
│  │    MySQL    │ │   User      │ │    Learning        │  │
│  │  Database   │ │ Management  │ │     Content        │  │
│  │             │ │             │ │                    │  │
│  └─────────────┘ └─────────────┘ └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                   AI/ML Layer                              │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐  │
│  │  Learning   │ │  Adaptive   │ │  Recommendation    │  │
│  │  Process    │ │  Feedback   │ │     Engine         │  │
│  │   Engine    │ │   System    │ │                    │  │
│  └─────────────┘ └─────────────┘ └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 **DEMO**

### 📸 **Screenshots**

#### 🏠 Dashboard Utama

```
┌─────────────────────────────────────────────────────────────┐
│ 🎓 LENTERAMU  │  🏠 Beranda │ 👨‍🎓 Dashboard │ 🛣️ Workflow ▼  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ✨ Selamat Datang di LENTERAMU                            │
│     Platform Pembelajaran Adaptif Berbasis AI              │
│                                                             │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐  │
│  │📊 Analytics │ │🤖 AI Learn  │ │👥 User Management  │  │
│  │    Dashboard│ │   Process   │ │                    │  │
│  └─────────────┘ └─────────────┘ └─────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### 👨‍🎓 Student Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│                Student Learning Dashboard                   │
├─────────────────────────────────────────────────────────────┤
│  📊 Progress: 75% ████████████░░░                          │
│  🎯 Next Goal: Complete Math Quiz                          │
│  🏆 Achievements: 5 badges earned                          │
│                                                             │
│  🤖 AI Recommendations:                                    │
│  • Advanced Algebra Topics                                 │
│  • Geometry Practice Tests                                 │
│  • Physics Fundamentals                                    │
└─────────────────────────────────────────────────────────────┘
```

### 🎬 **Live Demo**

- **URL**: http://localhost:5000
- **Demo Account**:
  - Username: `demo_student` | Password: `demo123` | Role: Student
  - Username: `demo_teacher` | Password: `demo123` | Role: Teacher
  - Username: `demo_admin` | Password: `demo123` | Role: Admin

---

## 🛠️ **INSTALASI**

### 📋 **Persyaratan Sistem**

- **Python**: 3.11 atau lebih baru
- **MySQL**: 8.0 atau lebih baru
- **Memory**: Minimum 4GB RAM
- **Storage**: Minimum 1GB ruang kosong
- **Browser**: Chrome 80+, Firefox 75+, Safari 13+

### ⚡ **Quick Start**

#### 1️⃣ Clone Repository

```bash
git clone https://github.com/lenteramu/lenteramu-platform.git
cd lenteramu-platform
```

#### 2️⃣ Setup Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Database Setup

```bash
# Login ke MySQL
mysql -u root -p

# Create database dan user
CREATE DATABASE lenteramu;
CREATE USER 'lenteramu_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON lenteramu.* TO 'lenteramu_user'@'localhost';
FLUSH PRIVILEGES;
exit;
```

#### 5️⃣ Configure Environment

```bash
# Copy file konfigurasi
cp config.example.py config.py

# Edit konfigurasi database
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lenteramu_user:your_password@localhost/lenteramu'
```

#### 6️⃣ Initialize Database

```bash
python init_db.py
```

#### 7️⃣ Run Application

```bash
python app.py
```

### 🌐 **Akses Aplikasi**

Buka browser dan akses: `http://localhost:5000`

---

## 📖 **DOKUMENTASI**

### 📚 **Dokumentasi Lengkap**

- 📋 **[Dokumentasi Aplikasi](DOKUMENTASI_APLIKASI.md)** - Panduan lengkap aplikasi
- 🗺️ **[Dokumentasi Menu & Fitur](DOKUMENTASI_MENU_FITUR.md)** - Detail menu dan fitur
- 🔌 **[Dokumentasi API](DOKUMENTASI_API.md)** - Reference API untuk developer
- 🔄 **[Workflow Implementation](workflow_implementation_summary.md)** - Summary implementasi
- 📐 **[Arsitektur Sistem](arsitektur.md)** - Desain arsitektur aplikasi

### 🎯 **Quick References**

#### 👨‍🎓 **Untuk Siswa**

- Login → Dashboard → Lihat AI Recommendations → Mulai Belajar
- [Panduan Student Workflow](DOKUMENTASI_MENU_FITUR.md#workflow-siswa)

#### 👨‍🏫 **Untuk Guru**

- Login → Teacher Dashboard → Kelola Kelas → Monitor Progress
- [Panduan Teacher Workflow](DOKUMENTASI_MENU_FITUR.md#workflow-guru)

#### 👨‍💼 **Untuk Administrator**

- Login → Admin Dashboard → Monitor Sistem → Kelola User
- [Panduan Admin Workflow](DOKUMENTASI_MENU_FITUR.md#workflow-admin)

---

## 🔧 **DEVELOPMENT**

### 🛠️ **Tech Stack**

```yaml
Backend:
  - Framework: Flask 2.3.3
  - ORM: SQLAlchemy 2.0.23
  - Database: MySQL 8.0+ dengan PyMySQL
  - AI/ML: Scikit-learn 1.3.0

Frontend:
  - Templates: Jinja2
  - Styling: CSS3 Glass Morphism
  - JavaScript: ES6 dengan Chart.js
  - Icons: Font Awesome 6.0.0

Infrastructure:
  - Session Management: Flask-Session
  - Environment: Python Virtual Environment
  - Development Server: Flask Development Server
```

### 📁 **Struktur Project**

```
lenteramu/
├── 📁 ai/                     # AI/ML Components
│   ├── learning_process.py    # AI Learning Engine
│   ├── adaptive_feedback.py   # Feedback System
│   └── retrain.py            # Model Retraining
├── 📁 templates/              # HTML Templates
│   ├── base.html             # Base Template
│   ├── dashboard_siswa.html  # Student Dashboard
│   ├── dashboard_admin.html  # Admin Dashboard
│   └── 📁 workflows/         # Workflow Templates
├── 📁 static/                 # Static Assets
│   ├── 📁 css/               # Stylesheets
│   └── 📁 js/                # JavaScript Files
├── 📄 app.py                 # Main Application
├── 📄 models.py              # Database Models
├── 📄 config.py              # Configuration
└── 📄 requirements.txt       # Dependencies
```

### 🧪 **Testing**

```bash
# Run unit tests
python -m pytest tests/

# Run dengan coverage
python -m pytest --cov=./ tests/

# Manual testing
python app.py
# Visit http://localhost:5000
```

### 🔍 **Debugging**

```bash
# Enable debug mode
export FLASK_DEBUG=1
export FLASK_ENV=development
python app.py

# Check logs
tail -f logs/app.log

# Database debugging
python -c "from app import db; print(db.engine.execute('SHOW TABLES').fetchall())"
```

---

## 📊 **FITUR & KEMAMPUAN**

### 🧠 **AI & Machine Learning**

- ✅ **6-Stage Learning Process**: Data Collection → Training → Deployment
- ✅ **Adaptive Feedback System**: Personalized responses
- ✅ **Smart Recommendations**: ML-powered content suggestions
- ✅ **Performance Prediction**: Learning outcome forecasting
- ✅ **Pattern Recognition**: Learning behavior analysis

### 👥 **Multi-Role Support**

- 👨‍🎓 **Students**: Personalized learning experience
- 👨‍🏫 **Teachers**: Class management dan content creation
- 👨‍💼 **Administrators**: System monitoring dan user management

### 📊 **Analytics & Monitoring**

- 📈 **Real-time Analytics**: Live performance tracking
- 📊 **Interactive Charts**: Data visualization dengan Chart.js
- 🎯 **Progress Tracking**: Detailed learning progress
- 📱 **Responsive Dashboard**: Mobile-optimized interface

### 🎨 **User Experience**

- ✨ **Glass Morphism Design**: Modern transparent UI
- 🌊 **Smooth Animations**: CSS transitions dan effects
- 📱 **Responsive Layout**: Multi-device compatibility
- 🔄 **Real-time Updates**: Live data synchronization

---

## 🔐 **KEAMANAN**

### 🛡️ **Security Features**

- 🔐 **Session Management**: Secure Flask sessions
- 🔑 **Password Security**: Hashed password storage
- 👮 **Role-based Access**: Multi-level authorization
- 🛡️ **Input Validation**: XSS dan injection protection
- 📝 **Audit Logging**: Comprehensive activity tracking

### 🔒 **Best Practices**

- Regular security updates
- Environment variable protection
- Database connection security
- Error message sanitization
- Session timeout management

---

## 📈 **PERFORMANCE**

### ⚡ **Optimization Features**

- 🚀 **Fast Page Loading**: < 2 second load times
- 💾 **Smart Caching**: Efficient data caching
- 📊 **Optimized Queries**: Database query optimization
- 🔄 **Lazy Loading**: Progressive content loading
- 📱 **Mobile Performance**: Touch-optimized interactions

### 📊 **Monitoring Metrics**

- Response time tracking
- Error rate monitoring
- User engagement analytics
- System resource usage
- Database performance metrics

---

## 🤝 **KONTRIBUSI**

### 👥 **Development Team**

- **Project Lead**: LENTERAMU Development Team
- **AI Engineer**: Machine Learning Specialist
- **Frontend Developer**: UI/UX Expert
- **Backend Developer**: Full-stack Developer
- **QA Engineer**: Quality Assurance

### 🔄 **Contributing Guidelines**

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### 🐛 **Bug Reports**

- Use GitHub Issues
- Include detailed description
- Provide steps to reproduce
- Include system information

### 💡 **Feature Requests**

- Submit via GitHub Issues
- Explain use case dan benefit
- Provide mockups if applicable
- Discuss implementation approach

---

## 📞 **DUKUNGAN**

### 📧 **Kontak**

- **Email**: contact@lenteramu.id
- **Website**: https://lenteramu.id
- **Documentation**: https://docs.lenteramu.id
- **Support**: https://support.lenteramu.id

### 🌐 **Social Media**

- **LinkedIn**: [@LENTERAMU-Platform](https://linkedin.com/company/lenteramu)
- **Twitter**: [@LENTERAMU_AI](https://twitter.com/lenteramu_ai)
- **YouTube**: [@LENTERAMU-Tutorials](https://youtube.com/@lenteramu)

### 📚 **Resources**

- [Knowledge Base](https://wiki.lenteramu.id)
- [Community Forum](https://forum.lenteramu.id)
- [Video Tutorials](https://youtube.com/@lenteramu)
- [Developer Docs](https://dev.lenteramu.id)

---

## 📅 **ROADMAP**

### 🎯 **Version 1.1 (Q4 2025)**

- [ ] Mobile application (React Native)
- [ ] Advanced AI models (Deep Learning)
- [ ] Real-time collaboration features
- [ ] Multi-language support

### 🚀 **Version 1.2 (Q1 2026)**

- [ ] Virtual classroom integration
- [ ] Advanced analytics dashboard
- [ ] Third-party LMS integration
- [ ] API marketplace

### 🌟 **Future Vision**

- Global learning platform
- AI-powered curriculum generation
- Virtual reality learning experiences
- Blockchain-based certifications

---

## 📄 **LICENSE**

```
MIT License

Copyright (c) 2025 LENTERAMU Platform

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 **ACKNOWLEDGMENTS**

### 📚 **Open Source Libraries**

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [SQLAlchemy](https://sqlalchemy.org/) - Database ORM
- [Scikit-learn](https://scikit-learn.org/) - Machine learning
- [Chart.js](https://chartjs.org/) - Data visualization
- [Font Awesome](https://fontawesome.com/) - Icons

### 🎨 **Design Inspiration**

- Glass morphism design trends
- Modern educational platforms
- AI/ML interface best practices

### 👥 **Community**

- Educational technology community
- Open source contributors
- Beta testers dan early adopters

---

<div align="center">

**🌟 Star this repository if you find it helpful! 🌟**

[![GitHub stars](https://img.shields.io/github/stars/lenteramu/lenteramu-platform?style=social)](https://github.com/lenteramu/lenteramu-platform/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/lenteramu/lenteramu-platform?style=social)](https://github.com/lenteramu/lenteramu-platform/network)
[![GitHub issues](https://img.shields.io/github/issues/lenteramu/lenteramu-platform)](https://github.com/lenteramu/lenteramu-platform/issues)

---

**© 2025 LENTERAMU Platform. All rights reserved.**

_Platform pembelajaran masa depan dimulai dari sekarang._

</div>
