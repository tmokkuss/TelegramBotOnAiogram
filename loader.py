from aiogram import Bot, Dispatcher, types
import config
import logging

bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)