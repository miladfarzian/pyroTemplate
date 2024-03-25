import yaml
from db_tools import *
with open("configs/config.yml",'r') as file :
    data = yaml.safe_load(file)

api_id = data['API_ID']
api_hash = data['API_HASH']
bot_token =  data['BOT_TOKEN']
session_string =  data['SESSION_STRING']
admins = data['ADMINS']
mongo_string = data['MONGO_STRING']
force_join_channel_id = ''
sudo = '00'
