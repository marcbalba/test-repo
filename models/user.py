import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'#define the table of the database
    id = db.Column(db.Integer, primary_key=True) #tell the columns
    username = db.Column(db.String(80)) #limit the size to 80 strings
    password = db.Column(db.String(80))
    #these 3 properties will match on the self.id / self.username / self.password below

    def __init__(self,username,password): #_id is not needed to be an argument because id is automatically increment
        #self.id = _id # "id" is python special variable so use _id to make it different or use other variable
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
