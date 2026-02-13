from flask import Flask, render_template, request

app = Flask(__name__)

# Display form (GET) and process form (POST)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('acknowledge.html', name=name, email=email, message=message)
    return render_template('contact_form.html')


if __name__ == '__main__':
    print("Flask app is running...")    
    print("You can access the contact form at http://localhost:5000/contact and the search page at http://localhost:5000/search?q=your+query")
    app.run(debug=True)