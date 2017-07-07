from flask import Flask, request, redirect,render_template
import cgi
import os

# template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['POST'])
def validate_name():
    name = request.form['username']

    name_error = ''

    if len(name) < 3 or len(name) > 20:
        name_error = "Your username must be between 3-20 characters"
        name = ''

    for char in name:
        if char == " ":
            name_error = "Your username cannot contain any spaces"
            name = ''

    if name_error:
        return render_template('signup.html', name_error = name_error)

    if not name_error:
        return render_template('signup_confirm.html', username=name)


def validate_password():
    password = request.form['password']
    password_ver = request.form['password_ver']

    password_error = ''
    password_ver_error = ''

    if len(password) < 3 or len(password) > 20:
        password_error = "Your password must be between 3-20 characters"

    if password != password_ver:
        password_ver_error = "Passwords do not match"

    for char in password:
        if char == " ":
            password_error = "Password cannot contain any spaces"

    if password_error or password_ver_error:
        return render_template('signup.html', password_error=password_error, password_ver_error = password_ver_error)

def validate_email():
    email = request.form['email']

    email_error = ''

    def is_email(email):
        for char in email:
            if char == "@":
                if char == ".":
                    return True
            else:
                return False

    if len(email) < 3 or len(email) > 20:
        email_error = "Invalid email address"
        email = ''

    for char in email:
        if char == ' ':
            email_error = "Invalid email address"
            email = ''

    if not is_email(email):
        email_error = "Invalid email address"
        email = ''

    if email_error:
        return render_template('signup.html', email_error=email_error)

@app.route('/welcome', methods=['POST','GET'])
def welcome():
    username = request.args.get('username')
    return render_template('signup_confirm.html', username=username)

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('signup.html')

app.run()