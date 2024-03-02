from bot_filters import is_admin
from pyrogram import Client , filters

@Client.on_message(is_admin & filters.command(['start']))
async def handle_admin_messages(c,m):
    name =  m.from_user.first_name
    user_id = m.from_user.id
    user_name = f'[{name}](tg://user?id={user_id})'
    await m.reply('hey dear admin {} !'.format(user_name))
    
    