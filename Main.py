from aiogram import types,Dispatcher,Bot
from dotenv import load_dotenv
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pprint import pprint
import asyncio
from aiogram.dispatcher.handler import CancelHandler
import sys
from src.MIDDLEWARES import Throt
sys.path.append("C:\Bot_TEDDY\src")
import HANDLERS



FSM_STORAGE=MemoryStorage()


load_dotenv(".env") #The load from .env tokenp
bot=Bot(token=os.getenv("api"))
dp=Dispatcher(bot,storage=MemoryStorage())

async def register_handlers(dp: Dispatcher)->None:
    for item in HANDLERS.list_handlers:
        await item(dp=dp)
        
async def main()->None:
    await register_handlers(dp)
    try:
        pprint("BOT IS SUCCESS STARTED!!!")
        await dp.start_polling()
    except Exception as _ex:
        pprint(f"{_ex}")
        return -1
    
if __name__=="__main__":
    dp.middleware.setup(Throt())
    asyncio.run(main())
