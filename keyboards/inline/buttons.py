from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


join_inline = InlineKeyboardMarkup(row_width=2)
join_inline.add(InlineKeyboardButton("Kanalga o`tish", url="https://t.me/Nurun_ala"))
join_inline.add(InlineKeyboardButton("🔁 Tekshirish", callback_data='check'))
