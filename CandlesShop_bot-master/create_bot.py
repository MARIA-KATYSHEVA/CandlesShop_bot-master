from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# или нужно импортировать os если к токену обращаемся так:
# bot = Bot(token=os.getenv('TOKEN))

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)