from threading import *
from functools import wraps
import time


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


semaphore = MyBoundedSemaphore(5)


@thread_decorator(semaphore)
def exex(n):
    print(str(n))
    time.sleep(2)
    semaphore.release()


class CJ(object):
    semaphore = MyBoundedSemaphore(5)

    def run(self):
        for i in range(10):
            CJ.exex(i)

    @classmethod
    @thread_decorator(semaphore)
    def exex(cls,n):
        time.sleep(1)
        print(str(n))
        cls.semaphore.release()



# class Myclassmethod(classmethod):
#     def __call__(self, *args, **kwargs):
#         return self.




if __name__ == '__main__':
    CJ().run()
