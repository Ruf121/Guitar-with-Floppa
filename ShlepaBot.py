from config import *


# Токен
bot = TeleBot(Bot_token)

# Создание менюшки
welcome = types.ReplyKeyboardMarkup(resize_keyboard=True)
les_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
akkords = types.ReplyKeyboardMarkup(resize_keyboard=True)
boy = types.ReplyKeyboardMarkup(resize_keyboard=True)
back = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


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
gm = types.KeyboardButton("Gm")
a = types.KeyboardButton("A")
a_ = types.KeyboardButton("A#")
h = types.KeyboardButton("H")
h7 = types.KeyboardButton("H7")
hm = types.KeyboardButton("Hm")
am = types.KeyboardButton("Am")
vekt = types.KeyboardButton("Викторина")
lessons = types.KeyboardButton("Уроки")
les_1 = types.KeyboardButton("1")
les_2 = types.KeyboardButton("2")
les_3 = types.KeyboardButton("3")
les_4 = types.KeyboardButton("4")
les_5 = types.KeyboardButton("5")
les_6 = types.KeyboardButton("6")
les_7 = types.KeyboardButton("7")
les_8 = types.KeyboardButton("8")
ak = types.KeyboardButton("Аккорды")
boi = types.KeyboardButton("Бой")
ch = types.KeyboardButton("Четверка")
sh = types.KeyboardButton("Шестерка")
sem = types.KeyboardButton("Семерка")
vos = types.KeyboardButton("Восьмерка")
ret = types.KeyboardButton("Вернуться")
welcome.add(hi)
akkords.add(a, a_, d, e, f, fm, f_m, g, gm, h, h7, hm, c, em, dm, am, ret)
les_menu.add(les_1, les_2, les_3, les_4, les_5, les_6, les_7, ret)
boy.add(ch, sh, sem, vos, ret)
menu.add(lessons, ak, boi, by, vekt)
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
    'C': r"ak/С/C.jpg",
    'D': r"ak/D/D.jpg",
    'Dm': r'ak/D/Dm.jpg',
    'E': r"ak/E/E.jpg",
    'Em': r"ak/E/Em.jpg",
    "F": r"ak/F/F.jpg",
    "Fm": r"ak/F/Fm.jpg",
    "F#M": r"ak/F/F#m.jpg",
    "G": r"ak/G/G.jpg",
    "Gm": r"ak/G/Gm.jpg",
    "A": r"ak/A/A.jpg",
    "A#": r"ak/A/A#.jpg",
    "Am": r"ak/A/Am.jpg",
    "H": r"ak/H/H.jpg",
    "H7": r"ak/H/H7.jpg",
    "Hm": r"ak/H/Hm.jpg"
}
bo = {
    "Четверка": r'boy/Chetverka.jpg',
    "Шестерка": r'boy/Shesterka.jpg',
    "Семерка": r"boy/Semerka.jpg",
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
# Словарь с уроками
less_dict = {
    # Наработка боя четверка
    '1': "Звезда по имени Солнце\n"
         "(4) - Нужно повторить бой зажимая аккорд 4 раза\n"
         r"\2 - Нужно повторить всю строку 2 раза" "\n"
         "Бой: Четверка\n"
         "Аккорды:\n"
         r"Am(4) C(4) Dm(4) G(4)\2" "\n"
         "Dm(4) Am(4)",

    '2': 'Пачка сигарет\n'
         r'Em C Am G\до конца',

    # Наработка боя шестерка
    '3': 'Кукушка\n'
         'Бой: Шестерка\n'
         'Вступление:\n'
         r'Am C G Em\4' '\n'
         'Куплет\n'
         r'Am(4) G Dm Am(2)\2' '\n'
         'Припев\n'
         r'G Dm Am(2)\4',

    '4': "Просвистела\n"
         "Бой: Шестерка\n"
         r"Аккорды: Em C G H7 \До конца",

    '5': "Когда твоя девушка больна\n"
         "Бой: Шестерка\n"
         "Аккорды:\n "
         r"G Em C D \4" "\n"
         r"C D G Em\2" '\n'
         'C D G Em C D G',
    # Знакомство с баррэ
    '6':'Утренний рассвет\n'
         'Бой: Шестерка'
         r'D(2) Hm Hm(У) A(У)\2' '\n'
         'D(2) Hm(2) D(2) Hm(2)\n'
         'Четверка(Dm C) Шестерка(A#)\2' '\n'
         'Шестерка(Gm A#) A(У)',
    # Совмещение Четверки и Шестерки
    '7': 'Дурак и молния\n'
         'Четверка\n'
         r'F(2) E(2) Am(4) \3 раза' '\n'
         'F(У) E(У) Am(У)\n'
         'Припев\n'
         r'F E Am(2) \3 раза' '\n'
         'Шестёрка\n'
         'Dm Em Am(У)\n'
         'G(2) Em(2) F G Em Am Dm(2) E(У)',
    # Изучение боя семерка
    '8': 'Выхода нет\n'
         '0,5 - разделение боя\n'
         'Первая половина - первые  два удара\n'
         'Вторая половина - все остальное\n'
         'Бой: Семерка\n'
         'Аккорды:\n'
         'Em(4)\n'
         r'C(0,5) G(0,5) D Em(0,5) C(0,5) G\2' '\n'
         r'C(0,5) G(0,5) D\2' '\n'
         r'Em C G D\2' '\n'
         'C D Em(4)'
}
aud_primery = {'1': "Primery_pesen/Звезда по имени Солнце (пример) .aac",

               '2': 'Primery_pesen/Пачка сигарет (пример).aac',

               '3': 'Primery_pesen/Кукушка(пример).aac',

               '4': "Primery_pesen/Просвистела(пример).aac",

               '5': 'Primery_pesen/Когда твоя девушка больна(пример).aac',

               '6': 'Primery_pesen/Утренний рассвет(пример).aac',

               '7': 'Primery_pesen/Дурак и Молния(пример).aac',

               '8': 'Primery_pesen/Выхода нет(пример).aac'}


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


# Код для викторины
def vikt(message):
    global live, count
    bot.send_message(message.chat.id,
                     "Итак, викторина. \nПравила просты, просто угадываешь аккорд или бой, если ошибаешься, то все по новой")
    # reply_markup=vik)
    while message != "Вернуться" or live > 0:
        print("Цикл начался")
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
        true_ind = vik_answers.index(true_answer)
        for i in range(4):
            while vik_answers.count(vik_answers[i]) > 1:
                print("Производится замена ответа")
                for j in range(len(vik_answers)):
                    vik_answers[j] = random.choice(list(vic_buttons))
        # while vik_answers.count(true_answer) > 1:
        #     print("Производится замена ответа")
        #     for i in range(len(vik_answers)):
        #         vik_answers[i] = random.choice(vik_answers)
        # while vik_answers.count(fake_answer1) > 1:
        #     print("Производится замена ответа")
        #     for i in range(len(vik_answers)):
        #         vik_answers[i] = random.choice(vik_answers)
        # while vik_answers.count(fake_answer2) > 1:
        #     print("Производится замена ответа")
        #     for i in range(len(vik_answers)):
        #         vik_answers[i] = random.choice(vik_answers)
        # while vik_answers.count(fake_answer3) > 1:
        #     print("Производится замена ответа")
        #     for i in range(len(vik_answers)):
        #         vik_answers[i] = random.choice(vik_answers)
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
        bot.send_photo(message.chat.id, open(for_vict[vik_answers[true_ind]], "rb"))
        bot.send_message(message.chat.id, "Какой это аккорд?)", reply_markup=vik_quiz)
        print("Отправлен вопрос")
        time.sleep(5)
        if live == 0:
            bot.send_message(message.chat.id, text=f"Количество жизней закончилось.\n Ты угадал аккордов: {count}",
                             reply_markup=menu)
            count = 0
            break
    message.text = ""
    get_text_messages(message)


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


# Сам код
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    b = message.text.title()
    print('-' * 100)
    print(message.from_user)
    print(b)
    print(datetime.datetime.now())
    print(message.chat.id)
    # print(message.chat)
    if b == "Поздороваться" or message.text == '/start':
        welcoming(message)
    elif b == "Викторина":
        bot.send_message(message.chat.id, "Викторина в данный момент разрабатывается")
        stick_dep(message)
        # vikt(message)
    # Вывод боя и выбор
    elif b == "Бой":
        bot.send_message(message.chat.id, "Выбирай бой\n"
                                          "Примечание: Щ - удар по струнам с глушением или без",
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
    # Отправка уроков пользователю(в будущем)
    elif b == "Уроки":
        bot.send_message(message.chat.id, "Выбирай урок\n"
                                          "Аккорд(количество повторов боя на аккорде) - Повтор игры аккорда\n"
                                          "Аккорд(У) - Означает что нужно просто ударить по струнам вниз"
                                          "/ число повторов - Количество повторов всей строки\n"
                                          "Пример с объянением есть в первом уроке если что-то не понятно",
                         reply_markup=les_menu)
    elif b in less_dict:
        bot.send_message(message.chat.id, less_dict[b])
        if aud_primery[b] != '':
            bot.send_message(message.chat.id, 'Пример:')
            bot.send_audio(message.chat.id, open(aud_primery[b], "rb"))
    # Помощь
    elif message.text == "/help":
        bot.send_message(message.chat.id,
                         "Я могу тебе показать аккорд или бой, тебе осталось только его выбрать нажимая кнопки внизу")
    # Прощание
    elif b == "Попрощаться":
        buying = random.choice(list(user_inp[2]))
        bot.send_message(message.chat.id, buying, reply_markup=welcome)
        stick_by(message)
    else:
        bot.send_message(message.chat.id, "Я тебя не понял, если тебе что то нужно напиши /help")


# Обратная связь с ботом
bot.polling(interval=2, none_stop=True)
