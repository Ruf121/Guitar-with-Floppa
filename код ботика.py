import telebot
from telebot import types
import random

# Токен
bot = telebot.TeleBot('5584522153:AAEWFjH0efEJRbpAAMWqGQR9tWeYRTY04_c')

# Создание менюшки
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
boy = types.ReplyKeyboardMarkup(resize_keyboard=True)
vik = types.ReplyKeyboardMarkup(resize_keyboard=True)
akkords = types.ReplyKeyboardMarkup(resize_keyboard=True)
# Создание кнопок для выбора
welcome = types.KeyboardButton("Поздороваться")
vekt = types.KeyboardButton("Викторина")
c = types.KeyboardButton("C")
d = types.KeyboardButton("D")
e = types.KeyboardButton("E")
em = types.KeyboardButton("Em")
dm = types.KeyboardButton("Dm")
f = types.KeyboardButton("F")
g = types.KeyboardButton("G")
a = types.KeyboardButton("A")
h = types.KeyboardButton("H")
am = types.KeyboardButton("Am")
ch = types.KeyboardButton("Четверка")
sh = types.KeyboardButton("Шестерка")
ak = types.KeyboardButton("Аккорды")
boi = types.KeyboardButton("Бой")
ret = types.KeyboardButton("Вернуться")
markup.add(welcome)
akkords.add(c, d, e, em, f, g, a, h, dm, am, ret)
vik.add(c, d, e, em, f, g, a, h, am, ret)
boy.add(ch, sh, ret)
menu.add(ak, boi, vekt)

# Создание вариантов приветствия и прощания которые вероятно будет вводить пользователь
hi_1 = {
    1: ["Привет", "Ку", "Хай", "Здарова", "Здаров", "Поздороваться", "Даров", "Дарова", "Мое почтение"],
    2: ["Пока", "Прощай", "Покеда", "До новых встреч", "Увидимся"]
}

# Варианты приветствия и прощания от самого бота
hi = {
    1: "Привет",
    2: "Ку",
    3: "Хай",
    4: "Здарова",
    5: "Здаров",
    6: "Поздороваться",
    7: "Даров",
    8: "Мое почтение",
    9: "ghbdtn"
}
by = {
    1: "Пока",
    2: "Прощай",
    3: "Покеда",
    4: "До новых встреч",
    5: "Увидимся",
    6: "gjrf"
}
# Создание словаря для викторинки на знание аккордов
akk = {
    'C': r'C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\С.jpg',
    'D': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\D-2.png.webp",
    'Dm': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\Dm.png",
    'E': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\E.jpg",
    'Em': r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\em.jpg",
    "F": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\f-major.png",
    "G": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\g.jpg",
    "A": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\A.png",
    "H": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\H.jpg",
    "Am": r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\am.webp"
}


# Сам код
@bot.message_handler(content_types=['text', 'audio', 'photo', 'video', 'document'])
def get_text_messages(message):
    b = message.text.title()
    # Начало и приветствие бота
    if message.text == '/start':
        bot.send_message(message.chat.id,
                         text="Привет, меня зовут Шлепа, ты можешь написать аккорд или бой и я отправлю тебе картинку, "
                              "чтобы ты знал как его зажать :)".format(message.from_user), reply_markup=menu)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG5V9joOHcQQpbtKTOMCW3n1eX9n49yAACURsAAi4oEEsHtj8GVrMeKiwE')
    elif b in hi_1[1]:
        hi_2 = random.choice(list(hi.values()))
        bot.send_message(message.chat.id,
                         text=hi_2.format(
                             message.from_user), reply_markup=menu)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG5oVjoV1JA0tzCCkDEhqPGxbZ7-V80AACGSAAAkIxcEqOleNVc2Gz9CwE')

    # Создание викторины
    elif b == "Викторина":
        bot.send_message(message.from_user.id, "Викторина в данный момент разрабатывается")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG5odjoV9eePKBrLbItdphAtMYze31xQACECAAAmE0aErrMemvXMLY8ywE')
    # Вывод боя и выбор, используются локальные файлы
    elif b == "Бой":
        bot.send_message(message.chat.id,
                         text="Выбирай какой бой учим)".format(message.from_user), reply_markup=boy)
        bot.send_message(message.from_user.id, "Там где на картинках крестик или звездочка это удар с глушением")
    elif b == "Четверка":
        bot.send_photo(message.from_user.id, open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\boy\kg5.png", "rb"))
    elif b == "Шестерка":
        bot.send_photo(message.from_user.id,
                       open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\boy\shesterka.jpg", "rb"))

    # Вывод меню с аккордами
    elif b == "Аккорды":
        bot.send_message(message.chat.id,
                         text="Выбирай аккорд".format(
                             message.from_user), reply_markup=akkords)
        bot.send_message(message.from_user.id,
                         '1-это указательный палец 2-это средний палец 3-это безымянный палец 4-это мизинец')
    # Выбор аккордов, используются локальные файлы
    elif message.text == "C":
        bot.send_photo(message.from_user.id, open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\С.jpg", "rb"))
    elif message.text == "D":
        bot.send_photo(message.from_user.id, open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\D-2.png.webp", "rb"))
    elif message.text == "Dm":
        bot.send_photo(message.from_user.id, open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\Dm.png", "rb"))
    elif message.text == "E":
        bot.send_photo(message.from_user.id, open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\E.jpg", "rb"))
    elif message.text == "Em":
        bot.send_photo(message.from_user.id, open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\em.jpg", "rb"))
    elif message.text == "F":
        bot.send_photo(message.from_user.id, open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\f-major.png", "rb"))
    elif message.text == "G":
        bot.send_photo(message.from_user.id, open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\g.jpg", "rb"))
    elif message.text == "A":
        bot.send_photo(message.from_user.id, open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\A.png", "rb"))
    elif message.text == "H":
        bot.send_photo(message.from_user.id, open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\H.jpg", "rb"))
    elif message.text == "Am":
        bot.send_photo(message.from_user.id, open(r"C:\Users\KuzVL\OneDrive\Рабочий стол\Shlepa\ak\am.webp", "rb"))

    # Возврат к меню
    elif b == "Вернуться":
        bot.send_message(message.chat.id, text="Выбери что тебе нужно :)".format(message.from_user), reply_markup=menu)

    # Помощь
    elif message.text == "/help":
        bot.send_message(message.from_user.id,
                         "Я могу тебе показать аккорд, тебе осталось только его написать подсказка:Лучше писать английскими")

    # Прощание
    elif b in hi_1[2]:
        buying = random.choice(list(by.values()))
        bot.send_message(message.chat.id,
                         text=buying.format(message.from_user), reply_markup=markup)
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понял, если тебе что то не понятно напиши /help, а если ты хочешь начать общение то просто "
                         "поздоровайся со мной:)")


# Обратная связь с ботом
bot.polling(none_stop=True, interval=0)
