from auth_data import token
import telebot
import ex_wb

def make_telegrambot(token):
        bot = telebot.TeleBot(token)

        #@bot.message_handler()
        @bot.message_handler(commands=["start"])
        def start_message(message):
                bot.send_message(message.chat.id, 'Привет! Я покажу тебе наушники со скидками. Введи номер страницы для поиска (от 1 до 100):')
        
        
        #оставь пока, возможно пригодится.
        @bot.message_handler(content_types=['text'])
        def send_message(message):
                #if message.text.lower() == 'go':
                        #bot.send_message(message.chat.id, 'Введите номер страницы для поиска:')
                #if message.text.lower() in range(1. 101):
                if message.text.lower() in '123456789':
                                #try:
                        num_page = message
                        #num_page = input()
                        #print(num_page)
                        bot.send_message(message.chat.id, num_page)
                                                #bot.send_message(chat_id=message.chat.id, "123")
                                                #bot.send_message(message.chat.id, "123")
                                                #num_page = message
                                                #x = 1
                                                #bot.send_message(message.chat.id, f'Введите номер страницы для поиска:{num_page}')
                                                #res = ex_wb.common_func(num_page)
                                                #bot.send_message(message.chat.id, str(ex_wb.common_func(num_page)))
                                                #bot.send_message(message.chat.id, '1111')
                                        
                                #except Exception as ex:
                                        #print(ex)
                                        #bot.send_message(message.chat.id, 'Ошибочка...')

                else:
                        bot.send_message(message.chat.id, 'Что-то не то. Напиши мне в ответ "sale"')

        bot.polling()
        #bot.stop_bot()

if __name__ == '__main__':
        make_telegrambot(token)

