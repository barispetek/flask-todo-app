import sqlite3

conn = sqlite3.connect('tasks.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL
)
''')

conn.commit()
conn.close()
