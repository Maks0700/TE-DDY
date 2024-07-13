from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup
from aiogram.utils.callback_data import CallbackData



button_menu=InlineKeyboardButton("Вернуться обратно в меню⬅️⬅️",callback_data="menu")
page_cb=CallbackData("empty","action","page") # Create pattern of CalbackData() for callback_data in functions and processing buttons

def keyboards_menu_main()->InlineKeyboardMarkup:
    keyboard_menu_main=InlineKeyboardMarkup(row_width=4).add(
        InlineKeyboardButton("Я знаю, что хочу🧸",callback_data="know"),
        InlineKeyboardButton("Подробная информация🗓📌",callback_data="info")).add(
        InlineKeyboardButton("Хочу в команду🔝🆒",callback_data="team"),
        InlineKeyboardButton("FAQ❓",callback_data="faq"))
        
    
    return keyboard_menu_main


def keyboard_button_know()->InlineKeyboardMarkup:
    keyboard_know=InlineKeyboardMarkup(row_width=2).add(button_menu)
    return keyboard_know


def paginator_major(page:int=0)->InlineKeyboardMarkup:
    return InlineKeyboardMarkup().row(InlineKeyboardButton(text="⬅️",callback_data=page_cb.new(action="prev",page=page)),
                                      InlineKeyboardButton(text="➡️",callback_data=page_cb.new(action="next",page=page))).add(button_menu)#The creating pattern of CallbackData and addressing by prefix and *parts 
    
def paginator_right(page:int=0)->InlineKeyboardMarkup:
    return InlineKeyboardMarkup().row(InlineKeyboardButton("➡️",callback_data=page_cb.new(action="next",page=page))).add(
        button_menu
        )


def paginator_left(page:int=0)->InlineKeyboardMarkup:
    return InlineKeyboardMarkup().row(InlineKeyboardButton("⬅️",callback_data=page_cb.new(action="prev",page=page))).add(
        button_menu
        )




def keyboard_button_menu(): # This is FUNCTION FOR APPEARENCE ERORRS!! MIDDLEWARE
    return InlineKeyboardMarkup().row(button_menu)







    
    





    





        
        
    





    



    



