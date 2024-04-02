from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import os
app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'mr.robott52@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')  # Access environment variable

mail = Mail(app)

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

    # Send email notification
    send_email_notification(name, email, message)

    return jsonify({'message': 'Form submitted successfully'}), 200

def is_valid_email(email):
    # Simple email validation using string methods
    return '@' in email and '.' in email.split('@')[-1]

def send_email_notification(name, email, message):
    # Create message object
    msg = Message('New Form Submission', 
                  sender='mr.robott52@gmail.com', 
                  recipients=['mr.robott52@gmail.com'])
    
    # Email body
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    
    # Send the email
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
