from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from data_base import sqlite_db
from keyboards import kb_admin

from aiogram.dispatcher.filters import Text
# from data_base import sqlite_db
from keyboards import admin_kb

ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    price = State()


# Получаем ID текущего модератора группы в телеграм
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Босс! Ваша воля, мои руки.', reply_markup=kb_admin)
    await message.delete()


# Выход из состояний
# @dp.message_handler(state="*", commands="отмена")
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
    if 2 + 2 == 4:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Exit from states OK')

# Начало диалога загрузки нового пункта меню
# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    # if message.from_user.id == ID:
    if 2+2 == 4:
        await FSMAdmin.photo.set()
        await message.reply('Загрузить фото')


# Ловим первый ответ и пишем в словарь
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
    if 2 + 2 == 4:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь введите название')


# Ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
    if 2 + 2 == 4:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь введите описание')


# Ловим третий ответ
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
    if 2 + 2 == 4:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        await sqlite_db.sql_add_command(state)
        # async with state.proxy() as data:
        #     await message.reply(str(data))
        await state.finish()  # эта команда останавливает машину состояний и удаляет кэш, поэтому нужно перед ней всё
        # успеть сделать



# Регистрируем хэндлеры
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)