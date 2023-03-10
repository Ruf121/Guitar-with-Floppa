import random
import time

import telebot
from telebot import types

# Токен
bot = telebot.TeleBot('5584522153:AAEWFjH0efEJRbpAAMWqGQR9tWeYRTY04_c')

# Создание менюшки
welcome = types.ReplyKeyboardMarkup(resize_keyboard=True)
vid_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
akkords = types.ReplyKeyboardMarkup(resize_keyboard=True)
boy = types.ReplyKeyboardMarkup(resize_keyboard=True)
back = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
A = types.ReplyKeyboardMarkup(resize_keyboard=True)
D = types.ReplyKeyboardMarkup(resize_keyboard=True)
E = types.ReplyKeyboardMarkup(resize_keyboard=True)
F = types.ReplyKeyboardMarkup(resize_keyboard=True)
G = types.ReplyKeyboardMarkup(resize_keyboard=True)
H = types.ReplyKeyboardMarkup(resize_keyboard=True)
C = types.ReplyKeyboardMarkup(resize_keyboard=True)

# Создание кнопок для выбора
hi = types.KeyboardButton("Поздороваться")
by = types.KeyboardButton("Попрощаться")
c = types.KeyboardButton("C")
d = types.KeyboardButton("D")
dm = types.KeyboardButton("Dm")
e = types.KeyboardButton("E")
em = types.KeyboardButton("Em")
f = types.KeyboardButton("F")
fm = types.KeyboardButton("Fm")
f_m = types.KeyboardButton("F#m")
g = types.KeyboardButton("G")
a = types.KeyboardButton("A")
h = types.KeyboardButton("H")
hm = types.KeyboardButton("Hm")
am = types.KeyboardButton("Am")
vekt = types.InlineKeyboardButton("Викторина", callback_data="Викторина")
video_lessons = types.KeyboardButton("Видеоуроки")
les_1 = types.InlineKeyboardButton("1", callback_data='1')
ak = types.KeyboardButton("Аккорды")
boi = types.KeyboardButton("Бой")
ch = types.KeyboardButton("Четверка")
sh = types.KeyboardButton("Шестерка")
vos = types.KeyboardButton("Восьмерка")
ret = types.KeyboardButton("Вернуться")
welcome.add(hi)
akkords.add(a, d, e, f, fm, f_m, g, h, hm, c, em, dm, am, ret)
vid_menu.add(les_1, ret)
A.add(a, am)
D.add(d, dm)
E.add(em, e)
F.add(f)
G.add(g)
H.add(h)
C.add(c)
boy.add(ch, sh, vos, ret)
menu.add(ak, boi, by, vekt)
back.add(ret)
# Словарь для генерирования разных ответов в викторине
vic_buttons = {
    'C': types.InlineKeyboardButton("C"),
    'D': types.InlineKeyboardButton("D"),
    'Dm': types.InlineKeyboardButton("Dm"),
    'E': types.InlineKeyboardButton("E"),
    'Em': types.InlineKeyboardButton("Em"),
    'F': types.InlineKeyboardButton("F"),
    'Fm': types.InlineKeyboardButton("Fm"),
    'F#m': types.InlineKeyboardButton("F#m"),
    'G': types.InlineKeyboardButton("G"),
    'A': types.InlineKeyboardButton("A"),
    'H': types.InlineKeyboardButton("H"),
    'Hm': types.InlineKeyboardButton("Hm"),
    'Am': types.InlineKeyboardButton("Am"),
}

# Создание вариантов приветствия и прощания которые от бота
user_inp = {
    1: ["Привет", "Ку", "Хай", "Здарова", "Здаров", "Даров", "Дарова", "Мое почтение"],
    2: ["Пока", "Прощай", "Покеда", "До новых встреч", "Увидимся"]
}

for_vict = {
    'C': r'for_vict/C.jpg',
    'D': r"for_vict/D.jpg",
    'Dm': r'for_vict/Dm.jpg',
    'E': r"for_vict/E.jpg",
    'Em': r"for_vict/Em.jpg",
    "F": r"for_vict/F.jpg",
    "Fm": r"for_vict/Fm.jpg",
    "F#m": r"for_vict/F#m.jpg",
    "G": r"for_vict/G.jpg",
    "A": r"for_vict/A.jpg",
    "H": r"for_vict/H.jpg",
    "Hm": r"for_vict/Hm.jpg",
    "Am": r"for_vict/Am.jpg"
}

# Создание словаря картинок
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
perebor = {}
bo = {
    "Четверка": r'boy/Chetverka.jpg',
    "Шестерка": r'boy/Shesterka.jpg',
    "Восьмерка": r'boy/Vosmerka.jpg'
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
# Словарь с видеоуроками
video = {'1': r''}


# Приветствие
def welcoming(message):
    if message.text == "/start":
        bot.send_message(message.chat.id,
                         "Привет, меня зовут Шлепа, ты можешь Выбрать аккорды или бои и я покажу тебе какие есть варианты :)",
                         reply_markup=menu)
        stick_hi(message)
    elif message.text == "Поздороваться":
        hi_2 = random.choice(list(user_inp[1]))
        bot.send_message(message.chat.id, hi_2, reply_markup=menu)
        stick_hi(message)


# Функции чтобы одни и те же стикеры не повторялись много раз и для их отправки
def stick_dep(message):
    used_stick = []
    chosen = random.choice(list(stick["depr"]))
    old_depr = ''
    while chosen == old_depr:
        chosen = random.choice(list(stick["depr"]))
    bot.send_sticker(message.chat.id, chosen)
    if len(used_stick) == 3:
        used_stick.clear()
    old_depr = chosen
    used_stick.append(old_depr)


def stick_scared(message):
    used_stick = []
    chosen = random.choice(list(stick["scared"]))
    old_scared = ''
    while chosen == old_scared:
        chosen = random.choice(list(stick["scared"]))
    bot.send_sticker(message.chat.id, chosen)
    if len(used_stick) == 3:
        used_stick.clear()
    old_scared = chosen
    used_stick.append(old_scared)


def stick_hi(message):
    used_stick = []
    chosen = random.choice(list(stick["hi"]))
    old_hi = ''
    while chosen == old_hi:
        chosen = random.choice(list(stick["hi"]))
    bot.send_sticker(message.chat.id, chosen)
    if len(used_stick) == 3:
        used_stick.clear()
    old_hi = chosen
    used_stick.append(old_hi)


def stick_by(message):
    used_stick = []
    chosen = random.choice(list(stick["by"]))
    old_by = ''
    while chosen == old_by:
        chosen = random.choice(list(stick["by"]))
    bot.send_sticker(message.chat.id, chosen)
    if len(used_stick) == 3:
        used_stick.clear()
    old_by = chosen
    used_stick.append(old_by)


live = 3
count = 0  # Подсчет угаданных аккордов


@bot.callback_query_handler(func=lambda query: True)
def check_answer(query):
    global live, count
    # Получение ответа
    data = query.data
    print(f'-{data}-')
    # Проверка на правильность ответа
    if data == 'Правильно!':
        bot.send_message(query.message.chat.id, "Правильно!")
        count += 1
    else:
        bot.send_message(query.message.chat.id, "Неправильно :(")
        live -= 1


# Код для викторины
def vikt(message):
    global live, count
    bot.send_message(message.chat.id,
                     "Итак, викторина. \nПравила просты, просто угадываешь аккорд или бой, если ошибаешься, то все по новой")
    # reply_markup=vik)
    while message != "Вернуться" or live > 0:
        vik_quiz = types.InlineKeyboardMarkup()
        vik_answers = []
        true_answer = random.choice(list(vic_buttons))
        fake_answer1 = random.choice(list(vic_buttons))
        fake_answer2 = random.choice(list(vic_buttons))
        fake_answer3 = random.choice(list(vic_buttons))
        vik_answers.append(true_answer)
        vik_answers.append(fake_answer1)
        vik_answers.append(fake_answer2)
        vik_answers.append(fake_answer3)
        random.shuffle(vik_answers)
        for i in range(0, 4):
            if vik_answers[0] == vik_answers[i] and i != 0 and vik_answers[0] != true_answer:
                vik_answers[i] = random.choice(list(vic_buttons))
            elif vik_answers[1] == vik_answers[i] and i != 1 and vik_answers[1] != true_answer:
                vik_answers[i] = random.choice(list(vic_buttons))
            elif vik_answers[2] == vik_answers[i] and i != 2 and vik_answers[2] != true_answer:
                vik_answers[i] = random.choice(list(vic_buttons))
            elif vik_answers[3] == vik_answers[i] and i != 3 and vik_answers[3] != true_answer:
                vik_answers[i] = random.choice(list(vic_buttons))
            else:
                pass
        true_ind = vik_answers.index(true_answer)
        vik_quiz.add(types.InlineKeyboardButton(text=vik_answers[0],
                                                callback_data='Правильно!' if vik_answers[true_ind] == vik_answers[
                                                    0] else 'Неправильно!'))
        vik_quiz.add(types.InlineKeyboardButton(text=vik_answers[1],
                                                callback_data='Правильно!' if vik_answers[true_ind] == vik_answers[
                                                    1] else 'Неправильно!'))
        vik_quiz.add(types.InlineKeyboardButton(text=vik_answers[2],
                                                callback_data='Правильно!' if vik_answers[true_ind] == vik_answers[
                                                    2] else 'Неправильно!'))
        vik_quiz.add(types.InlineKeyboardButton(text=vik_answers[3],
                                                callback_data='Правильно!' if vik_answers[true_ind] == vik_answers[
                                                    3] else 'Неправильно!'))
        bot.send_photo(message.chat.id, open(for_vict[true_answer], "rb"))
        bot.send_message(message.chat.id, "Какой это аккорд?)", reply_markup=vik_quiz)
        time.sleep(5)
        if live == 0:
            bot.send_message(message.chat.id, text=f"Количество жизней закончилось.\n Ты угадал аккордов: {count}",
                             reply_markup=menu)
            count = 0
            break
    message.text = ""
    get_text_messages(message)


# Сам код
@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_text_messages(message):
    b = message.text.title()
    print('-' * 100)
    print({bot.user})
    print(b)
    print(message.chat.id)
    print(message.chat)
    if b == "Поздороваться" or message.text == '/start':
        welcoming(message)
    elif b == "Викторина":
        # bot.send_message(message.chat.id, "Викторина в данный момент разрабатывается")
        # stick_dep(message)
        vikt(message)
    # Вывод боя и выбор
    if b == "Бой":
        bot.send_message(message.chat.id, "Выбирай бой",
                         reply_markup=boy)
    elif b in bo:
        bot.send_photo(message.chat.id, open(bo[b], "rb"))
    # Вывод меню с аккордами
    elif b == "Аккорды":
        bot.send_message(message.chat.id,
                         "Выбирай аккорд\n Крестиком обозначается струна по которой бить нельзя",
                         reply_markup=akkords)
    elif b in akk:
        bot.send_photo(message.chat.id, open(akk[b], "rb"))
    # Возврат к меню
    elif b == "Вернуться":
        bot.send_message(message.chat.id, "Выбери что тебе нужно :)", reply_markup=menu)
    # Отправка видеоуроков пользователю(в будущем)
    # elif b == "Видеоуроки":
    #     bot.send_message(message.chat.id, "Выбирай урок", reply_markup=vid_menu)
    # elif message.text in video:
    #     bot.send_video(message.chat.id, open(video[b], 'rb'))
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
bot.polling(interval=2, none_stop=True)
