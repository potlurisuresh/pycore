from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route - homepage
@app.route('/')
def home():
    return "Welcome to Flask! This is the home page."

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
