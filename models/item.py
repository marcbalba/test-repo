
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2)) #precision 2 is limit the decimal to 2
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name,price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self): #return json representation = dictionary
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
        #query is part of the db.Model SQLAlchemy where you can query like SELECT * from
        #filter_by is to filter using argument name
        #first() is to choose the first row filtered and limit to 1 only


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
