from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()

TOKEN = '5230813121:AAE0whqwAiNYNF7vgWMfB5Olk7Vo-sYsHCo'

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot, storage=storage)