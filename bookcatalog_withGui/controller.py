import eel


@eel.expose
def handler(name, autor, genre, year) -> int:
    from logic.catalog_app import add_book
    id = add_book(name, autor, genre, year)
    return id


@eel.expose
def get_list():
    from logic.catalog_app import get_list
    return get_list()


