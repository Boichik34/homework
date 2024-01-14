import re


class Note:
    def __init__(self, name, note):
        self.name = name
        self.note = note


class ListNotes:

    def __init__(self, lst):
        self.list_notes = lst

    @staticmethod
    def get_list_note():
        return list_notes.list_notes

    def add_in_list(self, note):
        self.list_notes[note.name] = note.note

    @staticmethod
    def del_note(name):
        del list_notes.list_notes[name]


class App:

    @staticmethod
    def add_note(name, new_note):
        note = Note(name, new_note)
        list_notes.add_in_list(note)
        App.save_note(note)
        return list_notes.list_notes

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

    @staticmethod
    def del_note(key):
        ListNotes.del_note(key)
        App.save_change(key)

    @staticmethod
    def save_change(key1, new_value=''):
        lst = App.get_list()
        file = open("text.txt", "w", encoding="utf8")
        for key, value in lst.items():
            if key != key1:
                info = f'{key}, {value}\n'
                file.write(info)
        file.close()


    @staticmethod
    def save_note(note):
        info = f'{note.name}, {note.note}\n'
        file = open("text.txt", "a", encoding="utf8")
        file.write(info)
        file.close()


list_notes = ListNotes(App.get_list())
