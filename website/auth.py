#standard routes where user want to go login page homepage
from xmlrpc.client import boolean
from flask import Blueprint ,render_template,request,flash ,redirect,url_for
#defining blueprint of our website

from .models import User #for importing user
from werkzeug.security import generate_password_hash , check_password_hash #encrypt password

from . import db
auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])#1
def login():
    if request.method == 'POST' :
        email = request.form.get('email')
        password = request.form.get('password')

        user=User.query.filter_by(email=email).first()
        if user :
            if check_password_hash(user.password,password):
                flash('Login Successfully!!',category='success')
            else :
                flash("Incorrect password , try again",category='error')
        else :
            flash('Email does not exist.' , category='error')            
    data=request.form
    print(data)
    return render_template("login.html", boolean=False)

@auth.route('/logout')#2
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up' ,methods=['GET','POST'])#3
def sign_up():
    if request.method == 'POST':
        email=request.form.get('email')
        first_name=request.form.get('firstname')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        user=User.query.filter_by(email=email).first()

        if user :
            flash('Email already exists',category='Error')
        elif len(email) < 4:
            flash('email must be grater than 4 characters.',category='error')
        elif len(first_name) < 2:
            flash('first name be grater than 2 characters.',category='error')
        elif password1 !=password2:
            flash('passwords don\'t match',category='error')
        elif len(password1) < 7 :
            flash('password must be atleast 7 characters.',category='error')
        else :
            new_user=User(email=email,first_name=first_name,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!',category='success')
            return redirect(url_for('views.home'))
            #add user to database

    return render_template("sign_up.html")
