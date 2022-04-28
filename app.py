from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Itemlist
from db import db
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #you can also use different SQL, not only sqlite
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False #turn off flask SQLAlchecmy modification tracker but not the SQLAlchemy modification tracker
api = Api(app)
app.secret_key = "macky"
jwt = JWT(app,authenticate,identity) #create endpoint name /auth

@app.before_first_request #this will create a table provided this is the first time table will be created
def create_table():
    db.create_all()

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    db.init_app(app)
    app.run(host='0.0.0.0', port='5000', debug='true')
