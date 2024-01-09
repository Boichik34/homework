import time
from functools import wraps
import time

def decorator(funk):
    @wraps(funk)
    def wraper():
        print(time.ctime())
        print(funk.__doc__)
        funk()
        print('-' * 30)
    return wraper



