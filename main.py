from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return render_template('signup_form.html', title='Signup')

@app.route("/", methods=['GET', 'POST'])
def validate_form():
    username = request.form['username']
    username_error = ''
    password = request.form['password']
    password_error = ''
    verify = request.form['verify']
    verify_error = ''
    email = request.form['email']
    email_error = ''

    if len(username) == 0:
        username_error = 'Username cannot be blank!'
    elif ' ' in username:
        username_error = 'Username cannot contain space!'
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Username must be between 3 and 20 characters!'

    if len(password) == 0:
        password_error = 'Password cannot be blank!'
    elif ' ' in password:
        password_error = 'Password cannot contain space!'
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Password must be betweeen 3 and 20 characters!'

    if verify != password:
        verify_error = 'Passwords do not match!'

    if len(email) == 0:
        email_error = ''
    elif email.count('.') != 1 or email.count('@') != 1:
        email_error = 'Invalid email format!'
    elif ' ' in email:
        email_error = 'Email address cannot space!'
    elif len(email) < 3 or len(email) > 20:
        email_error = 'Email length must be between 3 and 20 characters!'

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', title='Welcome!', username=username)
    else:
        return render_template('signup_form.html', title='Signup', username=username, username_error=username_error, password='', password_error=password_error, verify='', verify_error=verify_error, email=email, email_error=email_error) 

app.run()



