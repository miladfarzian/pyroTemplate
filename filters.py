from pyrogram import filters
from configs.configs import admins , force_join_channel_id , sudo


#--------------{ admin filter }---------------- 
async def check_if_user_is_admin(_,__,m):
    try:
        user_id=m.from_user.id
        if user_id in admins:
            return True
    except:
        return False    
        
    
is_admin = filters.create(func=check_if_user_is_admin)    



#--------------{ user is memeber filter / forced join }---------------- 

async def check_id_user_joined_channel(_,client,message):
    user_id = message.from_user.id
    try:
        await client.get_chat_member(force_join_channel_id, user_id)
        if int(user_id) not in admins:
            return  True
    except:
        return False

  

async def not_member(_,client,message):
    user_id = message.from_user.id
    try:
        await client.get_chat_member(force_join_channel_id, user_id)
        
        return  False 
    except:
        if int(user_id) not in admins:
            return  True
        return True


#--------------{ sudo filter }---------------- 
    
async def check_if_user_is_sudo(_,client,message):
    user_id = message.from_user.id
    if user_id==sudo:
        return True

