from flask import Flask, jsonify

app = Flask(__name__)

# 200 OK (default)
@app.route('/success')
def success():
    return "Success!", 200

# 400 Bad Request (client error)
@app.route('/bad')
def bad_request():
    return "Bad request!", 400

# 404 Not Found
@app.route('/notfound')
def not_found():
    return "Not found!", 404

# 500 Server Error
@app.route('/error')
def server_error():
    return "Server error!", 500

if __name__ == '__main__':
    print("Starting Flask app for status codes...")
    print("Try: http://localhost:5000/success, /bad, /notfound")
    app.run(debug=True)
