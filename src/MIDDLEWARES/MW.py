from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled
from aiogram.dispatcher.handler import CancelHandler,current_handler
from aiogram import types,Dispatcher
import asyncio

class Throt(BaseMiddleware):
    def __init__(self,limit:int=5):
        BaseMiddleware.__init__(self)
        self.rate_limit=limit
  
    async def on_process_message(self,message:types.Message,data:dict):
            dp=Dispatcher.get_current()
            try:
                await dp.throttle(key="",rate=self.rate_limit)
            except Throttled as _t:
                await self.msg_throlle(message,_t)
                raise CancelHandler()
    async def msg_throlle(self,msg:types.Message,throlle:Throttled):
            delta=throlle.rate-throlle.delta
            if throlle.exceeded_count<=5:
                await msg.reply("Превышен лимит на сообщения,повторите попытку позже!!!!")
            await asyncio.sleep(delta)
             
    
    
    
        
        
        
         
        
