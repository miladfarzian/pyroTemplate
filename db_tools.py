import os
import pymongo
import json
from configs.config import *
from pykeyboard import InlineKeyboard , InlineButton
client = pymongo.MongoClient(mongo_string)
db = client['file_manager']
users_collection = db["users"]
settings = db['settings']





def save_users():
    print('[ * ] saving dabatabase users in json file')
    with open('users.json','w') as bot_users_file :
        cursor = users_collection.find()
        users = list(cursor)
        json.dump(users,bot_users_file,indent=2)
        print("[ ✓ ] database users saved in ->c users.json")
        

def delete_user(user_id):
    print("[ * ] Deleteing user {} from database ".format(user_id))
    users_collection.delete_one({"_id":user_id})
    print("[ ✓ ] User {} Deleted from database".format(user_id))

def read_users():
   if not os.path.exists("users.json") :
       save_users()
   with open('users.json','r') as bot_users_file :
       return json.load(bot_users_file)
   
   
def get_user(user_id):
    user_id = int(user_id)
    print("[ * ] gettings user {} data from databse".format(user_id))
    for user in read_users():
        if user['_id'] ==int(user_id):
            print(user)
            return user
        
    try:    
        user_data = {
                "_id":user_id,
            }
        users_collection.insert_one(user_data)  
        save_users()  
        return user_data
    except:
      pass
    
        
def add_user_to_db(user_id,inviter=0):
    if not get_user(user_id):
        print("[ * ] Adding User {} to database".format(user_id))
        user_data = {
            "_id":user_id,
        }
        users_collection.insert_one(user_data)
        print('[ ✓ ] User {} Added to database'.format(user_id))
        save_users()
        return 
    print("[ × ] user {} existed in db not added to dabatabse".format(user_id))
        

