from pyrogram import Client , filters
from pyrogram.types import CallbackQuery
from pykeyboard import InlineKeyboard , InlineButton

@Client.on_callback_query()
async def handle_button(c:Client,q:CallbackQuery):
    """
    handles comming cq from user
    """
    
    call = q.data
    print(call)
