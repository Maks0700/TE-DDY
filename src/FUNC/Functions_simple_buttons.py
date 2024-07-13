from aiogram.types import Message
from aiogram.types import CallbackQuery,callback_query
from aiogram.types import MediaGroup,InputMediaPhoto,InputMedia,InputFile
import sys
from icecream import ic
from aiogram import types
from aiogram.utils.callback_data import CallbackData
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime,timedelta 
from aiogram import Bot
sys.path.append("C:\Bot_TEDDY\src")
sys.path.append("C:\Bot_TEDDY")
import KEYBOARDS
from Main import bot






photo_total=[r"C:\Bot_TEDDY\src\PHOTO\DOG\DOG.jpg",r"C:\Bot_TEDDY\src\PHOTO\DOLL-GIRL\DOLL.png",r"C:\Bot_TEDDY\src\PHOTO\DRAGON\DRAGON.png",r"C:\Bot_TEDDY\src\PHOTO\UNICORN\UNICORN.png"]


async def sale(bot:Bot,user_id:int):
    await bot.send_message(chat_id=int(user_id),text="""*Скидка

Ура! Скидка!
Сделано с любовью: получите скидку 5% по промокоду HANDMADE5 за проявленный интерес и внимательность! 

Просто отправьте мне его при оформлении заказа, и Ваша скидка будет применена❤️👌*)""",parse_mode="Markdown")
    



describe_total=["""*Собачка
- Игрушка выполнена из мягкой и приятной на ощупь пряжи, которая является гипоаллергенной и подойдет для малышей. Ушки, грудка и часть лапок выполнены из фактурной еще более мягкой пряжи, которая точно не оставит равнодушным.
- Глазки и носик на на безопасном креплении и надежно зафиксированы, так что малыш не сможет их вытащить.
- Высота игрушки около 26 см.
- Время изготовления: около 4-5 дней.
Срок может увеличиться из-за ожидания некоторых цветов пряжи.
- Стоимость БЕЗ доставки: 1150р

Возможен повтор в других цветах!*""","""*Кукла-девочка (1 вариант)
- Игрушка выполнена из мягкой и приятной на ощупь пряжи, которая является гипоаллергенной и подойдет для малышей.  Волосы в данном случае выполнены из фактурной еще более мягкой пряжи. Есть возможность делать различные прически.
- Глазки на безопасном креплении и надежно зафиксированы, так что малыш не сможет их вытащить. Реснички тоже хорошо проклеены. Украшения на сарафане/комбинезоне плотно пришиваются (их можем выбрать с Вами отдельно).
- Высота игрушки около 28 см
- Время изготовления: около 7 дней.
 Срок может увеличиться из-за ожидания некоторых цветов пряжи.
- Стоимость БЕЗ доставки: 1650р

Возможен повтор в других цветах!*""","""*Дракоша
-  Игрушка выполнена из мягкой и приятной на ощупь пряжи, которая является гипоаллергенной и подойдет для малышей.
- Глазки на безопасном креплении и надежно зафиксированы, так что малыш не сможет их вытащить. Реснички тоже хорошо проклеены.
- Высота игрушки около 30 см.
- Время изготовления: около 4-5 дней.
Срок может увеличиться из-за ожидания некоторых цветов пряжи.
- Стоимость БЕЗ доставки: 1150р

Возможен повтор в других цветах!*""","""*Единорожка
- Игрушка выполнена из мягкой и приятной на ощупь пряжи, которая является гипоаллергенной и подойдет для малышей.
- Глазки на безопасном креплении и надежно зафиксированы, так что малыш не сможет их вытащить. Реснички тоже хорошо проклеены.
- Высота игрушки около 28 см
- Время изготовления: около 7 дней.
Срок может увеличиться из-за ожидания некоторых цветов пряжи.
- Стоимость БЕЗ доставки: 1450р

Возможен повтор в других цветах!*"""]

total_dict=dict(zip(photo_total,describe_total))#extend two lists in union


async def cmd_greeting(message:Message):
        
            
            scheduler=AsyncIOScheduler(timezone="Europe/Moscow")
            scheduler.add_job(func=sale,trigger="date",next_run_time=datetime.now()+timedelta(seconds=5),kwargs={"bot":bot,"user_id":message.chat.id})#The established trigger(date in my case) for send message 
            
            scheduler.start()
            await message.answer(f"""*Привет {message.from_user.first_name}! Очень рада тебя видеть 🥰
Здесь ты сможешь получить актуальную информацию, узнать ответы на интересующие тебя вопросы и получить приятный бонус! 🌺
Также тут ты найдешь мои контакты для связи  ✨
Благодарю за проявленный интерес! ❤️*""",parse_mode="Markdown",reply_markup=KEYBOARDS.keyboards_menu_main())
            
            await message.delete()
            

async def cmd_menu(message:Message):
    await message.answer("*Вы вернулись в главное меню.Что Вас конкретно интересует?*❓❓",reply_markup=KEYBOARDS.keyboards_menu_main(),parse_mode="Markdown")       
    await message.delete()
    

async def cmd_menu_callback(callback:CallbackQuery):
    await callback.message.answer("*Вы вернулись в главное меню.Что Вас конкретно интересует?*❓❓",reply_markup=KEYBOARDS.keyboards_menu_main(),parse_mode="Markdown")       
    await callback.message.delete()
    
    
async def text_spam(message:Message):
    await message.reply("*Пользуйтесь встроенными кнопками!!!!*",parse_mode="Markdown")
    await message.delete()





async def button_know(callback:CallbackQuery):
    
        await callback.message.answer("*Отлично! Я благодарна за доверие и надеюсь воплотить в жизнь Вашу идею) ❤️*",parse_mode="Markdown",reply_markup=KEYBOARDS.keyboard_button_know())         
        await callback.message.delete()
        ke
async def button_make_order(callbalck:CallbackQuery):
    
    await callbalck.message.answer("""*Как заказать?
Написать мне в ВКонтакте (https://vk.com/ppppolinka13) или в телеграмм (https://t.me/Pollinchi_k) в личные сообщения.*""",parse_mode="Markdown",reply_markup=KEYBOARDS.keyboard_button_menu())
    await callbalck.message.delete()

async def button_team(callback:CallbackQuery):
    await callback.message.answer("""*Очень рада видеть, что данное творчество находит отклик в сердцах! ❤️

Если хочешь присоединиться, то обязательно пиши мне: чем хочешь заниматься, есть ли опыт, сколько времени готов или готова посвящать этому и примеры работ.

Буду рада работать вместе с заинтересованными и вдохновленными людьми! 🥰🥰*""",parse_mode="Markdown",reply_markup=KEYBOARDS.keyboard_button_menu())
    await callback.message.delete()

async def button_questions(callback:CallbackQuery):
    await callback.message.answer("""*1. Какие стоимость и срок выполнения?
Зависит от типа и сложности игрушки, а также от ожидания некоторых цветов пряжи. В среднем срок выполнения 4-7 дней.

2. Как происходит отправка?
Отправка производится Почтой России.

3. Что насчет оплаты?
Оплата производится в полном размере при оформлении заказа по данным, которые я Вам высылаю.

4.  Хочу увидеть примеры работ!
Примеры работ Вы можете найти в разделе "Подробная информация.

5. У меня другой вопрос.
Напишите мне по указанным выше контактам, и я постараюсь ответить на все Ваши вопросы! 🥰*""",parse_mode="Markdown",reply_markup=KEYBOARDS.keyboard_button_menu())
    await callback.message.delete()

async def button_info_dog(callback:CallbackQuery)->None:
    
    photo_first=InputFile(photo_total[0])#Input Photo as Media
    await callback.message.answer_photo(photo=photo_first,caption=describe_total[0],reply_markup=KEYBOARDS.paginator_right(),parse_mode="Markdown")
    

async def button_left(query:CallbackQuery,callback_data: dict):
        
        page=int(callback_data["page"])-1 if int(callback_data["page"]) > 0 else 0 #Defined current page of function paginator
        photo_test=InputFile(photo_total[page])
        caption_ph=describe_total[page]
        media_gr=InputMediaPhoto(photo_test,caption=caption_ph,parse_mode="Markdown")
        try:
             if page==0:
                    await query.message.edit_media(media=media_gr,reply_markup=KEYBOARDS.paginator_right(page))
             else:
                    await query.message.edit_media(media=media_gr,reply_markup=KEYBOARDS.paginator_major(page))
                 
        except IndexError:#This error is mean index page maybe outed of range available
            pass
        except KeyError:# This error is mean access by key which is not exists in callback_data[page]
            pass
        
async def button_right(query:CallbackQuery,callback_data:dict):
    page=int(callback_data["page"])+1
    photo_test=InputFile(photo_total[page])
    caption_ph=describe_total[page]
    media_gr=InputMediaPhoto(photo_test,caption=caption_ph,parse_mode="Markdown")
    try:
        if page==len(photo_total)-1:# This is switching between page in the end range
            
            await query.message.edit_media(media=media_gr,reply_markup=KEYBOARDS.paginator_left(page))
        else:
            await query.message.edit_media(media=media_gr,reply_markup=KEYBOARDS.paginator_major(page))
            
    except IndexError:
        pass
    except KeyError:
        pass
    except TypeError:
        pass
    
            
async def not_message_modif(update,error):#Bypass error MessageNotModified!!
    return True

    
                
            
        
            
        
        
                
            
            
            
        



    
            
        
        
        

      
               


            
        
            
    
                
                
        
        
    
   


        
            
            

            
            
                        
            
        
        
        
             
    
    
    
    
            
            
        
