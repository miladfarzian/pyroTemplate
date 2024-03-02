from bot_filters import is_sudo
from pyrogram import Client , filters


@Client.on_message(is_sudo & filters.command(['start']))
async def handle_admin_messages(c,m):
    name =  m.from_user.first_name
    user_id = m.from_user.id
    user_name = f'hey sudo [{name}](tg://user?id={user_id}) !'
    await m.reply(user_name)
    
    