from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.exceptions import MessageNotModified
import sys
sys.path.append("C:\Bot_TEDDY\src")
from FUNC import *
from KEYBOARDS import *





menu=lambda CallbackQuery:CallbackQuery.data=="menu"

async def register_handler_cmd_greeting(dp:Dispatcher):
    dp.register_message_handler(cmd_greeting,commands=["start"])


async def register_handler_button_menu(dp:Dispatcher):
    dp.register_message_handler(cmd_menu,commands=["menu"])


async def register_handler_button_spam_text(dp:Dispatcher):
   dp.register_message_handler(text_spam,content_types=["text"])
    


async def register_handler_process_know(dp:Dispatcher):
    dp.register_callback_query_handler(button_know,lambda CallbackQuery:CallbackQuery.data=="know")


async def register_handler_return_menu(dp:Dispatcher)->None:
    dp.register_callback_query_handler(cmd_menu_callback,menu)

async def register_handler_make_order(dp:Dispatcher)->None:
    dp.register_callback_query_handler(button_make_order,lambda CallbackQuery:CallbackQuery.data=="order")
  

async def register_handler_team(dp:Dispatcher)->None:
    dp.register_callback_query_handler(button_team,lambda CallbackQuery:CallbackQuery.data=="team")

async def register_handler_questions(dp:Dispatcher)->None:
    dp.register_callback_query_handler(button_questions,lambda CallbackQuery:CallbackQuery.data=="faq")


async def register_handler_info(dp:Dispatcher):
    dp.register_callback_query_handler(button_info_dog,lambda CallbackQuery:CallbackQuery.data=="info")


async def register_handler_button_right(dp:Dispatcher):
   dp.register_callback_query_handler(button_right,page_cb.filter(action="next"))

async def register_handler_button_left(dp:Dispatcher):
   dp.register_callback_query_handler(button_left,page_cb.filter(action="prev"))
    


async def register_handler_errors(dp:Dispatcher):
   dp.register_errors_handler(not_message_modif,exception=MessageNotModified)
    
    

list_handlers=[register_handler_cmd_greeting,
               register_handler_process_know,
               register_handler_return_menu,
               register_handler_make_order,
               register_handler_team,
               register_handler_questions,
               register_handler_info,
               register_handler_button_right,
               
               register_handler_button_left,
               register_handler_errors,
               register_handler_button_menu,
               register_handler_button_spam_text
               ]


        
        
    

