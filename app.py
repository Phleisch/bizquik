from flask import Flask, render_template, request
import sys
import json
from user_dao import User, user_is_unique
from base import Base, engine, Session

app = Flask(__name__)

# Create mapping from python classes to database tables
Base.metadata.create_all(engine)
session = Session()

def db_test():
    print (User.__table__, sys.stderr)
    users = session.query(User)
    for user in users:
        print (user)

# Error Functions / Handling

def page_not_found():
    return "Stop going to places you're not supposed to be in"

def bad_method():
    return "That's not what that endpoint is supposed to do"

def default_error():
    return "What the heck did you do?"

# List of error functions mapped to the error code they handle

error_functions = {404: page_not_found, 405: bad_method}

# Handle exception of page not being found
@app.errorhandler(Exception)
def handle_error(error):
    error_code = error.code
    print(error, sys.stderr)
    for code in error_functions:
        if code == error_code:
            return error_functions[code]()

    return default_error()

# Miscellaneous

# Username uniqueness database test
@app.route('/unique', methods=["GET", "POST"])
def get_unique():
    if request.method == 'GET':
        return render_template('unique.html')

    elif request.method == 'POST':
        unique = user_is_unique(request.form['username'].lower(), session)
        if unique:
            return "Unique username!"
        return "Not a unique username..."

    return "Error"

# Home page
@app.route('/', methods=["GET"])
def get_home():
    return render_template('index.html')

# USER FUNCTIONS

# Handle action to create users
@app.route('/user', methods=["POST"])
def create_user():
    return "CREATE_USER"

# Handle actions to read, update, and delete users
@app.route('/user/<string:username>', methods=["GET", "POST", "DELETE"])
def user_action(username):
    print(request)

    if request.method == 'GET':
        return "GET user_action"
    elif request.method == 'POST':
        return "POST user_action"
    elif request.method == 'DELETE':
        return "DELETE user_action"

    # We should not have gotten here
    raise ValueError()

# Handle request to login a user
@app.route('/user/login', methods=["GET"])
def login_user():
    return "GET login_user"

# Handle request to logout a user
@app.route('/user/logout', methods=["GET"])
def logout_user():
    return "GET logout_user"

# DATA FUNCTIONS

# Handle action to extract data from a business card picture
@app.route('/extract', methods=["POST"])
def extract_text():
    return "POST extract_text"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
