#make website folder as python package
#need to install flask,flask-login,flask-sqlalchemy
from flask import Flask#1

def create_app():
    app=Flask(__name__)#2 initializing flask
    app.config['SECRET_KEY']='hello'#3 encrypt our website

    #importing blueprints
    from .views import views#5 
    from .auth import auth#6

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app#4