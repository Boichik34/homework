from telebot import types

def create_hello_menu():
    markup = types.InlineKeyboardMarkup()

    btn_game_start = types.InlineKeyboardButton(text="начать игру",callback_data='start_game')
    
    markup.add(btn_game_start)

    return markup

def create_yes_or_no_menu():
    markup = types.InlineKeyboardMarkup()

    btn_yes = types.InlineKeyboardButton(text='да', callback_data='yes')
    btn_no = types.InlineKeyboardButton(text='нет', callback_data='no')

    markup.add(btn_no)
    markup.add(btn_yes)

    return markup

def create_clean_menu():
    pass