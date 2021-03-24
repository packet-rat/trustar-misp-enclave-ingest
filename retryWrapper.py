from functools import wraps
import time


def retry(func, max_retry=5, backoff=300):
    @wraps(func)
    def wrapper(*args, **kwargs):
        retExc = None
        for i in range(max_retry):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                retExc = e
                time.sleep(backoff)
        raise retExc

    return wrapper
