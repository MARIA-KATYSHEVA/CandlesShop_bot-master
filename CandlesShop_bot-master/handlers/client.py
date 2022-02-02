from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Привет!✋ Я - бот онлайн-магазин натуральных свечей и ароматов для дома Soul Hygge! \n Я всегда готов помочь! Выбери в меню интересующую тебя кнопку 👇',
                           reply_markup=kb_client)


# @dp.message_handler(commands=['🛍️Каталог'])
async def catalog(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь скоро появится каталог!', reply_markup=kb_client)


# @dp.message_handler(commands=['🧭Расположение'])
async def address(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь скоро появятся адреса!', reply_markup=kb_client)


# @dp.message_handler(commands=['🚚 Cпособы доставки'])
async def delivery(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Вы можете выбрать следующие способы доставки: \n ✔ Самовывоз ул. Садовая-Сухаревская 15с1 (Есть бесплатная парковка) \n ✔ Курьером по Москве внутри МКАД 2-3 дня — 350₽, за МКАД до 10 км 2-3 дня — 450₽ Пн-Вс с 11.30 до 21.00 \n ✔ Отправка такси до подъезда по Москве в день заказа - рассчитывается индивидуально \n ✔ Доставка за МКАД свыше 10км и по России транспортной компанией СДЭК - 450₽ от 2 до 16 дней \n ✔ Доставка по РФ Почтой России - рассчитывается индивидуально", reply_markup=kb_client)



# @dp.message_handler(commands=['💳 Cпособы оплаты'])
async def payment(message: types.Message):
    await bot.send_message(message.from_user.id, 'Оплата производится картой или электронным кошельком на нашем сайте  https://soulhygge.ru/', reply_markup=kb_client)


# @dp.message_handler(commands=['Расположение'])
async def parket_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь скоро появятся адреса!')


def register_handlers_client(dp: Dispatcher) -> object:
    dp.register_message_handler(command_start, commands=['start', 'help'])
    # dp.register_message_handler(catalog, commands=['🛍️Каталог'])
    # dp.register_message_handler(address, commands=['🧭Расположение'])
    # dp.register_message_handler(delivery, commands=['🚚 Cпособы доставки'])
    # dp.register_message_handler(payment, commands=['💳 Cпособы оплаты'])
    dp.register_message_handler(catalog, commands=['Каталог'])
    dp.register_message_handler(address, commands=['Расположение'])
    dp.register_message_handler(delivery, commands=['Доставка'])
    dp.register_message_handler(payment, commands=['Оплата'])

# @dp.message_handler(commands=['Каталог'])
# async def parket_catalog_command(message: types.Message):
#     await sqlite_db.sql_read(message)
