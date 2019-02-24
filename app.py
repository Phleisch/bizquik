from flask import Flask, render_template, request, url_for
import json
import sys
from Query import retrieve_results
from FieldParser import parse_fields

app = Flask(__name__)

# USER FUNCTIONS

# Handle action to create users
@app.route('/user', methods=["POST"])
def create_user():
    return

# Handle actions to read, update, and delete users
@app.route('/user/<string:username>', methods=["GET", "POST", "DELETE"])
def user_action(username):
    return

# Handle request to login a user
@app.route('/user/login', methods=["GET"])
def login_user:
    return

# Handle request to logout a user
@app.route('/user/logout', methods=["GET"])
def logout_user:
    return

# DATA FUNCTIONS

# Handle action to extract data from a business card picture
@app.route('/extract', methods=["POST"])
def extract_text:
    return 

if __name__ == '__main__':
    app.run()
