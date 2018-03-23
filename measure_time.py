from functools import wraps
import time
import os


def measure_time(func):
    """
    引数に取った関数の時間計測をする
    :param func: 時間計測したい関数
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start
        print(str(func.__name__) + "は" + str(elapsed_time) + "秒かかりました" + os.linesep)
        return result
    return wrapper
