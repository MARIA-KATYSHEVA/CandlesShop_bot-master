from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# button1 = KeyboardButton('🛍️Каталог')
# button2 = KeyboardButton('🧭Расположение')
# button3 = KeyboardButton('🚚 Cпособы доставки')
# button4 = KeyboardButton('💳 Cпособы оплаты')

button1 = KeyboardButton('/Каталог')
button2 = KeyboardButton('/Расположение')
button3 = KeyboardButton('/Доставка')
button4 = KeyboardButton('/Оплата')

kb_client = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
# kb_client.add(button1).add(button2).add(button3).add(button4)
kb_client.row(button1, button2).row(button3, button4)

# kb_client = ReplyKeyboardMarkup(resize_keyboard=True) # если хочу спрятать кнопки - аргумент one_time_keyboard=True

# Друг под другом
# kb_client.add(button1).add(button2).add(button3)
# button1, а под ним в одном ряду button2 и button3
# kb_client.add(button1).add(button2).insert(button3)
# все в ряд
# kb_client.add(button1).add(button2).add(button3).row(button4, button5)




