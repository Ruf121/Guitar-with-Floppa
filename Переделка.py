from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
import random

bot = Bot(token='5584522153:AAEWFjH0efEJRbpAAMWqGQR9tWeYRTY04_c')
dp = Dispatcher(bot)

user_inp = {
    1: ["Привет", "Ку", "Хай", "Здарова", "Здаров", "Даров", "Дарова", "Мое почтение"],
    2: ["Пока", "Прощай", "Покеда", "До новых встреч", "Увидимся"]
}
akk = {
    'C': r'ak/С/C.jpg',
    'D': r"ak/D/D.jpg",
    'Dm': r'ak/D/Dm.jpg',
    'E': r"ak/E/E.jpg",
    'Em': r"ak/E/Em.jpg",
    "F": r"ak/F/F.jpg",
    "Fm": r"ak/F/Fm.jpg",
    "F#M": r"ak/F/F#m.jpg",
    "G": r"ak/G/G.jpg",
    "A": r"ak/A/A.jpg",
    "Am": r"ak/A/Am.jpg",
    "H": r"ak/H/H.jpg",
    "Hm": r"ak/H/Hm.jpg"
}
stick = {
    # Просто для того чтобы поздороваться
    "hi": ['CAACAgIAAxkBAAEG5oVjoV1JA0tzCCkDEhqPGxbZ7-V80AACGSAAAkIxcEqOleNVc2Gz9CwE',
           'CAACAgIAAxkBAAEHNh9jvwtrSG5d9ODVFwkAAdiSBMiyCZUAAmQiAALvQWlKaTmyyNstuMMtBA',
           'CAACAgIAAxkBAAEHOcpjwFEe-dgckwclnbLrr6qay4mlkAAC8AoAAozKqUoAAfScFqvy1AItBA',
           'CAACAgIAAxkBAAEHOcxjwFElfpJWFxvOaQKiQGdp9zOljgACLxAAAnEbqEo5-QrXpUyHMy0E',
           'CAACAgIAAxkBAAEHOc5jwFEoLUiJ5jOwiyf8nwzhnh7D3AACCwsAAuHfqUpX01r7JW3ECC0E'],
    # Стикеры с грустным или депрессивным Шлепой
    "depr": ['CAACAgIAAxkBAAEG5odjoV9eePKBrLbItdphAtMYze31xQACECAAAmE0aErrMemvXMLY8ywE',
             'CAACAgIAAxkBAAEHNhVjvwpxsTxcx2gXPSZZ9bUBnvr0bAACKA0AAtgkAAFJFu-IZGRz4XstBA',
             'CAACAgIAAxkBAAEHNhdjvwp_v28JoV6n7-7J3mDG5im6bQACAxEAAoS74Ek3fGZjMbw2Zy0E',
             'CAACAgIAAxkBAAEHNhNjvwpu_qY6Nutnc1Bv8QEKUT0ecAACJA8AAkF0MUtLbb06I1IVEy0E'],

    "by": ['CAACAgIAAxkBAAEHOdBjwFM8F7Ups61jlebM-vfZLyAqmwACFg0AAi5FMUvkjTAr0RfRUy0E',
           'CAACAgIAAxkBAAEHOdFjwFM9Uk-tR7Uz8TBkjNvna6UAAaIAAkANAALRBuhKXBBwRgJRkoUtBA',
           'CAACAgIAAxkBAAEHOdRjwFNbGhkVyTzAsVHYrezTqq3i5wAC3AwAArwyMEvpqHQDAcqfgC0E',
           'CAACAgIAAxkBAAEHOdZjwFNinFXQJAABxmNTUAAB1y-vkt8vAAJnDAAC-xihS4JDjXDhj00DLQQ'],

    "scared": ['CAACAgIAAxkBAAEHlx1j3r4VzuDiqh8zWKH9UCoRYd-o5gAC5goAAqEGoUpEgJAmKveTjy4E',
               'CAACAgIAAxkBAAEHlz9j3sg62boThgL2BJa4x56x_TwsDwAC_gkAAijjMEsBHslhx99bIi4E',
               'CAACAgIAAxkBAAEHl0Fj3sj0mePpU5ehcdyl7zf6P4UsjwACIh8AAs7wEEsQpDtCO8Q8rS4E',
               'CAACAgIAAxkBAAEHl0Nj3snJfe6U7gS48bkjAAFZkwbF3XUAAjkjAALSO3BKN-IZU2C_-P4uBA']
}
bo = {
    "Четверка": r'boy/Chetverka.jpg',
    "Шестерка": r'boy/Shesterka.jpg',
    "Восьмерка": r'boy/Vosmerka.jpg'
}


# Функции чтобы одни и те же стикеры не повторялись много раз и для их отправки
async def stick_dep(message):
    used_stick = []
    chosen = random.choice(list(stick["depr"]))
    old_depr = ''
    while chosen == old_depr:
        chosen = random.choice(list(stick["depr"]))
    await bot.send_sticker(message.chat.id, chosen)
    if len(used_stick) == 3:
        used_stick.clear()
    old_depr = chosen
    used_stick.append(old_depr)


async def stick_scared(message):
    used_stick = []
    chosen = random.choice(list(stick["scared"]))
    old_scared = ''
    while chosen == old_scared:
        chosen = random.choice(list(stick["scared"]))
    await bot.send_sticker(message.chat.id, chosen)
    if len(used_stick) == 3:
        used_stick.clear()
    old_scared = chosen
    used_stick.append(old_scared)


async def stick_hi(message):
    used_stick = []
    chosen = random.choice(list(stick["hi"]))
    old_hi = ''
    while chosen == old_hi:
        chosen = random.choice(list(stick["hi"]))
    await bot.send_sticker(message.chat.id, chosen)
    if len(used_stick) == 3:
        used_stick.clear()
    old_hi = chosen
    used_stick.append(old_hi)


async def stick_by(message):
    used_stick = []
    chosen = random.choice(list(stick["by"]))
    old_by = ''
    while chosen == old_by:
        chosen = random.choice(list(stick["by"]))
    await bot.send_sticker(message.chat.id, chosen)
    if len(used_stick) == 3:
        used_stick.clear()
    old_by = chosen
    used_stick.append(old_by)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(
        "Привет, меня зовут Шлепа, ты можешь Выбрать аккорды или бои и я покажу тебе какие есть варианты :)/n"
        "Также есть несколько интересных команд которые могут быть использованы в боте, чтобы узнать о них просто напиши /help")


@dp.message_handler(commands=['Поздороваться', 'Попрощаться'])
async def Hi_and_By(message: types.Message):
    if message.text.title() == '/Поздороваться':
        hi_2 = random.choice(list(user_inp[1]))
        await bot.send_message(message.chat.id, hi_2)
        await stick_hi(message)
    else:
        buying = random.choice(list(user_inp[2]))
        await bot.send_message(message.chat.id, buying)
        await stick_by(message)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Вот список того что я могу :)")
    await bot.send_message(message.from_user.id,
                           "1 - Можешь написать /Поздороваться или /Попрощаться если вы достаточно интеллигентны\n"
                           "2 - Можешь выбрать аккорды используя /аккорды\n"
                           "3 - Можешь выбрать бои используя /бои\n"
                           "4 - Так же есть викторина /Викторина\n")


executor.start_polling(dp)
