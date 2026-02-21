from flask import Flask, g, jsonify, request
import sqlite3
import os

app = Flask(__name__)
DB_FOLDER = os.path.join(os.path.dirname(__file__), 'db')
os.makedirs(DB_FOLDER, exist_ok=True)
DATABASE = os.path.join(DB_FOLDER, 'query.db')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

# Create a table with multiple columns (run at startup)
def setup_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                age INTEGER,
                city TEXT
            )
        ''')
        db.commit()
setup_db()

# Query users by different columns
@app.route('/users', methods=['GET'])
def get_users():
    db = get_db()
    query = 'SELECT * FROM users WHERE 1=1'
    params = []
    name = request.args.get('name')
    email = request.args.get('email')
    city = request.args.get('city')
    min_age = request.args.get('min_age')
    max_age = request.args.get('max_age')
    if name:
        query += ' AND name = ?'
        params.append(name)
    if email:
        query += ' AND email = ?'
        params.append(email)
    if city:
        query += ' AND city = ?'
        params.append(city)
    if min_age:
        query += ' AND age >= ?'
        params.append(int(min_age))
    if max_age:
        query += ' AND age <= ?'
        params.append(int(max_age))
    users = db.execute(query, params).fetchall()
    return jsonify([
        {'id': row[0], 'name': row[1], 'email': row[2], 'age': row[3], 'city': row[4]} for row in users
    ])

@app.route('/add_user', methods=['POST'])
def add_user():
    db = get_db()
    data = request.json
    db.execute('''
        INSERT INTO users (name, email, age, city) VALUES (?, ?, ?, ?)
    ''', (
        data.get('name', 'Bob'),
        data.get('email', 'bob@example.com'),
        data.get('age', 25),
        data.get('city', 'Unknown')
    ))
    db.commit()
    return 'User added!'

if __name__ == '__main__':
    app.run(debug=True)
