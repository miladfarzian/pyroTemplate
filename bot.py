

##########Import##########

from pyrogram import Client
from configs.config import *
from time import time

##########Client##########

#________CLI__________________
Cli = Client(
  name = "Cli",
  api_id = api_id,
  api_hash = api_hash,
  app_version = "1.0.0",
  device_model = "Postchi",
  session_string = session_string,
  plugins = {"root": "cli_plugins"},
  workers = 1
)

# _______ API ______________
class Api(Client):
  def __init__(self):
    super().__init__(
      name = "Api",
      api_id = api_id,
      api_hash = api_hash,
      app_version = "1.0.0",
      device_model = "Postchi",
      bot_token = bot_token,
      plugins = {"root": "api_plugins"},
      workers = 20
    )

  async def start(self):
    await super().start()
    print("Bots are started!")

  async def stop(self, *args):
    await super().stop()
    print("Bots are stopped!")
    
    
    

    