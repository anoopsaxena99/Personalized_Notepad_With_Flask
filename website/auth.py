#standard routes where user want to go login page homepage
from xmlrpc.client import boolean
from flask import Blueprint ,render_template,request,flash
#defining blueprint of our website
auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])#1
def login():
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
        firstname=request.form.get('firstname')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        if len(email) < 4:
            flash('email must be grater than 4 characters.',category='error')
        elif len(firstname) < 2:
            flash('first name be grater than 2 characters.',category='error')
        elif password1 !=password2:
            flash('passwords don\'t match',category='error')
        elif len(password1) < 7 :
            flash('password must be atleast 7 characters.',category='error')
        else :
            flash('Account created!',category='success')
            pass
            #add user to database

    return render_template("sign_up.html")
