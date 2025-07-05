# 📝 Flask ToDo App with User Authentication

A full-featured ToDo web application built using Python and Flask.  
Users can register, log in, add tasks, delete them, and manage their personal to-do list securely.

---

## 🚀 Features

- ✅ User registration & login system (Flask-Login)
- ✅ Password hashing with Werkzeug (secure storage)
- ✅ Add tasks (only visible to logged-in user)
- ✅ Delete tasks
- ✅ Logout functionality
- ✅ Persistent task storage with SQLite
- ✅ Mobile-friendly UI with Bootstrap 5

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **Flask-Login**
- **SQLite**
- **HTML / Bootstrap 5**

---

## 💻 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/barispetek/flask-todo-app.git
cd flask-todo-app

# (Optional) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Initialize the database
python init_db.py

# Run the application
python app.py
