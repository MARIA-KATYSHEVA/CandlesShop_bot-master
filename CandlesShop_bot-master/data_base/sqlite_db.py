import sqlite3 as sq
from create_bot import bot, dp
import base64



def sql_start():
    global base, cur
    base = sq.connect('HyggoSoul.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS catalog(img TEXT, name TEXT PRIMARY KEY, price TEXT)')
    base.commit()


# Эта функция будет вносить изменения в базу данных
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO catalog VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nНазвание: {ret[-1]}')
        # await bot.send_document(message.from_user.id, ret)

