from pytz import timezone
from . import db # importing from current pacakge which is website __init__ file
from flask_login import UserMixin #help us to log user in
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))#user.id is an primary key


class User(db.Model,UserMixin):#userMixin is just user specific
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)#no user have same email
    password = db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    notes=db.relationship('Note')#list of notes created by user.id but not exactly list just able to access it
    