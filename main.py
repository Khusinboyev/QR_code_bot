from aiogram import *
from handlers.users.start_handler import *
from handlers.admin.admin_handlers import *
from key import bot, dp
import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode

class functions:
	@staticmethod
	async def check_on_start(user_id):
		with connect('./database/database.sqlite3') as db:
			cursor = db.cursor()
			rows = cursor.execute("SELECT id from channels ").fetchall()
			error_code = 0
			for row in rows:
				r = await bot.get_chat_member(chat_id=row[0], user_id=user_id)
				if r.status in ['member', 'creator', 'admin']:
					pass
				else:
					error_code = 1
		if error_code == 0:
			return True
		else:
			return False

@dp.message_handler(commands='myid')
async def id(message: types.Message):
	await message.reply(text = message.from_user.id)

@dp.message_handler(commands=['help'])
async def qr(message:types.Message):
	await message.reply('Assalomu alaykum 👋\nBu botda siz matnlarni CR CODE ga aylantirishingiz va aksincha CR CODE larni matnda aylantirishingiz mumkin\nBuning uchun siz:\n  • matn\n  • raqam \n\nYoki CR CODE ni yuboring va sabr qiling\n \nVa yana stiker smail... larni qr code qilolmaydi'
	                    '\n\nBiror narsaga tushunmasangiz va bot uchun g`oya yoki taklif bo`lsa adminga murojaat qiling @coder_admin')

@dp.message_handler(content_types='photo')
async def piccr(message: types.Message):
	await message.photo[-1].download("file.png")
	result = decode(Image.open('file.png'))
	data = result[0].data
	await message.reply(data)

@dp.message_handler(content_types='text')
async def translete(message: types.Message):
	if await functions.check_on_start(message.chat.id):
		if len(message.text) < 1200:
			s = message.text

			url = pyqrcode.create(s)

			url.png('myqr.png', scale=6)
			await message.reply_photo(photo=open('myqr.png', 'rb'))
		else:
			await message.reply(
				f'Faqat <b>1260</b> tadan oshmagan belgi yuborishingiz kerak.\nSiz esa <b>{len(message.text)} </b>ta belgi yubordingiz')
	else:
		await message.reply(
			f'Assalomu alaykum {message.from_user.first_name}\nBotimizdan foydalanish uchun kanalimizga azo bo`ing👇👇', reply_markup=join_inline)


if __name__=='__main__':
	executor.start_polling(dispatcher=dp)