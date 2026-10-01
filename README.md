# Django Resume Builder

A professional **Django-based Resume Builder** that allows users to create, edit, and preview structured resumes with sections such as professional summary, education, technical skills, projects, experience, and achievements.

The application provides a clean resume-building workflow and professionally designed resume preview templates suitable for students, freshers, and job seekers.

---

## 🚀 Features

* Create a professional resume
* Edit existing resumes
* Live resume preview
* Single-page professional resume layout
* Professional Summary section
* Education details
* Technical Skills
* Projects
* Work Experience
* Achievements
* LinkedIn, GitHub, and Portfolio links
* Responsive resume preview
* Print-friendly resume design
* Multiple professional resume templates
* Django form validation
* Django model-based data management
* SQLite database support
* Modular Django application structure

---

## 🖥️ Application Workflow

```text
Home Page
    ↓
Create Resume
    ↓
Enter Personal Details
    ↓
Add Education
    ↓
Add Technical Skills
    ↓
Add Projects
    ↓
Add Experience
    ↓
Add Achievements
    ↓
Save Resume
    ↓
Resume Preview
    ↓
Edit Resume / Print Resume
```

---

## 🛠️ Technologies Used

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* Django Templates

### Database

* SQLite

### Development Tools

* Visual Studio Code
* Git
* GitHub
* Python Virtual Environment

---

## 📂 Project Structure

```text
Django-Resume-Builder/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── resume/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_experience_institute_alter_achievement_id_and_more.py
│   │   ├── 0003_resume_template_alter_achievement_id_and_more.py
│   │   └── __init__.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   └── resume/
│       ├── create_resume.html
│       ├── home.html
│       ├── modern_preview.html
│       ├── professional_classic.html
│       ├── professional_executive.html
│       ├── professional_minimal.html
│       ├── professional_modern.html
│       ├── resume_preview.html
│       └── success.html
│
├── manage.py
├── .gitignore
└── README.md
```

---

## 📋 Resume Sections

The Resume Builder supports the following information:

### Personal Information

* Full Name
* Professional Title
* Email
* Phone
* Location
* LinkedIn
* GitHub
* Portfolio

### Professional Summary

Users can add a short professional summary describing their skills, experience, career interests, and professional goals.

### Education

Education records can include:

* Degree
* Institution
* Location
* Start Year
* End Year
* Description

### Technical Skills

Skills can be added individually with optional categories.

Examples:

```text
Programming Languages
Python
Java
C
SQL

Web Technologies
HTML
CSS
JavaScript
```

### Projects

Each project can contain:

* Project Title
* Technologies Used
* Project Description
* Project Link

### Experience

Experience records support:

* Company
* Position
* Start Date
* End Date
* Description

### Achievements

Users can add achievements, certifications, internships, awards, or other professional accomplishments.

---

## 🎨 Resume Templates

The project contains multiple professional resume template files:

```text
professional_classic.html
professional_executive.html
professional_minimal.html
professional_modern.html
modern_preview.html
resume_preview.html
```

The templates are designed to provide clean and professional resume layouts.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shwetadeshpande27/Django-Resume-Builder.git
```

Move into the project directory:

```bash
cd Django-Resume-Builder
```

---

### 2. Create a Virtual Environment

On Windows:

```cmd
python -m venv venv
```

Activate the virtual environment:

```cmd
venv\Scripts\activate
```

You should see:

```text
(venv)
```

before your terminal path.

---

### 3. Install Django

Install Django:

```cmd
pip install django
```

If a `requirements.txt` file is available in the project, install the dependencies using:

```cmd
pip install -r requirements.txt
```

---

### 4. Apply Database Migrations

Run:

```cmd
python manage.py migrate
```

---

### 5. Start the Development Server

Run:

```cmd
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

---

## 🌐 Application URLs

### Home

```text
http://127.0.0.1:8000/resume/
```

### Create Resume

```text
http://127.0.0.1:8000/resume/create/
```

### Edit Resume

Example:

```text
http://127.0.0.1:8000/resume/edit/8/
```

### Resume Preview

Example:

```text
http://127.0.0.1:8000/resume/preview/8/
```

### Django Admin

```text
http://127.0.0.1:8000/admin/
```

---

## 🗄️ Database

The current project uses **SQLite** for development.

The database file is:

```text
db.sqlite3
```

The database is intentionally excluded from GitHub through `.gitignore`.

When setting up the project on another computer, run:

```cmd
python manage.py
```
