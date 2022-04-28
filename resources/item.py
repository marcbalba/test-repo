from flask_restful import Resource,reqparse,request
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3

class Item(Resource):

    #to validate price is present and have the correct data type
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = "This field cannot be emtpy"
    )
    parser.add_argument('store_id',
        type = int,
        required = True,
        help = "Item needs a store ID"
    )

    @jwt_required()
    def get(self, name):
        return {'message': [x.json() for x in ItemModel.query.all()]}, 404
        #or you can use lambda
        #return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}

    def post(self, name):
        if ItemModel.find_by_name(name): #this will call the classmethod to search item in the database
            return {'message': "Item '{}' already exist".format(name)}, 400

        data = Item.parser.parse_args()
        #data = request.get_json()
        item = ItemModel(name, **data) # or item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {'message': 'Error occured inserting item.'}, 500 #internal server error

        return item.json(), 201

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}

    #put can either update or create items
    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None: #if name is not in the list, it will create a new item
            try:
                item = ItemModel(name, data['price'],data['store_id'])
            except:
                return {'message': 'Error occured inserting item'}, 500
        else:
            try:
                item.price = data['price']
            except:
                return {'message': 'Error occured updating item'}, 500
            #item.update(data) #if item is found, it will update the item
        item.save_to_db()
        return item.json()


class Itemlist(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'store_id': row[0], 'name': row[1], 'price': row[2]})
        connection.close()
        return {'items': items}
