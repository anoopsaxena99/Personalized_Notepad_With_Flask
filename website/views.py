#standard routes where user want to go login page homepage
from flask import Blueprint ,render_template
#defining blueprint of our website
views = Blueprint('views',__name__)

@views.route('/') # / for homepage
def home():
    return render_template("home.html")