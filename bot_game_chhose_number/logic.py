from telebot import types
import re
from random import randint


def create_main_menu():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Угадай число", callback_data="Угадай число")
    btn2 = types.InlineKeyboardButton(text="Угадай страну", callback_data="Угадай страну")
    markup.row(btn1, btn2)

    return markup


def markup_for_confirmation_country():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Да", callback_data="Да")
    btn2 = types.InlineKeyboardButton(text="Нет", callback_data="Нет")
    markup.row(btn1, btn2)
    return markup


def markup_for_confirmation_number():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Да граем", callback_data="Да граем")
    btn2 = types.InlineKeyboardButton(text="Нет не играем", callback_data="Нет не играем")
    markup.row(btn1, btn2)
    return markup


def markup_for_guess_city():
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Венесуэла.')
    btn2 = types.KeyboardButton('Вьетнам.')
    btn3 = types.KeyboardButton('Мальдивы.')
    markup.row(btn1, btn2, btn3)
    btn4 = types.KeyboardButton('Индонезия.')
    btn5 = types.KeyboardButton('Комбоджа.')
    btn6 = types.KeyboardButton('Франция.')
    markup.row(btn4, btn5, btn6)
    btn7 = types.KeyboardButton('Таиланд.')
    btn8 = types.KeyboardButton('Филиппины.')
    btn9 = types.KeyboardButton('Бора-Бора.')
    markup.row(btn7, btn8, btn9)
    return markup


def clear_markup():
    markup = types.ReplyKeyboardRemove(selective=False)
    return markup


def get_limit_number(str):
    new_str = re.split(";|,|\n| |:", str)
    return chek_limit_numbers(new_str)


def get_target(min, max):
    target = randint(int(min), int(max))
    return target


def chek_limit_numbers(lst):
    if isinstance(lst, list) and len(lst) == 2:
        if lst[0].isdigit() and lst[1].isdigit():
            if lst[0] < lst[1]:
                return lst
            if lst[0] > lst[1]:
                return [lst[1], lst[0]]
    return False


def counter():
    for i in range(1, 1000):
        yield i


# photo = open('./imaje/tay1.jpg', 'rb')