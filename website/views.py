#adding roots to our website
#standard routes where user want to go login page homepage
from flask import Blueprint #1
from flask import render_template
#defining blueprint of our website
views = Blueprint('views',__name__)#2

@views.route('/') #3 / for homepage
def home():#4
    return render_template("home.html")
    #5 in return it is returning html page
    #can also write return "<h1>Test</h1>"