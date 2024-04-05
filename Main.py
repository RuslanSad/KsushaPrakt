import telebot
from telebot import types
import webbrowser

API_TOKEN = "7182159674:AAF9zOAfpz1ntfTT8OgLiaRjhWq42iN5XzU"
bot = telebot.TeleBot(API_TOKEN)

keyboard_main = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_specialties = types.KeyboardButton("Перечень специальностей")
button_info = types.KeyboardButton("Контакты")
button_website = types.KeyboardButton("Сайт колледжа")
button_accept = types.KeyboardButton("Подать документы")
keyboard_main.add(button_specialties, button_accept, button_info, button_website)

keyboard_specialties = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
specialties = [
    "Компьютерные системы и комплексы",
    "Информационные системы и программирование",
    "Разработка электронных устройств и систем",
    "Биохимическое производство",
    "Технология продуктов питания из растительного сырья",
    "Экологическсая безопасность природных комплексов",
    "Товароведение и экспертиза качества потребительских товаров",
    "Финансы",
    "Банковское дело",
    "Право и судебное администрирование",
    "Документационное обеспечение управления и архивоведение",
    "Назад",
]
for spec in specialties:
    button = types.KeyboardButton(spec)
    keyboard_specialties.add(button)

keyboard_call = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
number = [
    "Директор колледжа, приемная (секретарь)",
    "Вахта колледжа",
    "Зав. директора по учебной работе, учебная часть",
    "Зам.  директора по воспитательной работе, психолог",
    "Методический кабинет",
    "Отдел кадров",
    "Главный бухгалтер, бухгалтерия",
    "Заочное отделение",
    "Зам. директора по общим вопросам и БОП",
    "Зав. общежитием, вахта общежития",
    "E-MAIL",
    "Назад",
]
for n in number:
    button = types.KeyboardButton(n)
    keyboard_call.add(button)

keyboard_sent = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
sent = ["Отправить", "Отменить"]
for n in sent:
    button = types.KeyboardButton(n)
    keyboard_sent.add(button)

keyboard_info = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_back_info = types.KeyboardButton("Назад")
keyboard_info.add(button_back_info)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Перечень специальностей":
        bot.send_message(
            message.chat.id,
            "Выберите специальность:",
            reply_markup=keyboard_specialties,
        )
    elif message.text == "Контакты":
        bot.send_message(
            message.chat.id, "Выберите контакт:", reply_markup=keyboard_call
        )
    elif message.text == "Подать документы":
        bot.send_message(
            message.chat.id,
            "Для того чтобы подать документы , вам нужно подать следующие данные:\n1)Ксерокопию \
                         паспорта, документа об образовании, заявления.\n2)ФИО\n3)Номер телефона\n4)Ваш телеграмм\n\
                         *Все данные нужно заполнить как в примере.*",
            reply_markup=keyboard_info,
            parse_mode="Markdown",
        )
        bot.send_photo(message.chat.id, open("guide.jpg", "rb"))
    elif message.text[:2] == "2)":
        bot.send_message(
            message.chat.id,
            'Если вы хотите отправить документы, нажмите кнопку "Отправить" ,иначе нажмите кнопку\
                          "Отменить"',
            reply_markup=keyboard_sent,
        )
    elif message.text == "Отправить":
        bot.forward_message("@thtkinfobot", message.chat.id, message.id - 2)
        bot.forward_message("@thtkinfobot", message.chat.id, message.id - 5)
        bot.forward_message("@thtkinfobot", message.chat.id, message.id - 4)
        bot.forward_message("@thtkinfobot", message.chat.id, message.id - 3)
        bot.send_message(
            message.chat.id,
            "Ваши документы успешно отправлены!В скором времени с вами свяжутся.",
        )
        bot.send_message(
            message.chat.id, "Выберите действие:", reply_markup=keyboard_main
        )

    elif message.text == "Директор колледжа, приемная (секретарь)":
        bot.send_contact(
            message.chat.id,
            "+74822782070",
            "Директор колледжа, приемная (секретарь)",
            reply_markup=keyboard_call,
        )
    elif message.text == "Вахта колледжа":
        bot.send_contact(
            message.chat.id,
            "+74822347530",
            "Вахта колледжа",
            reply_markup=keyboard_call,
        )
    elif message.text == "Зав. директора по учебной работе, учебная часть":
        bot.send_contact(
            message.chat.id,
            "+74822782060",
            "Зав. директора по учебной работе, учебная часть",
            reply_markup=keyboard_call,
        )
    elif message.text == "Зам.  директора по воспитательной работе, психолог":
        bot.send_contact(
            message.chat.id,
            "+74822781990",
            "Зам.  директора по воспитательной работе, психолог",
            reply_markup=keyboard_call,
        )
    elif message.text == "Методический кабинет":
        bot.send_contact(
            message.chat.id,
            "+74822786100",
            "Методический кабинет",
            reply_markup=keyboard_call,
        )
    elif message.text == "Отдел кадров":
        bot.send_contact(
            message.chat.id, "+74822781990", "Отдел кадров", reply_markup=keyboard_call
        )
    elif message.text == "Главный бухгалтер, бухгалтерия":
        bot.send_contact(
            message.chat.id,
            "+74822786300",
            "Главный бухгалтер, бухгалтерия",
            reply_markup=keyboard_call,
        )
    elif message.text == "Заочное отделение":
        bot.send_contact(
            message.chat.id,
            "+74822782061",
            "Заочное отделение",
            reply_markup=keyboard_call,
        )
    elif message.text == "Зам. директора по общим вопросам и БОП":
        bot.send_contact(
            message.chat.id,
            "+74822786100",
            "Зам. директора по общим вопросам и БОП",
            reply_markup=keyboard_call,
        )
    elif message.text == "Зав. общежитием, вахта общежития":
        bot.send_contact(
            message.chat.id,
            "+74822359604",
            "Зав. общежитием, вахта общежития",
            reply_markup=keyboard_call,
        )
    elif message.text == "E-MAIL":
        bot.send_message(
            message.chat.id, "Почта колледжа: thtk@list.tu", reply_markup=keyboard_call
        )
    elif message.text == "Компьютерные системы и комплексы":
        webbrowser.open(
            "https://www.leocdn.ru/uploadsForSiteId/202357/content/a4c63b99-1887-4993-8be6-4514e4e34768.docx"
        )
    elif message.text == "Информационные системы и программирование":
        webbrowser.open(
            "https://www.leocdn.ru/uploadsForSiteId/202357/content/3d0202ea-a32f-419a-8085-ca23393ffbc6.docx"
        )
    elif message.text == "Разработка электронных устройств и систем":
        webbrowser.open(
            "https://www.leocdn.ru/uploadsForSiteId/202357/content/2f749f7c-08da-434c-a3d6-b9b2c684682f.docx"
        )
    elif message.text == "Биохимическое производство":
        webbrowser.open(
            "https://www.leocdn.ru/uploadsForSiteId/202357/content/17b3336d-ac3e-4552-b971-7ec3085ae22f.docx"
        )
    elif message.text == "Технология продуктов питания из растительного сырья":
        webbrowser.open(
            "https://www.leocdn.ru/uploadsForSiteId/202357/content/b0a00fdb-9b68-46c6-a866-9922a4252ab1.docx"
        )
    elif message.text == "Экологическсая безопасность природных комплексов":
        webbrowser.open(
            "https://www.leocdn.ru/uploadsForSiteId/202357/content/a6ea723b-6274-471a-af3b-b4d1d22bd8f0.docx"
        )
    elif message.text == "Товароведение и экспертиза качества потребительских товаров":
        webbrowser.open(
            "https://www.leocdn.ru/uploadsForSiteId/202357/content/1eb7d9a8-a7ba-451f-946e-882b8a6a0858.docx"
        )
    elif message.text == "Финансы":
        webbrowser.open(
            "https://www.leocdn.ru/uploadsForSiteId/202357/content/4386ccd1-467d-4f25-ab68-dca6731f0160.docx"
        )
    elif message.text == "Банковское дело":
        webbrowser.open(
            "https://www.leocdn.ru/uploadsForSiteId/202357/content/69f5c1c8-92a7-4433-b9b7-60caa17fa3fa.docx"
        )
    elif message.text == "Право и судебное администрирование":
        webbrowser.open(
            "https://www.leocdn.ru/uploadsForSiteId/202357/content/fc311f98-13db-4d58-94d2-38859d8105b7.docx"
        )
    elif message.text == "Документационное обеспечение управления и архивоведение":
        webbrowser.open(
            "https://www.leocdn.ru/uploadsForSiteId/202357/content/1e27ce61-5054-4210-bfb8-a3f90e30129c.docx"
        )
    elif message.text == "Сайт колледжа":
        webbrowser.open("https://thtk-tver.ru/")
    elif message.text == "Назад":
        bot.send_message(
            message.chat.id, "Выберите действие:", reply_markup=keyboard_main
        )
    else:
        bot.send_message(
            message.chat.id, "Выберите действие:", reply_markup=keyboard_main
        )


bot.polling()
