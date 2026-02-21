from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
]
next_id = 3

# GET all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET one user
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200

# CREATE user
@app.route('/api/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    new_user = {'id': next_id, 'name': data.get('name'), 'email': data.get('email')}
    users.append(new_user)
    next_id += 1
    return jsonify(new_user), 201

# UPDATE user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify(user), 200

# DELETE user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    original_len = len(users)
    users = [u for u in users if u['id'] != user_id]
    if len(users) == original_len:
        return jsonify({'error': 'User not found'}), 404
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
