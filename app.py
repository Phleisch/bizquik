from flask import Flask, render_template, request
import sys

app = Flask(__name__)

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

    for code in error_functions:
        if code == error_code:
            return error_functions[code]()

    return default_error()

# Miscellaneous

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
    app.run()
