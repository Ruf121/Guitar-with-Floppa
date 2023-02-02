import random
from telebot import time

import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType

# Токен
bot = telebot.TeleBot('5584522153:AAEWFjH0efEJRbpAAMWqGQR9tWeYRTY04_c')

# Создание менюшки
welcome = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
akkords = types.ReplyKeyboardMarkup(resize_keyboard=True)
boy = types.ReplyKeyboardMarkup(resize_keyboard=True)
vik = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
A = types.ReplyKeyboardMarkup(resize_keyboard=True)
D = types.ReplyKeyboardMarkup(resize_keyboard=True)
E = types.ReplyKeyboardMarkup(resize_keyboard=True)
F = types.ReplyKeyboardMarkup(resize_keyboard=True)
G = types.ReplyKeyboardMarkup(resize_keyboard=True)
H = types.ReplyKeyboardMarkup(resize_keyboard=True)
C = types.ReplyKeyboardMarkup(resize_keyboard=True)
vik_quiz = types.InlineKeyboardMarkup()
# Создание кнопок для выбора
hi = types.KeyboardButton("Поздороваться")
by = types.KeyboardButton("Попрощаться")
vekt = types.KeyboardButton("Викторина")
c = types.KeyboardButton("C")
d = types.KeyboardButton("D")
dm = types.KeyboardButton("Dm")
e = types.KeyboardButton("E")
em = types.KeyboardButton("Em")
f = types.KeyboardButton("F")
g = types.KeyboardButton("G")
a = types.KeyboardButton("A")
h = types.KeyboardButton("H")
am = types.KeyboardButton("Am")
ak = types.KeyboardButton("Аккорды")
boi = types.KeyboardButton("Бой")
ch = types.KeyboardButton("Четверка")
sh = types.KeyboardButton("Шестерка")
vos = types.KeyboardButton("Восьмерка")
ret = types.KeyboardButton("Вернуться")
welcome.add(hi)
akkords.add(a, d, e, f, g, h, c, em, dm, am, ret)
A.add(a, am)
D.add(d, dm)
E.add(em, e)
F.add(f)
G.add(g)
H.add(h)
C.add(c)
vik.add(c, d, e, em, f, g, a, h, am, dm, ret)
boy.add(ch, sh, vos, ret)
menu.add(ak, boi, vekt, by)

# Словарь для генерирования разных ответов в викторине
vic_buttons = {
    'c': types.InlineKeyboardButton("C"),
    'd': types.InlineKeyboardButton("D"),
    'dm': types.InlineKeyboardButton("Dm"),
    'e': types.InlineKeyboardButton("E"),
    'em': types.InlineKeyboardButton("Em"),
    'f': types.InlineKeyboardButton("F"),
    'g': types.InlineKeyboardButton("G"),
    'a': types.InlineKeyboardButton("A"),
    'h': types.InlineKeyboardButton("H"),
    'am': types.InlineKeyboardButton("Am"),
    'ch': types.InlineKeyboardButton("Четверка"),
    'sh': types.InlineKeyboardButton("Шестерка"),
    'vos': types.InlineKeyboardButton("Восьмерка"),
}

# Создание вариантов приветствия и прощания которые от бота
user_inp = {
    1: ["Привет", "Ку", "Хай", "Здарова", "Здаров", "Даров", "Дарова", "Мое почтение"],
    2: ["Пока", "Прощай", "Покеда", "До новых встреч", "Увидимся"]
}

for_vict = {
    'C': r'C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\for_vict\С.jpg',
    'D': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\for_vict\D.png",
    'E': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\for_vict\E.jpg",
    'Em': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\for_vict\em.jpg",
    "F": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\for_vict\f-major.png",
    "G": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\for_vict\g.jpg",
    "Dm": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\for_vict\Dm.png",
    "A": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\for_vict\A.png",
    "H": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\for_vict\H.jpg",
    "Am": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\for_vict\Am.png"
}

# Создание словаря картинок
akk = {
    'C': r'C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\С\C.png',
    'C(III)': r'C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\С\C(III).png',
    'C(VI)': r'C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\С\C(VI).png',
    'D': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\D\D.png",
    'Dm': r'C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\D\Dm.png',
    'E': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\E\E.png",
    'Em': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\E\Em.png",
    "F": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\F\F.png",
    "G": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\G\G.png",
    "A": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\A\A.jpg",
    "H": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\H\H.png",
    "Am": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Guitar-with-Floppa\ak\A\Am.png"
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
@bot.message_handler(['start', 'help'])
def welcoming(message):
    if message.text == "/start":
        bot.send_message(message.chat.id,
                         "Привет, меня зовут Шлепа, ты можешь написать аккорд или бой и я отправлю тебе картинку, "
                         "чтобы ты знал как его зажать :)", reply_markup=menu)
        stick_hi(message)
    elif message.text == "Поздороваться":
        hi_2 = random.choice(list(user_inp[1]))
        bot.send_message(message.chat.id, hi_2, reply_markup=menu)
        stick_hi(message)
    elif message.text == "/help":
        bot.send_message(message.chat.id,
                         "Что-то пошло не так, если тебе что то не понятно напиши /help, а если ты хочешь начать общение то просто "
                         "напиши /start или нажми кнопку Поздороваться:)")


# Функции чтобы одни и те же стикеры не повторялись много раз и для их отправки
def stick_dep(message):
    used_stick_depr = []
    chosen = random.choice(list(stick["depr"]))
    old_depr = ''
    while chosen == old_depr:
        chosen = random.choice(list(stick["depr"]))
    bot.send_sticker(message.chat.id, chosen)
    if len(used_stick_depr) == 3:
        used_stick_depr.clear()
    old_depr = chosen
    used_stick_depr.append(old_depr)


def stick_hi(message):
    used_stick_hi = []
    chosen = random.choice(list(stick["hi"]))
    old_hi = ''
    while chosen == old_hi:
        chosen = random.choice(list(stick["hi"]))
    bot.send_sticker(message.chat.id, chosen)
    if len(used_stick_hi) == 3:
        used_stick_hi.clear()
    old_hi = chosen
    used_stick_hi.append(old_hi)


def stick_by(message):
    used_stick_by = []
    chosen = random.choice(list(stick["by"]))
    old_by = ''
    while chosen == old_by:
        chosen = random.choice(list(stick["by"]))
    bot.send_sticker(message.chat.id, chosen)
    if len(used_stick_by) == 3:
        used_stick_by.clear()
    old_by = chosen
    used_stick_by.append(old_by)


# Разобраться как создавать опрос
def generator_of_quiz():
    true_answer = random.choice(list(vic_buttons))
    fake_answer1 = random.choice(list(vic_buttons))
    fake_answer2 = random.choice(list(vic_buttons))
    fake_answer3 = random.choice(list(vic_buttons))
    vik_quiz.add(vic_buttons[true_answer], vic_buttons[fake_answer1], vic_buttons[fake_answer2], vic_buttons[fake_answer3])


def vikt(message):
    # poll_markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    # poll_markup.add(KeyboardButton('send me a poll',
    #                                request_poll=KeyboardButtonPollType(type='quiz')))
    # from my experience, only quiz type and regular type polls can be sent.

    remove_board = ReplyKeyboardRemove()
    # bot.send_message(message.chat.id, "Ку ку", reply_markup=vik_quiz)
    # some other code here
    # this can be used to remove the reply-keyboard when you no longer need it.
    # bot.send_message(message.chat.id, "Что то", reply_markup=remove_board)
    # time.sleep(15)
    bot.send_message(message.chat.id, "Итак, викторина.", reply_markup=vik)
    bot.send_message(message.chat.id,
                     "Правила просты, просто угадываешь аккорд или бой, если ошибаешься, то все по новой")
    live = 3
    count = 0
    while live > 0:
        generator_of_quiz()
        answer = random.choice(list(for_vict))
        ind = for_vict[answer]
        bot.send_photo(message.chat.id, open(ind, "rb"))
        bot.send_message(message.chat.id, "Какой это аккорд?)", reply_markup=vik_quiz)
        print(answer)
        time.sleep(5)
        # Ожидание бота ответа от пользователя
        if message.text == answer:
            bot.send_message(message.chat.id, "Правильно!")
            count += 1
        elif live == 0 or message.text == "Вернуться":
            bot.send_message(message.chat.id, f"Ты проиграл, количество правильных ответов:{count}",
                             reply_markup=menu)
    else:
        bot.send_message(message.chat.id, "Неправильно")
        live -= 1


# Сам код
@bot.message_handler(content_types=['text', 'audio', 'photo', 'video', 'document'])
def get_text_messages(message):
    b = message.text.title()
    if b == "Поздороваться":
        welcoming(message)
    elif b == "Викторина":
        # bot.send_message(message.chat.id, "Викторина в данный момент разрабатывается")
        # stick_dep(message)
        vikt(message)
    # Вывод боя и выбор
    if b == "Бой":
        bot.send_message(message.chat.id, "Выбирай бой", reply_markup=boy)
        bot.send_message(message.chat.id, "Примечание: крестиком обозначается глушение ударом")
    elif b in bo:
        bot.send_photo(message.chat.id, open(bo[b], "rb"))
    # Вывод меню с аккордами
    elif b == "Аккорды":
        bot.send_message(message.chat.id, "Выбирай аккорд", reply_markup=akkords)
        bot.send_message(message.chat.id,
                         "Примечание, крестиком обозначается струна которую нельзя трогать, а кружком просто открытая струна")
    elif b in akk:
        bot.send_photo(message.chat.id, open(akk[b], "rb"))
    # Возврат к меню
    elif b == "Вернуться":
        bot.send_message(message.chat.id, "Выбери что тебе нужно :)", reply_markup=menu)
    # Помощь
    elif message.text == "/help":
        bot.send_message(message.chat.id,
                         "Я могу тебе показать аккорд или бой, тебе осталось только его выбрать нажимая кнопки внизу")
    # Прощание
    elif b == "Попрощаться":
        buying = random.choice(list(user_inp[2]))
        bot.send_message(message.chat.id, buying, reply_markup=welcome)
        stick_by(message)


# Обратная связь с ботом
bot.polling(interval=2)
