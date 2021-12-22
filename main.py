import telebot

bot = telebot.TeleBot('5045518316:AAGQ_jomPjbdBNsFtz4XSLB8y0g5ROXXRN4')


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message, chat_id=None):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "🖐Привет, напиши Все команды для ознакомления🖐")
    elif message.text == "Все команды":
        bot.send_message(message.from_user.id, "Вот весь список:\n🗒Информация🗒\n🎯Упражнения🎯\n💵Поддержать💵\n🧠Факт🧠")
    elif message.text == "Информация":
        bot.send_message(message.from_user.id, "🗒Это прототип GetHealthy. Разработчик данного проекта является Бойцан "
                                               "Александр. Более подробная информация можно узнать у разработчика. "
                                               "Никнейм разработчика TooStupidToMakeNormalName🗒")
    elif message.text == "Упражнения":
        bot.send_message(message.from_user.id, "Вот список всех упражнений:\n👀Упражнения на глаза👀\n🤲Упражнения на "
                                               "руки🤲\n❤Базовые упражнения❤")
    elif message.text == "Упражнения на глаза":
        bot.send_message(message.from_user.id, "⏱Все упражнения стоит выполнять по три минуты каждой⏱")
        bot.send_photo(chat_id=1302743111,
                       photo='https://yandex.ru/images/search?pos=2&img_url=https%3A%2F%2Fwww.ochkov.net%2Fwiki%2Fstorage%2Fapp%2Fmedia%2F1.%2Fmetodika-avetisova-pri-blizorukosti%2Ff2.jpg&text=упражнение%20для%20глаз&lr=213&rpt=simage&source=wiz')
    elif message.text == "Упражнения на руки":
        bot.send_message(message.from_user.id, "⏱Все упражнения стоит выполнять по пять минут каждой⏱")
        bot.send_photo(chat_id=1302743111,
                       photo='https://yandex.ru/images/search?text=упражнения%20на%20кисти%20рук&lr=213&pos=0&img_url=https%3A%2F%2Fdiabetclinic.ru%2Fwp-content%2Fuploads%2F2021%2F02%2Fimg_16122233852414-1-1024x576.jpg&rpt=simage')
    elif message.text == "Базовые упражнения":
        bot.send_message(message.from_user.id, "⏱Упражнение нужно делать осторожно, при боли в груди стоит сделать "
                                               "небольшой перерыв и восстановить дыхание⏱")
        bot.send_photo(chat_id=1302743111,
                       photo='https://yandex.ru/images/search?text=Зарядка%20для%20офисных%20работников&source=related-duck&lr=213&pos=2&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FEoI2UeqXYAAJYCj.jpg&rpt=simage')
    elif message.text == "Факт":
        bot.send_message(message.from_user.id, "🍌Энергетик можно заменить чашкой зеленого чая и бананом🍌")
    else:
        bot.send_message(message.from_user.id, "🤷‍♂Я тебя не понимаю. Напиши Все команды.🤷‍♂")


bot.polling(none_stop=True, interval=0)
