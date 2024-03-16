from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Check if name, email, and message are provided
    if not name or not email or not message:
        return jsonify({'error': 'Name, email, and message are required'}), 400

    # Check email format
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format'}), 400

    # Further validation and processing...

    return jsonify({'message': 'Form submitted successfully'}), 200

def is_valid_email(email):
    # Simple email validation using string methods
    return '@' in email and '.' in email.split('@')[-1]

if __name__ == '__main__':
    app.run(debug=True)
