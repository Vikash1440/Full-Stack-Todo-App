# FullStackTodo Django Project

## Project Description
FullStackTodo is a simple Django-based ToDo List web application that allows users to manage tasks, mark them as completed or undone, edit and delete tasks through a clean Bootstrap-powered user interface.

## Project Structure

```
FullStackTodo/
│
├── FullStackTodo/                    # Main Django project module
│   ├── __init__.py                  
│   ├── settings.py                  # Project settings and configurations
│   ├── urls.py                     # URL routing for project-level paths
│   ├── views.py                    # Home view displaying tasks
│   ├── wsgi.py                    
│   └── asgi.py                    
│
├── todo/                           # Django app managing ToDo tasks
│   ├── __init__.py                
│   ├── admin.py                   # Admin registration for Task model
│   ├── apps.py                   
│   ├── models.py                 # Task model definition
│   ├── urls.py                  # App-specific URL routing for task views
│   ├── views.py                 # Task CRUD operations and business logic
│   └── migrations/              # Database migration files
│
├── templates/                    # Project level templates
│   ├── home.html                # Main task listing and management UI
│   └── edit_task.html           # Edit task UI form
│
├── db.sqlite3                   # SQLite database for development
├── manage.py                   # Django command-line utility
└── README.md                   # This file

## Key Files and Their Purpose
- `FullStackTodo/settings.py`: Django project configuration including database, installed apps, and templates.
- `FullStackTodo/urls.py`: Routes root URL to home view and includes app-specific routes.
- `FullStackTodo/views.py`: Contains home view rendering incomplete and completed tasks.
- `todo/models.py`: Defines the Task model with fields for task description, status, and timestamps.
- `todo/views.py`: Implements task creation, editing, deletion, and marking as done/undone.
- `todo/urls.py`: Routes task-related URLs to corresponding views.
- `todo/admin.py`: Registers Task model with Django admin panel.
- `templates/`: HTML templates powered with Bootstrap and FontAwesome for frontend UI.
- `manage.py`: CLI utility to interact with the project.

## Deployment Instructions

### 1. Environment Setup
- Install Python 3.8+ (preferably use a virtual environment)
- Install Django (`pip install django`)

### 2. Clone and Setup Project
- Clone the repository and navigate into `FullStackTodo` directory.

### 3. Database Migration
- Run migrations to create database tables:
  ```
  python manage.py migrate
  ```

### 4. Running the Development Server
- Start the Django development server:
  ```
  python manage.py runserver
  ```
- Visit `http://localhost:8000/` in your browser to access the ToDo app.

### 5. Accessing Admin Panel (Optional)
- Create admin user:
  ```
  python manage.py createsuperuser
  ```
- Access admin at `http://localhost:8000/admin/`

### 6. Notes for Production Deployment
- Set `DEBUG = False` in `settings.py`
- Configure `ALLOWED_HOSTS` with allowed domain names or IP addresses.
- Use a more robust database like PostgreSQL.
- Set up static files serving (collectstatic).
- Use a production-ready web server (e.g. Gunicorn, Nginx).

## Usage Overview
- Add tasks via the input form on the home page.
- Mark tasks done or undone.
- Edit existing tasks.
- Delete tasks as needed.
- Completed and incomplete tasks are displayed separately.

---

This README should help you understand the FullStackTodo project structure, purpose of files, and how to deploy and run the app.
