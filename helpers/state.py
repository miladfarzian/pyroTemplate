from pysondb import db
from pyrogram.types import Message

class StateManager:
    def __init__(self, db_path):
        self.db = db.getDb(db_path)

    async def set(self, step: str, message: Message):
        user_id = message.from_user.id
        user = self.db.getByQuery({"user_id": user_id})
        if user!=[]:
            self.db.updateById(user[0].get("id"), {"next": step})
        else:
            self.db.add({"user_id": user_id, "next": step})

    async def get(self, message: Message) -> str:
        user_id = message.from_user.id
        user = self.db.getByQuery({"user_id": user_id})
        if user!=[]:
            next_step = user[0].get("next")
            return next_step
        else:
            self.db.add({"user_id": user_id, "next": ""})
            return ""

   
    
   



    async def reset(self, message: Message) -> None:
        if self.db.getByQuery({"user_id":message.from_user.id})==[]:
            return
        user_id = message.from_user.id
        user = self.db.getByQuery({"user_id": user_id})[0]
        if user:
          self.db.deleteById(user.get('id'))
            


    async def delete(self,message:Message)->None:
        try:
            user_id = message.from_user.id
            user = self.db.getByQuery({"user_id": user_id})[0]
            if user:
                self.db.deleteById(user.get("id")
                                   )
        except:
            pass        


    

    
   






            



state_manager = StateManager('helpers/DB-FILES/state.json')            
