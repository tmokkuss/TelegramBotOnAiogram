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

