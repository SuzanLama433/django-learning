# Django Learning Project

A beginner-friendly Django project created for learning and understanding the fundamentals of Django web framework.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Project Setup](#project-setup)
- [Project Structure](#project-structure)
- [Running the Project](#running-the-project)
- [Creating Your First App](#creating-your-first-app)
- [Pushing to GitHub](#pushing-to-github)

---

## 🎯 Project Overview

This is an educational Django project designed to help beginners understand:
- Django project and app structure
- URL routing and views
- Template rendering
- Static files management
- Database migrations

---

## ✅ Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Git

---

## 🚀 Project Setup

### Step 1: Create Project & App

1. **Open Terminal** in VS Code (`Ctrl + `` `)

2. **Create a new Django project:**
   ```bash
   django-admin startproject project_name
   cd project_name
   ```

3. **Create a new Django app:**
   ```bash
   python manage.py startapp app_name
   ```

4. **Register the app** in `project_name/settings.py`:
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'app_name',  # Add your app here
   ]
   ```

### Step 2: Database Migration

```bash
# Apply migrations to create database tables
python manage.py migrate

# Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the project running.

---

## 📁 Project Structure

```
django_project/
│
├── app_name/                    # Your Django app
│   ├── migrations/
│   ├── templates/
│   │   └── home.html           # HTML templates
│   ├── static/
│   │   ├── css/                # CSS files
│   │   ├── js/                 # JavaScript files
│   │   └── images/             # Image assets
│   ├── views.py                # View functions
│   ├── urls.py                 # App-level URL routing
│   ├── models.py               # Database models
│   ├── admin.py                # Admin configuration
│   └── apps.py
│
├── project_name/               # Project configuration
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL routing
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py                   # Django management script
├── db.sqlite3                  # Database file (SQLite)
└── README.md                   # This file
```

---

## 💻 Creating Views & URLs

### views.py

Create a simple view function:

```python
# app_name/views.py
from django.shortcuts import render

def home(request):
    """Display the home page"""
    return render(request, 'home.html')
```

### urls.py

Configure URL routing:

```python
# app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Then include app URLs in main project:

```python
# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_name.urls')),
]
```

---

## 🎮 Running the Project

```bash
# Start the development server
python manage.py runserver

# Access the application
# Open browser and go to: http://127.0.0.1:8000/
```

---

## 📤 Pushing to GitHub

### Step 1: Initialize Git Repository

```bash
git init
```

### Step 2: Create .gitignore

Create a `.gitignore` file in your project root:

```
# Django
*.pyc
__pycache__/
*.py[cod]
*$py.class
*.so
db.sqlite3
*.log
*.pot
venv/
env/
.DS_Store
.vscode/
.env
```

### Step 3: Add & Commit Files

```bash
git add .
git commit -m "Initial Django project setup"
```

### Step 4: Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click **New Repository**
3. Name it (e.g., `django-learning-project`)
4. Click **Create Repository**

### Step 5: Push to GitHub

```bash
# Add remote repository
git remote add origin https://github.com/your-username/django-learning-project.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## 📚 Learning Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django for Beginners](https://djangoforbeginners.com/)
- [MDN Web Docs - Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

---

## 📝 Notes

- This is a **learning project** for educational purposes
- Always use virtual environment for Django projects
- Keep `SECRET_KEY` and sensitive data in `.env` file
- Test your code frequently during development

---

## 👨‍💻 Author

Created for Django learning purposes

---

**Happy Learning! 🎓**