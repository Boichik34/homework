import telebot
import logic
from  player_and_game import Player, PlayGuessNumber, PlayGuessCity

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

TARGET = None
game_guess_city = None
min = None
max = None
player = None
game = None
country_list = ['Венесуэла.', 'Вьетнам.', 'Мальдивы.', 'Индонезия.',
                'Комбоджа.', 'Франция.', 'Филиппины.', 'Бора-Бора.']


@bot.message_handler(commands=["start", "back"])
def start_handler(message):
    global player
    if not player:
        player = Player(message.from_user.id)
    markup = logic.create_main_menu()
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name},"
                                      f"Твой текущий рекорд:  {player.get_record()}! \n"
                                      f"Во что хочешь сыграть?", reply_markup=markup)


def restart(message):
    markup = logic.create_main_menu()
    bot.send_message(message.chat.id, 'Попробушь еще раз?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["Угадай число",
                                                            "Угадай страну"])
def chose_game(call):
    if call.data == "Угадай страну":
        markup = logic.markup_for_confirmation_country()
        bot.send_message(call.message.chat.id, "У тебя будет пять попыток угадать"
                                               "страну по фотографии. Поехали?",
                         reply_markup=markup)
    if call.data == "Угадай число":
        markup = logic.markup_for_confirmation_number()
        bot.send_message(call.message.chat.id, "Попробуй угадать число"
                                               "в заданном тобой диапазоне,"
                                               "который будет сокращаться"
                                               "до твоей неверной попытки.",
                         reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ["Да граем",
                                                            "Нет не играем",
                                                            "Нет"])
def btn_some_callback(call):
    if call.data == "Да граем":
        bot.send_message(call.message.chat.id, "Выберите два числа, которые"
                                               "будут минимальной и максимальной"
                                               "границей поиска")
    elif call.data == "Нет не играем" or call.data == "Нет":
        bot.send_message(call.message.chat.id, "Жаль")
        markup = logic.create_main_menu()
        bot.send_message(call.message.chat.id, "Во что поиграем?",
                         reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ["Да"])
def chose_play_in_city(call):
    global game_guess_city
    game_guess_city = PlayGuessCity()
    photo = open(f'./image/tay{game_guess_city.get_game_step()}.jpg', 'rb')
    bot.send_photo(call.message.chat.id, photo, "Попробуй угадать без"
                                                "подсказки. Напиши свой вариант.")


def show_next_picture(message):
    global game_guess_city
    game_guess_city.set_game_step()
    photo = open(f'./image/tay{game_guess_city.get_game_step()}.jpg', 'rb')
    markup = logic.markup_for_guess_city()
    bot.send_photo(message.chat.id, photo, "Твой выбор?", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def input_limit_handler(message):
    global game
    global game_guess_city
    global player

    if game_guess_city:
        if message.text.lower() in ['тайланд', 'таиланд', 'thailand',
                                    'иордания', 'jordan', 'таиланд.']:
            record = game_guess_city.calculate_record()
            player.save_record(record)
            markup = logic.clear_markup()
            bot.send_message(message.chat.id, f"Браво!!!\n"
                                              f"Твой рекорд увеличился на"
                                              f"{record} баллов."
                                              f"Теперь он равен {player.get_record()}",
                             reply_markup=markup)
            game_guess_city = None
            return restart(message)
        else:
            if game_guess_city.get_game_step() < 5:
                bot.send_message(message.chat.id, 'Ошибочка, посмотри'
                                                  'следующие картинки.')
                return show_next_picture(message)
            else:
                markup = logic.clear_markup()
                bot.send_message(message.chat.id, 'Это был Таиланд',
                                 reply_markup=markup)
                return restart(message)
    if not game:
        str = message.text
        limit_number = logic.get_limit_number(str)
        if limit_number:
            global TARGET
            TARGET = logic.get_target(limit_number[0], limit_number[1])

            global min
            min = limit_number[0]

            global max
            max = limit_number[1]

            game = PlayGuessNumber(min, max)
            print_input(message, min, max)
        else:
            repeat_input(message)

    else:

        num = int(message.text)
        if num == TARGET:
            TARGET = None
            is_game_guess_number = False
            min = None
            max = None
            markup = logic.create_main_menu()
            game.set_count_attempt()
            record = game.calculate_record()
            player.save_record(record)
            bot.send_message(message.chat.id, f"ПОБЕДА!!! Тебе потребовалось {game.get_count_attempt()}"
                                              f" попыток из {game.get_perfect_count_attempt()} возможных\n"
                                              f"Твой рекорд увеличился на {record}."
                                              f"Теперь твой рекорд: {player.get_record()}.\n"
                                              f"В какую игру сыграешь теперь?", reply_markup=markup)
            game = None
        elif num > TARGET:
            game.set_count_attempt()
            max = num
            print_input(message, min, max)
        elif num < TARGET:
            game.set_count_attempt()
            min = num
            print_input(message, min, max)


def print_input(message, min, max):
    bot.send_message(message.chat.id, f"Введите число"
                                      f"от {min} до {max}")


def repeat_input(message):
    bot.send_message(message.chat.id, "Неверный ввод. Введите два"
                                      "числа через пробел или запятую")


bot.infinity_polling()
