from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

# Handle 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return """
    Page not found! (404)
    The page you are looking for does not exist.
    """

# Handle 500 - Server Error
@app.errorhandler(500)
def server_error(error):
    return """
    Server error! (500)
    Something went wrong on our end.
    """


if __name__ == '__main__':
    print("Starting Flask app with error handlers...")
    print("Open http://localhost:5000 in your browser")
    print("Try visiting a non-existent URL like: http://localhost:5000/invalid")
    app.run(debug=True)
