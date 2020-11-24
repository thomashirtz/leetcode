import threading
from typing import Callable
from threading import Semaphore


def printFirst():
    print("first", end="")

def printSecond():
    print("second", end="")

def printThird():
    print("third", end="")


class Foo:
    def __init__(self):
        self.semaphore_second = Semaphore(0)
        self.semaphore_third = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.semaphore_second.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.semaphore_second.acquire()
        printSecond()
        self.semaphore_third.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.semaphore_third.acquire()
        printThird()


if __name__ == '__main__':

    foo = Foo()

    threads = []
    threads.append(threading.Thread(target=foo.third, args=[printThird]))
    threads.append(threading.Thread(target=foo.second, args=[printSecond]))
    threads.append(threading.Thread(target=foo.first, args=[printFirst]))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print()
