from functools import wraps
from threading import BoundedSemaphore
from threading import Thread

def thread_decorator(semaphore):
    if isinstance(semaphore, MyBoundedSemaphore):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                while True:
                    if semaphore.acquire(blocking=False):
                        print('semaphore._value == %s' % len(semaphore))
                        thread = Thread(target=func, args=args, kwargs=kwargs, daemon=False)
                        thread.start()
                        break

            return wrapper

        return decorator


class MyBoundedSemaphore(BoundedSemaphore):
    def __init__(self, value=1):
        super(MyBoundedSemaphore, self).__init__(value=value)

    def __len__(self):
        return self._value