#make website folder as python package
#need to install flask,flask-login,flask-sqlalchemy
from flask import Flask#1
from flask_sqlalchemy import SQLAlchemy#for database
from os import path

db = SQLAlchemy()#database object
DB_NAME = "database.db"#db name

def create_app():
    app=Flask(__name__)#2 initializing flask
    app.config['SECRET_KEY']='hello'#3 config variable for encrypt our website
    app.config['SQLALCHMEY_DATABASE_URI']=f'sqlite:///{DB_NAME}'#where the database is located at f'sqlite:///{DB_NAME}'
    db.init_app(app)#initialize the app


    #make Website as package
    #importing blueprints
    from .views import views#5 
    from .auth import auth#6
    #registering blueprint
    # . for relative import
    app.register_blueprint(views,url_prefix='/')#7
    app.register_blueprint(auth,url_prefix='/')#8
    #url prefix decides what u need to put before your registered blue print url
    
    from .models import User,Note#importing database schema

    create_database(app)
    return app#4

#
def create_database(app):
    if not path.exists('website/'+DB_NAME):#website is an folder name
        db.create_all(app=app)#created database
        print('Created Database!')

    