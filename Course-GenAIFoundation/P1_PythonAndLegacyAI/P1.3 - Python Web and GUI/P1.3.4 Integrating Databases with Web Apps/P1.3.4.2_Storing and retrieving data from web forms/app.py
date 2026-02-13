from flask import Flask, request, g, render_template, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
# Store the database inside the db folder
DB_FOLDER = os.path.join(os.path.dirname(__file__), 'db')
os.makedirs(DB_FOLDER, exist_ok=True)
DATABASE = os.path.join(DB_FOLDER, 'formdata.db')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.route('/', methods=['GET', 'POST'])
def form():
    db = get_db()
    db.execute('CREATE TABLE IF NOT EXISTS submissions (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        db.execute('INSERT INTO submissions (name, email) VALUES (?, ?)', (name, email))
        db.commit()
        return redirect(url_for('submissions'))
    return render_template('form.html')

@app.route('/submissions')
def submissions():
    db = get_db()
    submissions = db.execute('SELECT * FROM submissions').fetchall()
    return render_template('submissions.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
