from werkzeug.security import safe_str_cmp #to properly compare string for password
#import hmac
#from hmac import compare_digest
from models.user import UserModel


#username_mapping = { u.username: u for u in Users} #this is a comprehension to search for username in users list
#userid_mapping = {u.id: u for u in users } #same with id

def authenticate(username,password):
    user = UserModel.find_by_username(username) #this will search for the "username" in the dictionary username_mapping. it will return None if no username
    #if user and safe_str_cmp(user.password, password): # users.password == password sometimes does not work well
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
