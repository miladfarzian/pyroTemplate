import os
import json
from configs.config import *
from pysondb import db
from pykeyboard import InlineKeyboard , InlineButton
from log_handler import error_logger , info_file_handler

users = db.getDb("db_file/users.json")
def add_user(user_id,lang):
    user_model = {
        "user_id" : user_id,
        "wallet" : 0,
        "lan" : lang
    }
    
    
    
    if users.getByQuery({"user_id":user_id})!=[]:
        users.add(
            user_model
        )
        
        info_file_handler.info(f"user with id [{user_id}] added to db")



