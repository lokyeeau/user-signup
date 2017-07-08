from flask import Flask, request, redirect,render_template
import cgi
import os

# template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['POST'])
def validate():
    error = False
    name = request.form['username']
    password = request.form['password']
    password_ver = request.form['password_ver']
    email = request.form['email']

    name_error = ''    
    password_error = ''
    password_ver_error = ''
    email_error = ''

    if len(name) < 3 or len(name) > 20:
        name_error = "Your username must be between 3-20 characters"
        error = True

    if " " in name:
        name_error = "Your username cannot contain any spaces"
        error = True

    if error:
        return render_template('signup.html', error=error, name_error = name_error)
    
    if len(password) < 3 or len(password) > 20:
        password_error = "Your password must be between 3-20 characters"
        error = True

    if password != password_ver:
        password_ver_error = "Passwords do not match"
        error = True

    if " " in password:
        password_error = "Password cannot contain any spaces"
        error = True

    if password_error or password_ver_error:
        error = True
        return render_template('signup.html', error = error, password_error=password_error, password_ver_error = password_ver_error, username=name)
    
    if len(email) > 0:
        if "@" not in email and "." not in email:
            email_error = "Invalid email address"
            error = True
            return render_template('signup.html', error=error, email_error = email_error, username=name)

    if len(email) > 20:
        email_error = "Invalid email address"
        error = True
        return render_template('signup.html', error=error, email_error=email_error, username=name)
    
    if " " in email:
        email_error = "Invalid email address"
        error = True
        return render_template('signup.html', error=error, email_error=email_error, username=name)

    return render_template('signup_confirm.html', username=name)

# @app.route('/welcome', methods=['GET', 'POST'])
# def welcome():
#     username = request.form['username']
#     return render_template('signup_confirm.html', username=username)

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('signup.html')

app.run()