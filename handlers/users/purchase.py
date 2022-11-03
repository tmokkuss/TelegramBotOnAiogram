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