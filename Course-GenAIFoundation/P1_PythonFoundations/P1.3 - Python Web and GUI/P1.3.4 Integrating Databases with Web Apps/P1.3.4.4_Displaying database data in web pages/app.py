from flask import Flask, g, render_template
import sqlite3
import os

app = Flask(__name__)
DB_FOLDER = os.path.join(os.path.dirname(__file__), 'db')
os.makedirs(DB_FOLDER, exist_ok=True)
DATABASE = os.path.join(DB_FOLDER, 'example.db')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.route('/show_users')
def show_users():
    db = get_db()
    db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    users = db.execute('SELECT * FROM users').fetchall()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
