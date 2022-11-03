+ [App.py](#app.py)
+ [config.py](#config.py)
+ [loader.py](#loader.py)
+ [callback_datas.py](#callback_datas.py)
+ [choice_buttons.py](#choice_buttons.py)
+ [purchase.py](#purchase.py)


## Main
Это репозиторий бота, который умеет отправлять рандомные факты, цитаты из keyboard-кнопок. Также может выполнить несколько команд c '\' ( например отправить расписание на сегодня или же на завтра). Также бот по команде может вызвать inline-кнопки и для каждого выдать ответ.

## App.py

Главный код для запуска всего дерева кода

```python
if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    import random
    import datetime
    from aiogram import Bot, Dispatcher, executor, types
    from aiogram.utils.callback_data import CallbackData

    from loader import bot, dp

    f = open('facts.txt', 'r', encoding='UTF-8')
    facts = f.read().split('\n')
    f.close()

    f = open('thinks.txt', 'r', encoding='UTF-8')
    thinks = f.read().split('\n')
    f.close()


    @dp.message_handler(commands=['start'])
    async def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        fact = types.KeyboardButton('Факт')
        think = types.KeyboardButton('Мотивация')
        ruz = types.KeyboardButton('Расписание')
        deadlines = types.KeyboardButton('Дедлайны')
        records = types.KeyboardButton('Записи')
        markup.add(ruz, deadlines, records)
        markup.add(fact, think)
        mess = f'Привет,{message.from_user.first_name}. Вот мой нынешний функционал'
        await bot.send_message(message.chat.id, mess, reply_markup=markup)


    @dp.message_handler(commands=['today'])
    async def today(message):
        now = datetime.datetime.today().weekday()
        if now == 0:
            mess = """Расписание на сегодня:
                   8:00 - 10:50
                   Математический анализ
                   https://events.webinar.ru/20063157/782301512

                   11:10 - 12:30
                   Английский язык
                   https://events.webinar.ru/20063157/186438404"""
            await bot.send_message(message.chat.id, mess)
        elif now == 1:
            mess = """Расписание на сегодня:
                   8:00 - 9:20
                   Вводный курс математики
                   https://events.webinar.ru/20063157/1797944677

                   9:30 - 12:30
                   Дискретная математика
                   https://events.webinar.ru/20063157/186438404"""
            await bot.send_message(message.chat.id, mess)
        elif now == 2:
            mess = """Расписание на сегодня:
                   8:00 - 9:20
                   Консультация по Дискретной математике
                   https://us02web.zoom.us/j/76586765434?pwd=VDlyZ1YxUXpuL2ZjWG4xbXF0Tk9RZz09

                   9:30 - 10:50
                   Основы и методология программирования
                   https://events.webinar.ru/20063157/2063575350

                   11:10 - 14:20
                   Физическая культура
                   https://zoom.us/j/3654602354
                   КОД: ggVF5G
                   """
            await bot.send_message(message.chat.id, mess)
        elif now == 3:
            mess = """Расписание на сегодня:
                   9:30 - 10:50
                   Основы и методология программирования
                   https://events.webinar.ru/20063157/2063575350

                   11:10 - 12:30
                   Вводный курс математики
                   https://events.webinar.ru/20063157/1170045680

                   13:00 - 14:20
                   Английский язык
                   https://events.webinar.ru/20063157/186438404
                   """
            await bot.send_message(message.chat.id, mess)
        elif now == 4:
            mess = """Расписание на сегодня:
                   9:30 - 12:30
                   Логистика в условиях цифровой экономики
                   https://events.webinar.ru/20063157/1849702597

                   13:00 - 14:20
                   Управленческая эконимика
                   https://events.webinar.ru/20063157/703389457
                   """
            await bot.send_message(message.chat.id, mess)
        elif now == 5:
            mess = """Расписание на сегодня:
                   8:00 - 10:50
                   Цифровая грамотность
                   https://events.webinar.ru/20063157/1232737973

                   11:10 - 14:20
                   Линейная алгебра и геометрия
                   https://events.webinar.ru/20063157/1409146203
                   """
            await bot.send_message(message.chat.id, mess)
        elif now == 6:
            mess = f'Расписание на сегодня нету, отдыхай и делай домашку'
            await bot.send_message(message.chat.id, mess)


    @dp.message_handler(commands=['tomorrow'])
    async def today(message):
        now = datetime.datetime.today().weekday()
        if now == 0:
            mess = """Расписание на завтра:
                   8:00 - 9:20
                   Вводный курс математики
                   https://events.webinar.ru/20063157/1797944677

                   9:30 - 12:30
                   Дискретная математика
                   https://events.webinar.ru/20063157/186438404"""
            await bot.send_message(message.chat.id, mess)
        elif now == 1:
            mess = """Расписание на завтра:
                   8:00 - 9:20
                   Консультация по Дискретной математике
                   https://us02web.zoom.us/j/76586765434?pwd=VDlyZ1YxUXpuL2ZjWG4xbXF0Tk9RZz09

                   9:30 - 10:50
                   Основы и методология программирования
                   https://events.webinar.ru/20063157/2063575350

                   11:10 - 14:20
                   Физическая культура
                   https://zoom.us/j/3654602354
                   КОД: ggVF5G
                   """
            await bot.send_message(message.chat.id, mess)
        elif now == 2:
            mess = """Расписание на завтра:
                   9:30 - 10:50
                   Основы и методология программирования
                   https://events.webinar.ru/20063157/2063575350

                   11:10 - 12:30
                   Вводный курс математики
                   https://events.webinar.ru/20063157/1170045680

                   13:00 - 14:20
                   Английский язык
                   https://events.webinar.ru/20063157/186438404
                   """
            await bot.send_message(message.chat.id, mess)
        elif now == 3:
            mess = """Расписание на завтра:
                   9:30 - 12:30
                   Логистика в условиях цифровой экономики
                   https://events.webinar.ru/20063157/1849702597

                   13:00 - 14:20
                   Управленческая эконимика
                   https://events.webinar.ru/20063157/703389457
                   """
            await bot.send_message(message.chat.id, mess)
        elif now == 4:
            mess = """Расписание на завтра:
                   8:00 - 10:50
                   Цифровая грамотность
                   https://events.webinar.ru/20063157/1232737973

                   11:10 - 14:20
                   Линейная алгебра и геометрия
                   https://events.webinar.ru/20063157/1409146203
                   """
            await bot.send_message(message.chat.id, mess)
        elif now == 5:
            mess = f'Расписание на завтра нету, отдыхай и делай домашку'
            await bot.send_message(message.chat.id, mess)
        elif now == 6:
            mess = """Расписание на завтра:
                           8:00 - 10:50
                           Математический анализ
                           https://events.webinar.ru/20063157/782301512

                           11:10 - 12:30
                           Английский язык
                           https://events.webinar.ru/20063157/186438404"""
            await bot.send_message(message.chat.id, mess)


    @dp.message_handler()
    async def get_user_text(message):
        if message.text == 'Расписание':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Расписание", url='https://ruz.hse.ru/ruz/main'))
            await bot.send_message(message.chat.id, 'Лови Расписание!', reply_markup=markup)
        elif message.text == 'id':
            await bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}')
        elif message.text == 'Факт':
            mess = random.choice(facts)
            await bot.send_message(message.chat.id, mess)
        elif message.text == 'Мотивация':
            mess = random.choice(thinks)
            await bot.send_message(message.chat.id, mess)
        elif message.text == 'Записи' or message.text == 'записи':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Записи",
                                                  url='https://docs.google.com/spreadsheets/d/1ZVVRapMav_x2lXy64cp_qhCASdM6Yjsck8j9Tm0fEEM/edit#gid=0'))
            await bot.send_message(message.chat.id, 'Вот записи наших занятий!', reply_markup=markup)
        elif message.text == 'Дз' or message.text == 'Домашка' or message.text == 'Дедлайны':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Дедлайны", url='https://disk.yandex.ru/i/fVDCYuRvCbJTiA'))
            await bot.send_message(message.chat.id, 'Домашка пока что только такая!', reply_markup=markup)
```

## loader.py

Код объявления Dispatcher

```python
from aiogram import Bot, Dispatcher, types
import config
import logging

bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
```
## config.py

Код импорта токена бота из .env

```python
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
```


## choice_buttons.py

Объявление самих inline-кнопок и их CallBack

```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

choice_linag = InlineKeyboardButton(text='Линейная алгебра', callback_data=buy_callback.new(item_name='linag'))
choice.insert(choice_linag)
choice_diskret = InlineKeyboardButton(text='Дискретная математика', callback_data=buy_callback.new(item_name='diskret'))
choice.insert(choice_diskret)
choice_matan = InlineKeyboardButton(text='Математический анализ', callback_data=buy_callback.new(item_name='matan'))
choice.insert(choice_matan)
choice_prog = InlineKeyboardButton(text='Программирование', callback_data=buy_callback.new(item_name='prog'))
choice.insert(choice_prog)
choice_dg = InlineKeyboardButton(text='Цифровая грамотность', callback_data=buy_callback.new(item_name='dg'))
choice.insert(choice_dg)
choice_logist = InlineKeyboardButton(text='Логистика', callback_data=buy_callback.new(item_name='logist'))
choice.insert(choice_logist)
choice_eco = InlineKeyboardButton(text='Экономика', callback_data=buy_callback.new(item_name='eco'))
choice.insert(choice_eco)
choice_eng = InlineKeyboardButton(text='Английский язык', callback_data=buy_callback.new(item_name='eng'))
choice.insert(choice_eng)
```

## callback_datas.py

Объявление callback общий кнопок

```python
from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData("Buy", "item_name")

```

## purchase.py

Реакция бота на callback и ответ в чат

```python
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, chat
import aiogram
from keyboards.inline.choice_buttons import choice
from loader import dp, bot


@dp.message_handler(Command("getemails"))
async def show_emails(message: Message):
    await message.answer(text="Выбери предмет", reply_markup=choice)


@dp.callback_query_handler(text_contains='linag')
async def choice_linag(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.answer("ФИО: Вагурина Ирина Вячеславовна\n"
                              "email: ivagurina@hse.ru")


@dp.callback_query_handler(text_contains='diskret')
async def choice_diskret(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.answer("ФИО: Казакевич Виктория Григорьевна\n"
                              "email: vkazakevich@hse.ru  vgkazakevich@etu.ru")


@dp.callback_query_handler(text_contains='matan')
async def choice_matan(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.answer("ФИО: Литвинова Виктория Викторовна\n"
                              "email: vvlitvinova@hse.ru")


@dp.callback_query_handler(text_contains='prog')
async def choice_prog(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.answer("ФИО: Резник Сергей Александрович\n"
                              "email: sreznik@hse.ru\n"
                              "tg: @sreznick\n"
                              "ФИО: Шагаев Дамир Тагирзянович\n"
                              "email: dshagaev@hse.ru")


@dp.callback_query_handler(text_contains='dg')
async def choice_dg(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.answer("ФИО: Травин Александр Сергеевич\n"
                              "email: atravin@hse.ru")


@dp.callback_query_handler(text_contains='logist')
async def choice_logist(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.answer("ФИО: Левченко Анна Владимировна\n"
                              "email: a.levchenko@hse.ru")


@dp.callback_query_handler(text_contains='log')
async def choice_log(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.answer("ФИО: Левченко Анна Владимировна\n"
                              "email: a.levchenko@hse.ru")


@dp.callback_query_handler(text_contains='eco')
async def choice_eco(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.answer("ФИО: Сторчевой Максим Анатольевич\n"
                              "email: mstorchevoy@hse.ru")


@dp.callback_query_handler(text_contains='eng')
async def choice_eng(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.answer("ФИО: Солнцев Сергей Владимирович\n"
                              "email: svsolntsev@hse.ru")

```
