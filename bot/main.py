from telebot import TeleBot, types

from bot.models import Feedback
from bot.repositories import save_feedback
from settings import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['give_feedback'])
def ask_course(message):
    courses = types.InlineKeyboardMarkup()
    networks = types.InlineKeyboardButton(text='Компьютерные сети', callback_data='networks')
    python = types.InlineKeyboardButton(text='Python Pro', callback_data='python')
    courses.add(networks, python)

    bot.send_message(message.chat.id, 'В каком курсе вы участвовали?', reply_markup=courses)


@bot.callback_query_handler(func=lambda answer: answer.data)
def ask_feedback(answer):
    course = answer.data
    bot.answer_callback_query(answer.id)
    bot.send_message(answer.message.chat.id, 'Как бы вы оценили курс?')
    bot.register_next_step_handler(answer.message, get_feedback, course=course)


def get_feedback(message, **kwargs):
    new_feedback = Feedback(
        course=kwargs.get('course'),
        content=message.text
    )

    save_feedback(new_feedback)
    bot.send_message(message.chat.id, 'Ваш ответ записан!')
    bot.send_message(message.chat.id, 'Спасибо за участие в опросе')


bot.polling(none_stop=True)

