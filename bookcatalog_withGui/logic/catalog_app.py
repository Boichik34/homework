import sys
sys.path.append('..')
from logic.booook import Book


def get_list():
    return extract_list()


def a():
    return 'return from logic.logic.a'


def add_book(name, autor, genre, date_of_publication, is_read=False) -> bool:

    book = Book(name, autor, genre, date_of_publication, is_read)

    dictionary = {
        'name': book.get_name(),
        'autor': book.get_autor(),
        'genre': book.get_genre(),
        'year': book.get_date_of_publication(),
        'is_done': book.get_is_read()
                  }
    id = kick_to_save(dictionary)
    return id


def kick_to_save(dictionary, metod='json'):
    if metod == 'json':
        id = save_into_json(dictionary)
    return id

def change_save_metod():
    return 'json'


def save_into_json(dictionary):
    import json
    data = extract_list()
    id = get_id()
    data[id] = dictionary
    with open('file.json', 'w') as file:
        json.dump(data, file, indent=4)
        return id

def extract_list():
    import json
    with open('file.json', 'r') as file:
        data = json.load(file)
    return data


def get_id():
    import json
    with open('id.json', 'r') as file:
        dic = json.load(file)
        id = dic['id'] + 1
        dic["id"] = id
    with open('id.json', 'w') as file:
        json.dump(dic, file)
    return id
