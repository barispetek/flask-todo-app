# 📝 Flask ToDo App with SQLite

This is a simple yet functional ToDo web application built using Python and Flask.  
It allows users to add and delete tasks, with all data stored in a local SQLite database.

---

## 🚀 Features

- Add new tasks
- Delete existing tasks
- Tasks are saved permanently using SQLite
- Mobile-friendly and responsive design using Bootstrap 5

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **SQLite**
- **HTML / Bootstrap 5**

---


## 💻 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/yourusername/todo-flask-app.git
cd todo-flask-app

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # For Windows
# source venv/bin/activate  # For Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Initialize the database
python init_db.py

# Run the app
python app.py
