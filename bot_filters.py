from pyrogram import filters
from configs.config import admins , force_join_channel_id
from pyrogram.errors import UserNotParticipant

#--------------{ admin filter }---------------- 
async def check_if_user_is_admin(_,__,m):
    return m.from_user.id in admins
        



#--------------{ user is memeber filter / forced join }---------------- 

async def check_user_not_in_chat(_,client: Client, message: Message):
    try:
        user_id = message.from_user.id
        member = await client.get_chat_member(force_join_channel_id, user_id)
        return False
    except UserNotParticipant:
        print("user is not a memeber of the chat !")
        return True

  
async def check_user_in_chat(_,client: Client, message: Message):
    try:
        user_id = message.from_user.id
        member = await client.get_chat_member(force_join_channel_id, user_id)
        return True
    except UserNotParticipant:
        return False





#list filters 
    
is_admin = filters.create(func=check_if_user_is_admin)    
is_member = filters.create(func=check_user_in_chat)    
not_member = filters.create(func=check_user_not_in_chat)    

