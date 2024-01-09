import gui
import decorators


@decorators.decorator
def click_button_add():
    """
    Функция сложения
    """
    cap = check_entry()
    if isinstance(cap, tuple):
        a, b = cap
        print('Результат: ', a + b)
    else:
        return


@decorators.decorator
def click_button_min():
    """
    Функция вычитания
    """
    cap = check_entry()
    if isinstance(cap, tuple):
        a, b = cap
        print('Результат: ', a-b)
    else:
        return


@decorators.decorator
def click_button_ymn():
    """
    Функция умнежения
    """
    cap = check_entry()
    if isinstance(cap, tuple):
        a, b = cap
        print('Результат: ', a * b)
    else:
        return


@decorators.decorator
def click_button_del():
    """
    Функция деления
    """
    cap = check_entry()
    if isinstance(cap, tuple):
        a, b = cap
        if b != 0:
            print('Результат: ', a / b)
        else:
            print('некорректный ввод')
            gui.show_error()
            gui.clean()
    else:
        return


def check_entry():
    """
    Функция проверки введеных данных
    """
    char = gui.string_input.get()
    if ',' not in char:
        print('некорректный ввод')
        gui.show_error()
        gui.clean()
    else:
        lst = char.split(',')
        if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit():
            return int(lst[0]), int(lst[1])
        else:
            print('некорректный ввод')
            gui.show_error()
            gui.clean()



