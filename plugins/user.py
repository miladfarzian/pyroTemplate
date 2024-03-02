from bot_filters import is_member , not_member
from pyrogram import Client , filters


@Client.on_message(is_member & filters.command(['start']))
async def handle_admin_messages(c,m):
    name =  m.from_user.first_name
    user_id = m.from_user.id
    user_name = f'hey sudo [{name}](tg://user?id={user_id}) !'
    await m.reply(user_name)
    
    
    


@Client.on_message(not_member)
async def handle_admin_messages(c,m):
    name =  m.from_user.first_name
    user_id = m.from_user.id
    user_name = f'hey dear user  [{name}](tg://user?id={user_id}) !\nyou havent joined our channel yet'
    await m.reply(user_name)
    
    
    


    