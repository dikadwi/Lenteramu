# 🔌 DOKUMENTASI API LENTERAMU

## Complete API Reference Guide

---

## 📋 **DAFTAR ISI**

1. [API Overview](#1-api-overview)
2. [Authentication](#2-authentication)
3. [Main Application Endpoints](#3-main-application-endpoints)
4. [Workflow API](#4-workflow-api)
5. [AI & Machine Learning API](#5-ai--machine-learning-api)
6. [Analytics API](#6-analytics-api)
7. [Database API](#7-database-api)
8. [Error Handling](#8-error-handling)
9. [Rate Limiting](#9-rate-limiting)
10. [Examples](#10-examples)

---

## 1. **API OVERVIEW**

### 🌐 **Base URL**

```
Development: http://localhost:5000
Production: https://api.lenteramu.id
```

### 📋 **API Features**

- ✅ **RESTful Design**: Standard HTTP methods
- ✅ **JSON Responses**: Consistent data format
- ✅ **Session-based Auth**: Secure user sessions
- ✅ **Error Handling**: Standardized error responses
- ✅ **Real-time Data**: Live updates untuk analytics

### 📊 **Response Format**

```json
{
  "status": "success|error",
  "message": "Description of the response",
  "data": {
    // Response data
  },
  "timestamp": "2025-09-04T10:30:00Z"
}
```

---

## 2. **AUTHENTICATION**

### 🔐 **Session Management**

LENTERAMU menggunakan Flask session-based authentication.

#### 🔑 **Login Process**

```http
POST /login
Content-Type: application/json

{
  "username": "student1",
  "password": "password123",
  "role": "student"
}
```

**Response:**

```json
{
  "status": "success",
  "message": "Login successful",
  "data": {
    "user_id": 1,
    "username": "student1",
    "role": "student",
    "session_id": "abc123"
  }
}
```

#### 🚪 **Logout Process**

```http
POST /logout
```

**Response:**

```json
{
  "status": "success",
  "message": "Logout successful"
}
```

### 🛡️ **Role-based Access**

- **Student**: Access to learning features
- **Teacher**: Access to class management
- **Admin**: Full system access

---

## 3. **MAIN APPLICATION ENDPOINTS**

### 🏠 **Homepage**

```http
GET /
```

**Description**: Main landing page
**Authentication**: None required
**Response**: HTML template

### 👨‍🎓 **Student Dashboard**

```http
GET /dashboard/siswa
```

**Description**: Student personal dashboard
**Authentication**: Student role required
**Response**: HTML template dengan student data

**Data Included:**

- Personal progress statistics
- AI recommendations
- Recent learning activities
- Achievement badges

### 👨‍💼 **Admin Dashboard**

```http
GET /dashboard/admin
```

**Description**: Administrator control panel
**Authentication**: Admin role required
**Response**: HTML template dengan system data

**Data Included:**

- System health metrics
- User statistics
- Recent activities
- Performance indicators

### 📊 **Analytics Dashboard**

```http
GET /analytics/student
```

**Description**: Student analytics dan insights
**Authentication**: Student/Teacher/Admin
**Response**: HTML template dengan analytics data

### 👁️ **System Monitoring**

```http
GET /monitoring
```

**Description**: Real-time system monitoring
**Authentication**: Admin role required
**Response**: HTML template dengan monitoring data

### 🤖 **AI Personalization**

```http
GET /ai_personalization
```

**Description**: AI personalization interface
**Authentication**: Required
**Response**: HTML template dengan AI features

---

## 4. **WORKFLOW API**

### 👨‍🎓 **Student Workflow**

```http
GET /student/workflow
```

**Description**: Student learning workflow interface
**Authentication**: Student role
**Response**: HTML template

**Data Structure:**

```json
{
  "activities": [
    {
      "id": 1,
      "activity_type": "quiz_attempt",
      "score": 85,
      "created_at": "2025-09-04T10:00:00Z"
    }
  ],
  "recommendations": [
    {
      "id": 1,
      "recommendation_type": "next_topic",
      "content": "Math Advanced Topics",
      "confidence": 0.8
    }
  ],
  "progress_percentage": 75,
  "total_activities": 10
}
```

### 👨‍🏫 **Teacher Workflow**

```http
GET /teacher/workflow
```

**Description**: Teacher management workflow
**Authentication**: Teacher role
**Response**: HTML template

**Data Structure:**

```json
{
  "total_courses": 5,
  "total_students": 30,
  "recent_activities": [
    {
      "student_name": "John Doe",
      "activity": "completed_quiz",
      "score": 90,
      "timestamp": "2025-09-04T09:30:00Z"
    }
  ],
  "metrics": [
    {
      "metric_name": "average_score",
      "metric_value": 85.5,
      "metric_unit": "%"
    }
  ]
}
```

### 👨‍💼 **Admin Workflow**

```http
GET /admin/workflow
```

**Description**: Administrator system workflow
**Authentication**: Admin role
**Response**: HTML template

**Data Structure:**

```json
{
  "total_users": 150,
  "active_users": 120,
  "system_health": {
    "uptime": "99.8%",
    "response_time": "250ms",
    "error_rate": "0.02%"
  },
  "recent_activities": [
    {
      "user": "student1",
      "activity": "login",
      "timestamp": "2025-09-04T10:15:00Z"
    }
  ]
}
```

---

## 5. **AI & MACHINE LEARNING API**

### 🧠 **AI Learning Process**

```http
POST /ai/learning-process
Content-Type: application/json

{
  "user_id": 1,
  "trigger_training": true
}
```

**Response:**

```json
{
  "status": "success",
  "message": "AI learning process initiated",
  "data": {
    "process_id": "ai_proc_001",
    "stages": [
      {
        "stage": "data_collection",
        "status": "completed",
        "duration": "2.3s"
      },
      {
        "stage": "preprocessing",
        "status": "in_progress",
        "progress": 45
      }
    ],
    "estimated_completion": "2025-09-04T10:35:00Z"
  }
}
```

### 🎯 **Adaptive Feedback**

```http
POST /ai/adaptive-feedback
Content-Type: application/json

{
  "user_id": 1,
  "assessment_data": {
    "quiz_score": 85,
    "time_spent": 1200,
    "difficulty_level": "intermediate"
  }
}
```

**Response:**

```json
{
  "status": "success",
  "message": "Adaptive feedback generated",
  "data": {
    "feedback_id": "fb_001",
    "personalized_feedback": "Great job! You're showing strong understanding...",
    "recommendations": [
      {
        "type": "next_topic",
        "content": "Advanced Algebra",
        "reason": "Based on your current performance"
      }
    ],
    "difficulty_adjustment": {
      "current": "intermediate",
      "recommended": "advanced",
      "confidence": 0.85
    }
  }
}
```

### 🔮 **Get AI Recommendations**

```http
GET /ai/recommendations?user_id=1&limit=5
```

**Response:**

```json
{
  "status": "success",
  "data": {
    "recommendations": [
      {
        "id": 1,
        "type": "learning_content",
        "title": "Calculus Fundamentals",
        "description": "Based on your math progress",
        "confidence": 0.9,
        "created_at": "2025-09-04T10:00:00Z"
      }
    ],
    "total_count": 12,
    "page": 1
  }
}
```

---

## 6. **ANALYTICS API**

### 📊 **User Performance Analytics**

```http
GET /analytics/performance?user_id=1&period=30d
```

**Response:**

```json
{
  "status": "success",
  "data": {
    "performance_metrics": {
      "average_score": 87.5,
      "completion_rate": 92.3,
      "study_time_hours": 45.2,
      "activities_completed": 28
    },
    "trends": [
      {
        "date": "2025-09-01",
        "score": 85,
        "activities": 3
      },
      {
        "date": "2025-09-02",
        "score": 88,
        "activities": 4
      }
    ],
    "subject_breakdown": {
      "mathematics": 90,
      "science": 85,
      "language": 87
    }
  }
}
```

### 📈 **Learning Progress**

```http
GET /analytics/progress?user_id=1
```

**Response:**

```json
{
  "status": "success",
  "data": {
    "overall_progress": 75.5,
    "current_level": "intermediate",
    "subjects": [
      {
        "name": "Mathematics",
        "progress": 82.3,
        "last_activity": "2025-09-04T09:00:00Z"
      }
    ],
    "milestones": [
      {
        "name": "First Quiz Completed",
        "achieved_at": "2025-08-15T10:00:00Z",
        "points": 100
      }
    ]
  }
}
```

### 📊 **System Analytics**

```http
GET /analytics/system
```

**Authentication**: Admin only

**Response:**

```json
{
  "status": "success",
  "data": {
    "user_metrics": {
      "total_users": 150,
      "active_today": 45,
      "new_registrations": 5
    },
    "usage_metrics": {
      "page_views": 1250,
      "api_calls": 890,
      "average_session_duration": "25m"
    },
    "performance_metrics": {
      "response_time_avg": "245ms",
      "error_rate": "0.02%",
      "uptime": "99.8%"
    }
  }
}
```

---

## 7. **DATABASE API**

### 👥 **User Management**

#### Get Users

```http
GET /api/users?page=1&limit=10&role=student
```

**Response:**

```json
{
  "status": "success",
  "data": {
    "users": [
      {
        "id": 1,
        "username": "student1",
        "email": "student1@example.com",
        "role": "student",
        "is_active": true,
        "created_at": "2025-08-01T10:00:00Z"
      }
    ],
    "pagination": {
      "current_page": 1,
      "total_pages": 15,
      "total_users": 150
    }
  }
}
```

#### Create User

```http
POST /api/users
Content-Type: application/json

{
  "username": "newstudent",
  "email": "newstudent@example.com",
  "password": "securepassword",
  "role": "student",
  "full_name": "New Student"
}
```

### 📚 **Course Management**

#### Get Courses

```http
GET /api/courses
```

**Response:**

```json
{
  "status": "success",
  "data": {
    "courses": [
      {
        "id": 1,
        "title": "Mathematics Grade 10",
        "description": "Basic mathematics concepts",
        "teacher_id": 2,
        "created_at": "2025-08-01T00:00:00Z",
        "subjects": [
          {
            "id": 1,
            "name": "Algebra",
            "description": "Linear and quadratic equations"
          }
        ]
      }
    ]
  }
}
```

### 📊 **Learning Activities**

#### Get Activities

```http
GET /api/activities?user_id=1&limit=20
```

#### Create Activity

```http
POST /api/learning-activity
Content-Type: application/json

{
  "user_id": 1,
  "activity_type": "quiz_attempt",
  "content": "Mathematics Quiz 1",
  "score": 85,
  "duration": 1200
}
```

### 📈 **System Metrics**

```http
GET /api/metrics?metric_name=user_engagement&period=7d
```

**Response:**

```json
{
  "status": "success",
  "data": {
    "metrics": [
      {
        "id": 1,
        "metric_name": "user_engagement",
        "metric_value": 87.5,
        "metric_unit": "%",
        "recorded_at": "2025-09-04T10:00:00Z"
      }
    ]
  }
}
```

---

## 8. **ERROR HANDLING**

### 🚨 **Standard Error Format**

```json
{
  "status": "error",
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "Username or password is incorrect",
    "details": "Authentication failed for user: student1"
  },
  "timestamp": "2025-09-04T10:30:00Z"
}
```

### 📋 **Common Error Codes**

| Code                        | HTTP Status | Description                  |
| --------------------------- | ----------- | ---------------------------- |
| `INVALID_CREDENTIALS`       | 401         | Authentication failed        |
| `INSUFFICIENT_PERMISSIONS`  | 403         | Access denied                |
| `RESOURCE_NOT_FOUND`        | 404         | Requested resource not found |
| `VALIDATION_ERROR`          | 400         | Input validation failed      |
| `RATE_LIMIT_EXCEEDED`       | 429         | Too many requests            |
| `INTERNAL_SERVER_ERROR`     | 500         | Server error                 |
| `DATABASE_CONNECTION_ERROR` | 503         | Database unavailable         |

### 🔧 **Error Response Examples**

#### Validation Error

```json
{
  "status": "error",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "field_errors": {
        "email": "Invalid email format",
        "password": "Password too short"
      }
    }
  }
}
```

#### Authentication Error

```json
{
  "status": "error",
  "error": {
    "code": "INSUFFICIENT_PERMISSIONS",
    "message": "Admin access required",
    "details": "User role 'student' cannot access admin endpoints"
  }
}
```

---

## 9. **RATE LIMITING**

### ⚡ **Rate Limits**

- **General API**: 100 requests per minute
- **AI Endpoints**: 10 requests per minute
- **Analytics**: 50 requests per minute
- **Authentication**: 5 attempts per minute

### 📊 **Rate Limit Headers**

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1693833600
```

### 🚫 **Rate Limit Response**

```json
{
  "status": "error",
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests",
    "details": "Rate limit: 100 requests per minute. Try again in 30 seconds."
  },
  "retry_after": 30
}
```

---

## 10. **EXAMPLES**

### 🚀 **Complete User Journey Example**

#### 1. User Login

```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "student1",
    "password": "password123",
    "role": "student"
  }' \
  -c cookies.txt
```

#### 2. Get User Dashboard

```bash
curl -X GET http://localhost:5000/dashboard/siswa \
  -b cookies.txt
```

#### 3. Get AI Recommendations

```bash
curl -X GET "http://localhost:5000/ai/recommendations?user_id=1&limit=5" \
  -b cookies.txt
```

#### 4. Submit Learning Activity

```bash
curl -X POST http://localhost:5000/api/learning-activity \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{
    "user_id": 1,
    "activity_type": "quiz_attempt",
    "content": "Mathematics Quiz 1",
    "score": 85,
    "duration": 1200
  }'
```

#### 5. Get Analytics

```bash
curl -X GET "http://localhost:5000/analytics/performance?user_id=1&period=30d" \
  -b cookies.txt
```

### 🤖 **AI Integration Example**

#### Trigger AI Learning Process

```javascript
// JavaScript Example
async function triggerAILearning(userId) {
  try {
    const response = await fetch("/ai/learning-process", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user_id: userId,
        trigger_training: true,
      }),
    });

    const data = await response.json();

    if (data.status === "success") {
      console.log("AI process started:", data.data.process_id);
      monitorAIProcess(data.data.process_id);
    }
  } catch (error) {
    console.error("AI process failed:", error);
  }
}
```

#### Generate Adaptive Feedback

```python
# Python Example
import requests

def generate_adaptive_feedback(user_id, assessment_data):
    url = "http://localhost:5000/ai/adaptive-feedback"

    payload = {
        "user_id": user_id,
        "assessment_data": assessment_data
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return data['data']

    return None

# Usage
assessment = {
    "quiz_score": 85,
    "time_spent": 1200,
    "difficulty_level": "intermediate"
}

feedback = generate_adaptive_feedback(1, assessment)
print(feedback['personalized_feedback'])
```

### 📊 **Analytics Integration Example**

#### Real-time Dashboard Update

```javascript
// Real-time Analytics Dashboard
class AnalyticsDashboard {
  constructor(userId) {
    this.userId = userId;
    this.updateInterval = 30000; // 30 seconds
    this.startRealTimeUpdates();
  }

  async fetchAnalytics() {
    try {
      const response = await fetch(
        `/analytics/performance?user_id=${this.userId}&period=7d`
      );
      const data = await response.json();

      if (data.status === "success") {
        this.updateCharts(data.data);
      }
    } catch (error) {
      console.error("Failed to fetch analytics:", error);
    }
  }

  updateCharts(data) {
    // Update Chart.js charts dengan new data
    this.progressChart.data.datasets[0].data = data.trends.map((t) => t.score);
    this.progressChart.update();

    // Update statistics
    document.getElementById("average-score").textContent =
      data.performance_metrics.average_score;
    document.getElementById("completion-rate").textContent =
      data.performance_metrics.completion_rate + "%";
  }

  startRealTimeUpdates() {
    setInterval(() => {
      this.fetchAnalytics();
    }, this.updateInterval);
  }
}

// Initialize dashboard
const dashboard = new AnalyticsDashboard(1);
```

---

## 📚 **SDK DAN LIBRARIES**

### 🐍 **Python SDK Example**

```python
class LenteramuAPI:
    def __init__(self, base_url, session=None):
        self.base_url = base_url
        self.session = session or requests.Session()

    def login(self, username, password, role):
        response = self.session.post(f"{self.base_url}/login", json={
            "username": username,
            "password": password,
            "role": role
        })
        return response.json()

    def get_ai_recommendations(self, user_id, limit=10):
        response = self.session.get(f"{self.base_url}/ai/recommendations", params={
            "user_id": user_id,
            "limit": limit
        })
        return response.json()

    def create_learning_activity(self, user_id, activity_type, content, score=None):
        response = self.session.post(f"{self.base_url}/api/learning-activity", json={
            "user_id": user_id,
            "activity_type": activity_type,
            "content": content,
            "score": score
        })
        return response.json()

# Usage
api = LenteramuAPI("http://localhost:5000")
api.login("student1", "password123", "student")
recommendations = api.get_ai_recommendations(1, 5)
```

### 🌐 **JavaScript SDK Example**

```javascript
class LenteramuAPI {
  constructor(baseUrl) {
    this.baseUrl = baseUrl;
  }

  async login(username, password, role) {
    const response = await fetch(`${this.baseUrl}/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password, role }),
    });
    return response.json();
  }

  async getAnalytics(userId, period = "7d") {
    const response = await fetch(
      `${this.baseUrl}/analytics/performance?user_id=${userId}&period=${period}`
    );
    return response.json();
  }

  async triggerAIProcess(userId) {
    const response = await fetch(`${this.baseUrl}/ai/learning-process`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, trigger_training: true }),
    });
    return response.json();
  }
}

// Usage
const api = new LenteramuAPI("http://localhost:5000");
```

---

## 🔧 **DEVELOPMENT TOOLS**

### 📋 **API Testing dengan Postman**

1. **Import Collection**: Download Postman collection
2. **Environment Setup**: Configure base URL dan variables
3. **Authentication**: Set up session cookies
4. **Test Automation**: Automated API testing

### 🐛 **Debugging Tools**

- **Flask Debug Mode**: Detailed error messages
- **SQL Query Logging**: Database operation monitoring
- **Performance Profiling**: Response time analysis
- **Error Tracking**: Comprehensive error logging

### 📊 **Monitoring Tools**

- **Health Check Endpoints**: System status monitoring
- **Metrics Collection**: Performance data gathering
- **Log Aggregation**: Centralized logging
- **Alert System**: Automated issue detection

---

**📅 Last Updated: September 4, 2025**
**🔄 API Version: 1.0.0**
**👥 Team: LENTERAMU Development Team**

_API documentation akan terus diperbarui seiring dengan pengembangan fitur baru._
