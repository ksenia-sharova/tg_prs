from auth_data import token
import telebot
import ex_wb
import ex_wb_brend
from telebot import types

def make_telegrambot(token):
        bot = telebot.TeleBot(token)


        @bot.message_handler(commands=["start"])
        def start_message(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            but_start = types.KeyboardButton('Покажи все скидки')
            but_brend = types.KeyboardButton('Хочу найти по бренду')
            markup.add(but_start, but_brend)
            bot.send_message(message.chat.id, "Привет! Показать тебе скидки на наушники?", reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def send_message(message):
            if message.text == 'Покажи все скидки':
                msg = bot.reply_to(message, 'Введи номер страницы для поиска (от 1 до 100):')
                bot.register_next_step_handler(msg, send_results)
            elif message.text == 'Хочу найти по бренду':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                #xiomi = types.KeyboardButton('Xiaomi')
                apple = types.KeyboardButton('Apple')
                jbl = types.KeyboardButton('JBL')
                honor = types.KeyboardButton('Honor')
                samsung = types.KeyboardButton('Samsung')
                huawei = types.KeyboardButton('Huawei')
                main_menu = types.KeyboardButton('Вернуться в главное меню')
                #markup.add(xiomi, apple, jbl, honor,samsung, huawei, main_menu)
                markup.add(apple, jbl, honor,samsung, huawei, main_menu)
                msg = bot.send_message(message.chat.id, 'Выбери бренд', reply_markup= markup)
                bot.register_next_step_handler(msg, send_brend_results)
            elif message.text == 'Вернуться в главное меню':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                but_start = types.KeyboardButton('Покажи все скидки')
                but_brend = types.KeyboardButton('Хочу найти по бренду')
                markup.add(but_start, but_brend)
                bot.send_message(message.chat.id, "Мы вернулись в главное меню", reply_markup=markup)

        def send_results(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            main_menu = types.KeyboardButton('Вернуться в главное меню')
            markup.add(main_menu)
            lst_num = list(map(str,range(1, 101)))
            if message.text in lst_num:
                    a = str(ex_wb.common_func(message.text))
                    bot.send_message(message.chat.id, a)
            #bot.send_message(message.chat.id, reply_markup=markup)
            else:
                    bot.send_message(message.chat.id, 'Что-то не то. Укажи НОМЕР страницы')
            bot.send_message(message.chat.id,'?', reply_markup=markup)

        def send_brend_results(message):
            #lst_brand = ['Xiaomi','Apple', 'JBL', 'Honor', 'Samsung', 'Huawei']
            lst_brand = ['Apple', 'JBL', 'Honor', 'Samsung', 'Huawei']
            if message.text in lst_brand:
                for i in range(1,4):
                    name_df = ex_wb_brend.connect_func(i)
                    b = str(ex_wb_brend.chek_brend(name_df, message.text))
                    bot.send_message(message.chat.id, b)


        bot.polling(none_stop=True)

if __name__ == '__main__':
        make_telegrambot(token)
