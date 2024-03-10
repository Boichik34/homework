# import telebot as tb
# import viewbot as vb


# TOKEN = "..."

# bot = tb.TeleBot(TOKEN, parse_mode="MARKDOWN")

# @bot.message_handler(commands=["start"])
# def start_handler(message):
#     markup = vb.create_main_menu()
#     bot.send_message(message.chat.id, "Hello!", reply_markup=markup)


# @bot.callback_query_handler(func=lambda call: call.data == "label_some")
# def btn_some_callback(call):
#     bot.send_message(call.message.chat.id, "label some")

# if __name__ == "__main__":
#     bot.infinity_polling()

import telebot
import viewbot
token = "6356460604:AAHppVm6NbTsItuRUnRHqPNuzJIckVz_7-Y"

bot = telebot.TeleBot(token)

target = None
left = None
right = None

is_game_playing = False


def check_for_number_and_not_state(message) -> bool:
    global is_game_playing
    return True if message.text.isdigit() and not is_game_playing else False

def check_for_number_and_state(message) -> bool:
    global is_game_playing
    return True if message.text.isdigit() and is_game_playing else False

def reset_state_game():
    global left
    global right
    global target

    global is_game_playing

    target = None
    left = None
    right = None

    is_game_playing = False

@bot.message_handler(commands=['start'])
def hello_handler(message):
    hello_text = 'здравствуйте, я бот крот, и я сегодня буду вас развлекать'

    markup = viewbot.create_hello_menu()

    bot.send_message(message.chat.id, hello_text, reply_markup=markup)

@bot.message_handler(func=check_for_number_and_not_state)
def number_handler(message):
    global left
    global right

    if left == None:
        left = int(message.text) 
        return 
    
    if right == None:
        right = int(message.text)

    if left != None and right != None:
        markup = viewbot.create_yes_or_no_menu()
        bot.send_message(message.chat.id, 'вы успешно установили левую и правую границы')
        bot.send_message(message.chat.id, 'играем?', reply_markup=markup)


@bot.message_handler(func=check_for_number_and_state)
def search_target_number_handler(message):
    global target
    some_number = int(message.text)
    result_text = ''

    if some_number == target:
        reset_state_game()
        result_text = "Win!"
    elif some_number > target:
        result_text = ">"
    else:
        result_text = "<"

    bot.send_message(message.chat.id, result_text)

@bot.callback_query_handler(func=lambda call: call.data == "start_game")
def start_game_callback(call):
    game_info_text = 'игра - угадай число\nя загадаю число,а вы угадаете его.\ninput limits left and right'
    bot.send_message(call.message.chat.id,game_info_text)

@bot.callback_query_handler(func=lambda call: call.data == "yes")
def yes_callback(call):
    global target
    global left
    global right
    global is_game_playing

    is_game_playing = True

    import random

    target = random.randint(left, right)

    bot.send_message(call.message.chat.id, f"я загадал число, жду твоих вариантов (это число {target})")

if __name__ == "__main__":
    bot.infinity_polling()