# 🐛 BugFlow AI

> **AI-powered bug tracking and intelligent bug analysis platform built with Django and Google Gemini.**

BugFlow AI is a web-based bug management system designed to help developers **report, track, organize, and analyze software bugs**. It combines traditional bug tracking with **AI-powered analysis** to provide useful insights and debugging suggestions.

---

## ✨ Features

* 🔐 User Registration & Login
* 🐛 Create and manage bugs
* 📋 Track bug status
* ⚡ Manage bug priority
* 🚨 Manage bug severity
* 🤖 AI-powered bug analysis
* 💡 AI-generated debugging suggestions
* 👤 User authentication
* 🗄️ SQLite database
* 🔌 Django REST Framework
* 🌐 CORS support
* 📦 Render deployment support

---

## 🛠️ Tech Stack

| Technology                 | Usage             |
| -------------------------- | ----------------- |
| 🐍 Python                  | Backend           |
| 🎯 Django                  | Web Framework     |
| 🔌 Django REST Framework   | API               |
| 🤖 Google Gemini           | AI Bug Analysis   |
| 🗄️ SQLite                 | Database          |
| 🌐 HTML / CSS / JavaScript | Frontend          |
| 🚀 Gunicorn                | Production Server |
| 📦 WhiteNoise              | Static Files      |
| 🔧 Git & GitHub            | Version Control   |
| ☁️ Render                  | Deployment        |

---

## 📂 Project Structure

```text
bugflow-ai/
│
├── backend/
│   ├── bugs/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── manage.py
│   ├── requirements.txt
│   └── db.sqlite3
│
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/codewithritikyadav/bugflow-ai.git
```

### 2. Navigate to the Project

```bash
cd bugflow-ai
cd backend
```

### 3. Create Virtual Environment

#### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the `backend` folder.

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
GEMINI_API_KEY=your_gemini_api_key
```

⚠️ **Never upload your `.env` file or API keys to GitHub.**

---

## 🗄️ Database Setup

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Create Admin Account

```bash
python manage.py createsuperuser
```

Enter your username, email, and password when prompted.

---

## ▶️ Run Locally

Start the development server:

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

---

## 🤖 Gemini AI

BugFlow AI uses **Google Gemini** to provide AI-powered bug analysis and debugging suggestions.

Add your Gemini API key to `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key
```

The API key should always be stored as an environment variable and should never be hard-coded into the source code.

---

## 🚀 Deployment

BugFlow AI can be deployed using **GitHub + Render**.

### Root Directory

```text
backend
```

### Build Command

```bash
pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
```

### Start Command

```bash
gunicorn config.wsgi:application
```

### Render Environment Variables

```text
SECRET_KEY=your_django_secret_key
DEBUG=False
ALLOWED_HOSTS=*
GEMINI_API_KEY=your_gemini_api_key
```

---

## 🧪 Django Checks

Check the project:

```bash
python manage.py check
```

Production security check:

```bash
python manage.py check --deploy
```

---

## 🐛 Example Bug

**Title:** Login fails with invalid credentials

**Description:**

When a user enters incorrect login credentials, the application should display a proper error message instead of returning a server error.

**Priority:** High

**Severity:** Major

**Status:** Open

BugFlow AI can analyze the bug and provide possible causes and debugging suggestions.

---

## 🔮 Future Improvements

* [ ] AI-powered bug classification
* [ ] Automatic severity prediction
* [ ] Duplicate bug detection
* [ ] GitHub Issues integration
* [ ] Email notifications
* [ ] Team collaboration
* [ ] Bug analytics dashboard
* [ ] Automated test generation
* [ ] Advanced AI debugging
* [ ] Production database support

---

## 👨‍💻 Author

### Ritik Yadav

**B.Tech CSE (AI & ML)**

Backend Developer | AI/ML Enthusiast

GitHub:
https://github.com/codewithritikyadav

---

## ⭐ Support

If you find **BugFlow AI** useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is developed for educational and project purposes.
