from telebot import TeleBot
from settings import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['give_feedback'])
def ask_feedback(message):
    bot.send_message(message.chat.id, 'Как бы вы оценили курс?')
    bot.register_next_step_handler(message, get_feedback)


def get_feedback(message):
    print(message.text)
    bot.send_message(message.chat.id, 'Ваш ответ записан!')
    bot.send_message(message.chat.id, 'Спасибо за участие в опросе')


bot.polling(none_stop=True)

