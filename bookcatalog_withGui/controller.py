import eel
from logic.logic import a


@eel.expose
def handler() -> int:
    print('handler')
    return a()
