# 🏗️ MCK Constructions ERP System

A role-based Construction ERP system developed using Django to manage business operations including workforce management, recruitment, financial tracking, and project lifecycle management.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- Role-based login system
- Secure session handling
- Roles: Admin, HR, Accounts, Project Management

---

### 👨‍💼 Admin Module
- Daily Attendance Tracking
- Weekly Expense Monitoring (drivers, logistics, housekeeping)
- Monthly Salary Management

---

### 🧑‍💻 HR Module
- 5-stage recruitment workflow:
  - First Round
  - Technical Round
  - Client Round
  - HR Round
  - Final Decision
- Candidate status tracking (Selected / Rejected / In Progress)
- Remarks & joining date handling

---

### 💰 Accounts Module
- Expense tracking (Material, Labour, Transport)
- Income tracking (Project / Client payments)
- Automatic Profit Calculation
- Financial dashboard overview

---

### 🏗️ Project Tracking Module
- Project creation & management
- Task-based tracking (Foundation, Plumbing, etc.)
- Task status updates (Pending / Ongoing / Completed)
- Automatic progress calculation (% based on completed tasks)

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** MySQL
- **Architecture:** MVT (Model-View-Template)

---

## 📊 System Architecture
ERP System
│
├── Admin → Operations Management
├── HR → Recruitment Workflow
├── Accounts → Financial Tracking
└── Project → Execution & Progress Tracking

---

## 🎯 Key Highlights

- Modular ERP design
- Real-world business logic implementation
- Role-based access control
- Scalable architecture using Django ORM
- Clean and responsive UI

---

## 📸 Screenshots (Optional)

_Add screenshots here if available_

---

## 🚀 Future Enhancements

- 📊 Charts & Analytics Dashboard
- 📄 Invoice Generation (PDF)
- 🔍 Search & Filter functionality
- 📱 Mobile optimization
- 🔗 API integration (Django REST Framework)

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/mck-constructions-erp.git
cd mck-constructions-erp

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

---

# 🚫 🔥 .gitignore (IMPORTANT)

Create file: `.gitignore`

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Django
db.sqlite3
*.log

# Environment
.env
venv/
env/

# VS Code / IDE
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

# Migrations (optional keep if needed)
# */migrations/*
# !*/migrations/__init__.py

# Static files (if collected)
staticfiles/

# Media uploads
media/

👨‍💻 Author

 - Karthik M
 - Python Full Stack Developer