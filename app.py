from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key_here"

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id_, username, password):
        self.id = id_
        self.username = username
        self.password = password

# User loader for session management
@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT id, username, password FROM users WHERE id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return User(*row)
    return None

# Connect to database helper
def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home (task list)
@app.route("/", methods=["GET", "POST"])
@login_required
def home():
    conn = get_db_connection()

    if request.method == "POST":
        task = request.form.get("task")
        if task:
            conn.execute("INSERT INTO tasks (content, user_id) VALUES (?, ?)", (task, current_user.id))
            conn.commit()

    tasks = conn.execute("SELECT * FROM tasks WHERE user_id = ?", (current_user.id,)).fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

# Delete task
@app.route("/delete/<int:id>")
@login_required
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", (id, current_user.id))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            flash("Registration successful. You can now log in.")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username already exists. Try a different one.")
        finally:
            conn.close()
    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            user_obj = User(user["id"], user["username"], user["password"])
            login_user(user_obj)
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password.")

    return render_template("login.html")

# Logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
