#standard routes where user want to go login page homepage
from flask import Blueprint
#defining blueprint of our website
auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>sign up</p>"
