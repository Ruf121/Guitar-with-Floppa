import telebot
from telebot import types
import random

used_stick = {}

# Токен
bot = telebot.TeleBot('5584522153:AAEWFjH0efEJRbpAAMWqGQR9tWeYRTY04_c')
# Создание менюшки
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
akkords = types.ReplyKeyboardMarkup(resize_keyboard=True)
boy = types.ReplyKeyboardMarkup(resize_keyboard=True)
vik = types.ReplyKeyboardMarkup(resize_keyboard=True)

# Создание кнопок для выбора
welcome = types.KeyboardButton("Поздороваться")
by = types.KeyboardButton("Попрощаться")
vekt = types.KeyboardButton("Викторина")
c = types.KeyboardButton("C")
d = types.KeyboardButton("D")
e = types.KeyboardButton("E")
em = types.KeyboardButton("Em")
f = types.KeyboardButton("F")
g = types.KeyboardButton("G")
a = types.KeyboardButton("A")
h = types.KeyboardButton("H")
am = types.KeyboardButton("Am")
ch = types.KeyboardButton("Четверка")
sh = types.KeyboardButton("Шестерка")
vos = types.KeyboardButton("Восьмерка")
ak = types.KeyboardButton("Аккорды")
boi = types.KeyboardButton("Бой")
ret = types.KeyboardButton("Вернуться")
markup.add(welcome)
akkords.add(c, d, e, em, f, g, a, h, am, ret)
vik.add(c, d, e, em, f, g, a, h, am, ret)
boy.add(ch, sh, vos, ret)
menu.add(ak, boi, vekt, by)

# Создание вариантов приветствия и прощания которые вероятно будет вводить пользователь
user_inp = {
    1: ["Привет", "Ку", "Хай", "Здарова", "Здаров", "Даров", "Дарова", "Мое почтение"],
    2: ["Пока", "Прощай", "Покеда", "До новых встреч", "Увидимся"]
}

# Создание словаря картинок
akk = {
    'C': r'C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\С.jpg',
    'D': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\D-2.png.webp",
    'E': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\E.jpg",
    'Em': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\em.jpg",
    "F": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\f-major.png",
    "G": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\g.jpg",
    "A": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\A.png",
    "H": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\H.jpg",
    "Am": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\am.webp"
}
bo = {
    "Четверка": r'C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\boy\kg5.png',
    "Шестерка": r'C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\boy\shesterka.jpg',
    "Восьмерка": r'C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\boy\Vosmerka.jpg'
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
           'CAACAgIAAxkBAAEHOdZjwFNinFXQJAABxmNTUAAB1y-vkt8vAAJnDAAC-xihS4JDjXDhj00DLQQ']
}


# Приветствие
def welcoming(message):
    if message.text == "/start":
        bot.send_message(message.chat.id,
                         text="Привет, меня зовут Шлепа, ты можешь написать аккорд или бой и я отправлю тебе картинку, "
                              "чтобы ты знал как его зажать :)".format(message.from_user), reply_markup=menu)
        bot.send_sticker(message.chat.id, random.choice(list(stick["hi"])))
    elif message.text == "Поздороваться":
        hi_2 = random.choice(list(user_inp[1]))
        bot.send_message(message.chat.id, text=hi_2.format(message.from_user), reply_markup=menu)
        bot.send_sticker(message.chat.id, random.choice(list(stick["hi"])))


# Создание викторины, ПОПРОБОВАТЬ СДЕЛАТЬ ИГРУ
def vikt(message):
    bot.send_message(message.chat.id, text="Итак, викторина.".format(message.from_user), reply_markup=vik)
    bot.send_message(message.from_user.id,
                     "Правила просты, просто угадываешь аккорд или бой, если ошибаешься, то все по новой")
    live = 3
    count = 0
    while live > 0:
        b = message.text.title()
        answer = random.choice(list(akk))
        ind = akk[answer]
        bot.send_photo(message.from_user.id, open(ind, "rb"))
        bot.send_message(message.chat.id, text="Какой это аккорд?)".format(message.from_user), reply_markup=akkords)
        if b == answer:
            bot.send_message(message.from_user.id, "Правильно!")
            count += 1
        elif b != answer:
            bot.send_message(message.from_user.id, "Неправильно")
            live -= 1
        if live == 0:
            bot.send_message(message.from_user.id,
                             text=f"Ты проиграл, количество правильных ответов:{count}".format(message.from_user),
                             reply_markup=menu)


# Сам код
@bot.message_handler(content_types=['text', 'audio', 'photo', 'video', 'document'])
def get_text_messages(message):
    b = message.text.title()
    # Начало и приветствие бота
    if b == "/start" or b == "Поздороваться":
        welcoming(message)
    elif b == "Викторина":
        bot.send_message(message.from_user.id, "Викторина в данный момент разрабатывается")
        bot.send_sticker(message.chat.id, random.choice(list(stick["depr"])))
    # Вывод боя и выбор
    elif b == "Бой":
        bot.send_message(message.chat.id,
                         text="Выбирай бой".format(
                             message.from_user), reply_markup=boy)
    elif b in bo:
        bot.send_photo(message.from_user.id, open(bo[b], "rb"))
    # Вывод меню с аккордами
    elif b == "Аккорды":
        bot.send_message(message.chat.id,
                         text="Выбирай аккорд".format(
                             message.from_user), reply_markup=akkords)
    elif b in akk:
        bot.send_photo(message.from_user.id, open(akk[b], "rb"))
    # Возврат к меню
    elif b == "Вернуться":
        bot.send_message(message.chat.id, text="Выбери что тебе нужно :)".format(message.from_user), reply_markup=menu)
    # Помощь
    elif message.text == "/help":
        bot.send_message(message.from_user.id,
                         "Я могу тебе показать аккорд, тебе осталось только его написать подсказка:Лучше писать английскими")
    # Прощание
    elif b == "Попрощаться":
        buying = random.choice(list(user_inp[2]))
        bot.send_message(message.chat.id,
                         text=buying.format(message.from_user), reply_markup=markup)
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понял, если тебе что то не понятно напиши /help, а если ты хочешь начать общение то просто "
                         "поздоровайся со мной:)")


# Обратная связь с ботом
bot.polling(none_stop=True, interval=2)
