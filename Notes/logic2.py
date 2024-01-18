import re


class Note:
    def __init__(self, name, note):
        self.__name = name
        self.__note = note

    def get_name(self):
        return self.__name

    def get_note(self):
        return self.__note


class List:

    def __init__(self, lst):
        self.__list_notes = lst

    def get_list_note(self):
        return self.__list_notes

    def add_in_list(self, note):
        self.__list_notes[note.get_name()] = note.get_note()

    def del_note(self, name):
        del self.__list_notes[name]


class App:

    @classmethod
    def add_note(cls, name, new_note):
        note = Note(name, new_note)
        list_notes.add_in_list(note)
        cls.save_note(note)
        return list_notes.get_list_note()

    @staticmethod
    def get_list():
        file = open("text.txt", "r", encoding="utf8")
        catalog = file.read()
        file.close()
        lst = {}
        lst_0 = catalog.split("\n")
        for el in lst_0:
            lst_1 = re.split(", |;", el)
            for i in range(0, len(lst_1)-1, 2):
                lst[lst_1[i]] = lst_1[i+1]
        return lst

    @classmethod
    def del_note(cls, key):
        list_notes.del_note(key)
        cls.save_change(key)

    @staticmethod
    def save_change(key1, new_value=''):
        lst = list_notes.get_list_note()
        file = open("text.txt", "w", encoding="utf8")
        for key, value in lst.items():
            if key != key1:
                info = f'{key}, {value}\n'
                file.write(info)
        file.close()

    @staticmethod
    def save_note(note):
        info = f'{note.get_name()}, {note.get_note()}\n'
        file = open("text.txt", "a", encoding="utf8")
        file.write(info)
        file.close()


list_notes = List(App.get_list())
