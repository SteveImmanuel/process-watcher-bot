import os
import logging
import telebot
from telebot.types import Message

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
telebot.logger.setLevel(logging.INFO)

@bot.message_handler(commands=['info'])
def send_welcome(message: Message):
    chat_id = message.chat.id
    telebot.logger.info(f'Sending info message to {chat_id}')
    bot.send_message(chat_id, f'Chat ID: {chat_id}')

def push_message(chat_id, message):
    telebot.logger.info(f'Sending push message to {chat_id}')
    bot.send_message(chat_id, message)

if __name__ == '__main__':
    telebot.logger.info('Bot is running')
    bot.infinity_polling()