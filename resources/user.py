from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    #for registering user
    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str, required=True,help="This is required")
    parser.add_argument('password',type=str, required=True,help="This is required")


    def post(self):
        data = UserRegister.parser.parse_args()
        #to prevent duplicate username
        if UserModel.find_by_username(data['username']): #it means if User.find_by_username is NOT equal to None, then the username already EXISTS
            return {'message': 'Username already exist'}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'User created successfully'}, 201
