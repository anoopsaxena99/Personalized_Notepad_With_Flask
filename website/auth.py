#standard routes where user want to go login page homepage
from flask import Blueprint
#defining blueprint of our website
auth = Blueprint('auth',__name__)

@auth.route('/login')#1
def login():
    return "<p>Login</p>"

@auth.route('/logout')#2
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')#3
def sign_up():
    return "<p>sign up</p>"
