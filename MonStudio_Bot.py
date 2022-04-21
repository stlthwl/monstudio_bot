import telebot
from telebot import types
from telebot.types import InputMediaPhoto


bot = telebot.TeleBot('YOUR_TOKEN')     # YOUR OWN TOKEN FOR TELEGRAM BOT
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
name = ''
phone = ''
specialist = ''
promotion_name = ''
promotion_phone = ''
promotion_name2 = ''
promotion_phone2 = ''


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Цены и услуги', 'Записаться')
    markup.row('Акции', 'О нас')
    #markup.row('Отзывы')
    bot.send_message(message.chat.id, 'MONSTUDIO - студия маникюра и педикюра!💅🏻',
                     reply_markup=markup)
    bot.send_message(message.chat.id, 'Чтобы узнать интересующую Вас информацию, выберите нужный раздел, пользуясь '
                                      'подсказками ниже👇🏻', reply_markup=markup)
    bot.register_next_step_handler(message, section_selection)


def section_selection(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Цены и услуги':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.from_user.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, prices_and_services)
    elif message.text == 'Записаться':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.from_user.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, sign_up)
    elif message.text == 'Акции':
        # markup.row('Записаться на маникюр по акции')
        # markup.row('Записаться на брови по акции')
        markup.row('В начало')
        bot.send_message(message.chat.id, 'В настоящий момент нет акций', reply_markup=markup)
        # bot.send_message(message.chat.id, 'Акции:\n\n-30% в день рожденья\nАкция действует пять дней до и после дня рождения при предъявлении документа;\n\n'
        #                                   'Знакомство с мастером\nМаникюр с покрытием за 990руб;\n\n'
        #                                   'Брови со скидкой\nКоррекция бровей с окрашиванием за 690руб;\n\n'
        #                                   '-7% за отзыв\nОставьте отзыв на сайте или сделайте репост нашей страницы Instagram.'
        #                                   , reply_markup=markup)
        bot.register_next_step_handler(message, start)
        # bot.register_next_step_handler(message, promotion_sign_up)
    elif message.text == 'О нас':
        markup.row('Контакты', 'Примеры работ')
        bot.send_message(message.from_user.id, 'Уютная студия маникюра в центре города Домодедово.\nНаши специалисты - '
                                               'настоящие мастера своего дела!\nОказываем качественные услуги и даем '
                                               'гарантию на наши работы.\nКомфортная зона ожидания, чай, кофе, WI-FI, '
                                               'ТВ.\nМы ценим своих клиентов и делаем все, чтобы Вы были довольны!'
                                               '\nЖдем Вас у нас в студии😊', reply_markup=markup)
        bot.register_next_step_handler(message, info)
    else:
        markup.row('В начало')
        bot.send_message(message.chat.id, 'Для продолжения работы воспользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, start)


def prices_and_services(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Ногтевой сервис':
        markup.row('Записаться')
        markup.row('Вернуться назад')
        markup.row('В начало')
        with open('/home/stlthwl/mon_bot/img/nailpr.jpg', 'rb') as price_nails:
            data = price_nails.read()
        bot.send_photo(message.from_user.id, photo=data)
        bot.send_message(message.from_user.id, 'Хотите записаться?', reply_markup=markup)
        bot.register_next_step_handler(message, sign_from)
    elif message.text == 'Брови':
        # markup.row('Записаться')
        # markup.row('Вернуться назад')
        markup.row('В начало')
        # browprice = open('/home/stlthwl/mon_bot/img/browpr.jpg', 'rb')
        # bot.send_photo(message.chat.id, browprice)
        # bot.send_message(message.from_user.id, 'Хотите записаться?', reply_markup=markup)
        bot.send_message(message.from_user.id, 'В настоящий момент данный раздел временно недоступен', reply_markup=markup)
        bot.register_next_step_handler(message, start)
    else:
        markup.row('В начало')
        bot.send_message(message.chat.id, 'Для общения со мной пользуйтесь встроенной клавиатурой👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, start)


def back_or_finish(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Вернуться назад':
        markup.row('Контакты', 'Примеры работ')
        bot.send_message(message.from_user.id, 'Выберите подраздел', reply_markup=markup)
        bot.register_next_step_handler(message, info)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def sign_from(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Записаться':
        markup.row('Светлана', 'Елена')
        markup.row('Евгения')
        bot.send_message(message.chat.id, 'Выберите мастера', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Вернуться назад':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, prices_and_services)
    elif message.text == 'В начало':
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def sign_from2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Записаться':
        markup.row('Алена')
        bot.send_message(message.chat.id, 'Выберите мастера', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Вернуться назад':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, prices_and_services)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Введите номер Вашего телефона')
    bot.register_next_step_handler(message, reg_phone)


def promotion_reg_name(message):
    global promotion_name
    promotion_name = message.text
    bot.send_message(message.from_user.id, 'Введите номер Вашего телефона')
    bot.register_next_step_handler(message, promotion_reg_phone)
    
    
def promotion_reg_name2(message):
    global promotion_name2
    promotion_name2 = message.text
    bot.send_message(message.from_user.id, 'Введите номер Вашего телефона')
    bot.register_next_step_handler(message, promotion_reg_phone2)


def reg_phone(message):
    global phone
    phone = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    confirm = 'Имя: ' + str(name) + '\nТелефон: ' + str(phone) + '\nВерно?'
    bot.send_message(message.from_user.id, text=confirm, reply_markup=keyboard)


def promotion_reg_phone(message):
    global promotion_phone
    promotion_phone = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='correct')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='incorrect')
    keyboard.add(key_no)
    confirm = 'Имя: ' + str(promotion_name) + '\nТелефон: ' + str(promotion_phone) + '\nВерно?'
    bot.send_message(message.from_user.id, text=confirm, reply_markup=keyboard)


def promotion_reg_phone2(message):
    global promotion_phone2
    promotion_phone2 = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='right')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='notright')
    keyboard.add(key_no)
    confirm = 'Имя: ' + str(promotion_name) + '\nТелефон: ' + str(promotion_phone) + '\nВерно?'
    bot.send_message(message.from_user.id, text=confirm, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if call.data == "yes":
        global name
        global phone
        global specialist
        markup.row('Получить купон')
        confirm = 'Новая запись!\n' + 'К мастеру: ' + str(specialist) + '\nИмя: ' + str(name) + '\nТелефон: ' + str(phone)
        msg = bot.send_message(call.message.chat.id, 'Заявка успешно отправлена!\nВ ближайшее время наш специалист с '
                                                     'Вами свяжется.\nБлагодарим за уделенное время и'
                                                     ' дарим Вам купон на скидку!', reply_markup=markup)
        bot.send_message(chat_id=-558081836, text=confirm)
        bot.register_next_step_handler(msg, coupon)
    elif call.data == 'correct':
        global promotion_name
        global promotion_phone
        markup.row('В начало')
        confirm = 'Новая запись!\n' + 'Акция: знакомство с мастером\n' + 'Имя: ' + str(promotion_name) + '\nТелефон: ' + str(promotion_phone)
        msg = bot.send_message(call.message.chat.id, 'Заявка успешно отправлена!\nВ ближайшее время наш специалист с '
                                                     'Вами свяжется.\nБлагодарим за уделенное время!', reply_markup=markup)
        bot.send_message(chat_id=-558081836, text=confirm)
        bot.register_next_step_handler(msg, back_or_finish)
    elif call.data == 'right':
        global promotion_name2
        global promotion_phone2
        markup.row('В начало')
        confirm = 'Новая запись!\n' + 'Акция: брови со скидкой\n' + 'Имя: ' + str(promotion_name2) + '\nТелефон: ' + str(promotion_phone2)
        msg = bot.send_message(call.message.chat.id, 'Заявка успешно отправлена!\nВ ближайшее время наш специалист с '
                                                     'Вами свяжется.\nБлагодарим за уделенное время!', reply_markup=markup)
        bot.send_message(chat_id=-558081836, text=confirm)
        bot.register_next_step_handler(msg, back_or_finish)    
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Повторите попытку\nВведите имя')
        bot.register_next_step_handler(call.message, reg_name)
    elif call.data == "incorrect":
        bot.send_message(call.message.chat.id, 'Повторите попытку\nВведите имя')
        bot.register_next_step_handler(call.message, promotion_reg_name)
    elif call.data == "notright":
        bot.send_message(call.message.chat.id, 'Повторите попытку\nВведите имя')
        bot.register_next_step_handler(call.message, promotion_reg_name2)

def sign_up(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Ногтевой сервис':
        markup.row('Светлана', 'Елена')
        # markup.row('Евгения')
        bot.send_message(message.from_user.id, 'Выберите мастера', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Брови':
        # markup.row('Алена')
        markup.row('В начало')
        # bot.send_message(message.chat.id, 'Выберите мастера', reply_markup=markup)
        bot.send_message(message.chat.id, 'В настоящий момент данный раздел временно недоступен', reply_markup=markup)
        bot.register_next_step_handler(message, start)
    else:
        markup.row('В начало')
        bot.send_message(message.chat.id, 'Для общения со мной пользуйтесь встроенной клавиатурой👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, start)


def promotion_sign_up(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard = types.InlineKeyboardMarkup()
    if message.text == 'Записаться на маникюр по акции':
        markup = types.ReplyKeyboardRemove(selective=False)
        zhenka = open('/home/stlthwl/mon_bot/img/zhenya.jpg', 'rb')
        bot.send_photo(message.chat.id, zhenka)
        url_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻@mon_studio_dmd',
                                             url='https://www.instagram.com/mon_studio_dmd/')
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp:\n+79684705401\n+79261533738', reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Введите имя: ', reply_markup=markup)
        bot.register_next_step_handler(message, promotion_reg_name)
    elif message.text == 'Записаться на брови по акции':
        markup = types.ReplyKeyboardRemove(selective=False)
        zhenka = open('/home/stlthwl/mon_bot/img/alena.jpg', 'rb')
        bot.send_photo(message.chat.id, zhenka)
        url_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻@mon_studio_dmd',
                                             url='https://www.instagram.com/mon_studio_dmd/')
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp:\n+79684705401\n+79261533738', reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Введите имя: ', reply_markup=markup)
        bot.register_next_step_handler(message, promotion_reg_name2)    
    elif message.text == 'В начало':
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def specialists(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.InlineKeyboardMarkup()
    global specialist
    specialist = message.text
    if (message.text == 'Светлана') or (message.text == 'Записаться к Светлане'):
        markup.row('Подтвердить запись')
        markup.row('Вернуться назад')
        markup.row('В начало')
        svetka = open('/home/stlthwl/mon_bot/img/sveta.jpg', 'rb')
        bot.send_photo(message.chat.id, svetka)
        url_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻 @impash_love',
                                             url='https://www.instagram.com/impash_love')
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp: +79684705401', reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Подтвердите запись, чтобы получить купон на скидку😊', reply_markup=markup)
        bot.register_next_step_handler(message, confirm_sing_up)
    elif (message.text == 'Елена') or (message.text == 'Записаться к Елене'):
        markup.row('Подтвердить запись')
        markup.row('Вернуться назад')
        markup.row('В начало')
        lenka = open('/home/stlthwl/mon_bot/img/lena.jpg', 'rb')
        bot.send_photo(message.chat.id, lenka)
        url_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻 @_lenas_nails',
                                             url='https://www.instagram.com/_lenas_nails')
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp: +79261533738', reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Подтвердите запись, чтобы получить купон на скидку😊', reply_markup=markup)
        bot.register_next_step_handler(message, confirm_sing_up)
    elif (message.text == 'Евгения') or (message.text == 'Записпться к Евгении') or (message.text == 'Записаться по акции'):
        markup.row('Подтвердить запись')
        markup.row('Вернуться назад')
        markup.row('В начало')
        zhenka = open('/home/stlthwl/mon_bot/img/zhenya.jpg', 'rb')
        bot.send_photo(message.chat.id, zhenka)
        url_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻@mon_studio_dmd',
                                             url='https://www.instagram.com/mon_studio_dmd/')
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp:\n+79684705401\n+79261533738', reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Подтвердите запись, чтобы получить купон на скидку😊', reply_markup=markup)
        bot.register_next_step_handler(message, confirm_sing_up)
    elif (message.text == 'Алена') or (message.text == 'Записаться к Алене'):
        markup.row('Подтвердить запись')
        markup.row('Вернуться назад')
        markup.row('В начало')
        tanka = open('/home/stlthwl/mon_bot/img/alena.jpg', 'rb')
        bot.send_photo(message.chat.id, tanka)
        url_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻@mon_studio_dmd',
                                             url='https://www.instagram.com/mon_studio_dmd/')
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp:\n+79684705401\n+79261533738', reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Подтвердите запись, чтобы получить купон на скидку😊', reply_markup=markup)
        bot.register_next_step_handler(message, confirm_sing_up)
    elif message.text == 'Вернуться назад':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, info_about_master)
    elif message.text == 'В начало':
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def confirm_sing_up(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    if message.text == 'Подтвердить запись':
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(message.chat.id, 'Введите имя', reply_markup=markup)
        bot.register_next_step_handler(msg, reg_name)
    elif message.text == 'Вернуться назад':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, sign_up)
    elif message.text == 'В начало':
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def coupon(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Получить купон':
        markup.row('В начало')
        kup = open('/home/stlthwl/mon_bot/img/cpn.jpg', 'rb')
        bot.send_photo(message.chat.id, kup)
        bot.send_message(message.chat.id, 'Чтобы получить скидку, покажите купон мастеру', reply_markup=markup)
        bot.register_next_step_handler(message, back_or_finish)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.InlineKeyboardMarkup()
    if message.text == 'Контакты':
        markup.row('Вернуться назад')
        markup.row('В начало')
        adres_btn = types.InlineKeyboardButton(text='Адрес: г. Домодедово, Каширское ш., 7А',
                                               url='https://yandex.ru/maps/10725/domodedovo/house/kashirskoye_shosse_7a/Z04YcQFkQEQDQFtvfXh1dnllYQ==/?ll=37.764914%2C55.447566&utm_source=main_stripe_big&z=16.65')
        keyboard.add(adres_btn)
        insta_btn = types.InlineKeyboardButton(text='Ссылка на Instagram 👉🏻@mon_studio_dmd',
                                               url='https://www.instagram.com/mon_studio_dmd/')
        keyboard.add(insta_btn)
        site_btn = types.InlineKeyboardButton(text='Наш сайт: monstudiodmd.ru', url='https://monstudiodmd.ru')
        keyboard.add(site_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp:\n+79684705401\n+79261533738', reply_markup=keyboard)
        bot.send_message(message.from_user.id, 'Связаться с нами можно по любому из указанных '
                                               'выше номеров, а так же с помощью Instagram', reply_markup=markup)
        bot.register_next_step_handler(message, back_or_finish)
    elif message.text == 'Примеры работ':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, info_about_master)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def info_about_master(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Ногтевой сервис':
        markup.row('Светлана', 'Елена')
        # markup.row('Евгения')
        bot.send_message(message.from_user.id, 'Выберите мастера', reply_markup=markup)
        bot.register_next_step_handler(message, info_photo)
    elif message.text == 'Брови':
        # markup.row('Алена')
        markup.row('В начало')
        # bot.send_message(message.chat.id, 'Выберите мастера', reply_markup=markup)
        bot.send_message(message.chat.id, 'В настоящий момент данный раздел временно недоступен', reply_markup=markup)
        bot.register_next_step_handler(message, start)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def info_photo(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Светлана':
        markup.row('Записаться к Светлане')
        markup.row('Вернуться назад')
        markup.row('В начало')
        ph1 = open('/home/stlthwl/mon_bot/img/Света/pic1.jpeg', 'rb')
        ph2 = open('/home/stlthwl/mon_bot/img/Света/pic2.jpeg', 'rb')
        ph3 = open('/home/stlthwl/mon_bot/img/Света/pic3.jpeg', 'rb')
        ph4 = open('/home/stlthwl/mon_bot/img/Света/pic4.jpeg', 'rb')
        ph5 = open('/home/stlthwl/mon_bot/img/Света/pic5.jpeg', 'rb')
        ph6 = open('/home/stlthwl/mon_bot/img/Света/pic6.jpeg', 'rb')
        ph7 = open('/home/stlthwl/mon_bot/img/Света/pic7.jpeg', 'rb')
        ph8 = open('/home/stlthwl/mon_bot/img/Света/pic8.jpeg', 'rb')
        ph9 = open('/home/stlthwl/mon_bot/img/Света/pic9.jpeg', 'rb')
        ph10 = open('/home/stlthwl/mon_bot/img/Света/pic10.jpeg', 'rb')
        media = [InputMediaPhoto(ph1), InputMediaPhoto(ph2), InputMediaPhoto(ph3), InputMediaPhoto(ph4),
				 InputMediaPhoto(ph5),
				 InputMediaPhoto(ph6), InputMediaPhoto(ph7), InputMediaPhoto(ph8), InputMediaPhoto(ph9),
				 InputMediaPhoto(ph10)]
        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Хотите записаться?', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Елена':
        markup.row('Записаться к Елене')
        markup.row('Вернуться назад')
        markup.row('В начало')
        le1 = open('/home/stlthwl/mon_bot/img/Лена/l1.jpeg', 'rb')
        le2 = open('/home/stlthwl/mon_bot/img/Лена/l2.jpeg', 'rb')
        le3 = open('/home/stlthwl/mon_bot/img/Лена/l3.jpeg', 'rb')
        le4 = open('/home/stlthwl/mon_bot/img/Лена/l4.jpeg', 'rb')
        le5 = open('/home/stlthwl/mon_bot/img/Лена/l5.jpeg', 'rb')
        le6 = open('/home/stlthwl/mon_bot/img/Лена/l6.jpeg', 'rb')
        le7 = open('/home/stlthwl/mon_bot/img/Лена/l7.jpeg', 'rb')
        le8 = open('/home/stlthwl/mon_bot/img/Лена/l8.jpeg', 'rb')
        le9 = open('/home/stlthwl/mon_bot/img/Лена/l9.jpeg', 'rb')
        le10 = open('/home/stlthwl/mon_bot/img/Лена/l10.jpeg', 'rb')
        lmedia = [InputMediaPhoto(le1), InputMediaPhoto(le2), InputMediaPhoto(le3), InputMediaPhoto(le4), InputMediaPhoto(le5),
				  InputMediaPhoto(le6), InputMediaPhoto(le7), InputMediaPhoto(le8), InputMediaPhoto(le9), InputMediaPhoto(le10)]
        bot.send_media_group(message.chat.id, lmedia)
        bot.send_message(message.chat.id, 'Хотите записаться?', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Евгения':
        markup.row('Записаться к Евгении')
        markup.row('Вернуться назад')
        markup.row('В начало')
        zh1 = open('/home/stlthwl/mon_bot/img/Женя/z1.jpeg', 'rb')
        zh2 = open('/home/stlthwl/mon_bot/img/Женя/z2.jpeg', 'rb')
        zh3	= open('/home/stlthwl/mon_bot/img/Женя/z3.jpeg', 'rb')
        zh4 = open('/home/stlthwl/mon_bot/img/Женя/z4.jpeg', 'rb')
        zh5 = open('/home/stlthwl/mon_bot/img/Женя/z5.jpeg', 'rb')
        zh6 = open('/home/stlthwl/mon_bot/img/Женя/z6.jpeg', 'rb')
        zh7 = open('/home/stlthwl/mon_bot/img/Женя/z7.jpeg', 'rb')
        zh8 = open('/home/stlthwl/mon_bot/img/Женя/z8.jpeg', 'rb')
        zh9 = open('/home/stlthwl/mon_bot/img/Женя/z9.jpeg', 'rb')
        zh10 = open('/home/stlthwl/mon_bot/img/Женя/z10.jpeg', 'rb')
        zmedia = [InputMediaPhoto(zh1), InputMediaPhoto(zh2), InputMediaPhoto(zh3), InputMediaPhoto(zh4),
								  InputMediaPhoto(zh5), InputMediaPhoto(zh6), InputMediaPhoto(zh7),
								  InputMediaPhoto(zh8),InputMediaPhoto(zh9), InputMediaPhoto(zh10)]
        bot.send_media_group(message.chat.id, zmedia)
        bot.send_message(message.chat.id, 'Хотите записаться?', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Алена':
        markup.row('Записаться к Алене')
        markup.row('Вернуться назад')
        markup.row('В начало')
        br1 = open('/home/stlthwl/mon_bot/img/Алена/ale1.jpg', 'rb')
        br2 = open('/home/stlthwl/mon_bot/img/Алена/ale2.jpg', 'rb')
        br3 = open('/home/stlthwl/mon_bot/img/Алена/ale3.jpg', 'rb')
        br4 = open('/home/stlthwl/mon_bot/img/Алена/ale4.jpg', 'rb')
        br5 = open('/home/stlthwl/mon_bot/img/Алена/ale5.jpg', 'rb')
        tmedia = [InputMediaPhoto(br1), InputMediaPhoto(br2), InputMediaPhoto(br3), InputMediaPhoto(br4),
				  InputMediaPhoto(br5)]
        bot.send_media_group(message.chat.id, tmedia)
        bot.send_message(message.chat.id, 'Хотите записаться?', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


bot.polling(none_stop=True)
