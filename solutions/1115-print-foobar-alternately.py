import threading
from typing import Callable
from threading import Semaphore


def printBar():
    print("bar", end="")

def printFoo():
    print("foo",end="")


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_semaphore = Semaphore(1)
        self.bar_semaphore = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_semaphore.acquire()
            printFoo()
            self.bar_semaphore.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.bar_semaphore.acquire()
            printBar()
            self.foo_semaphore.release()


if __name__ == '__main__':
    examples = [2, 5]
    for example in examples:
        foobar = FooBar(example)

        threads = []
        threads.append(threading.Thread(target=foobar.foo, args=[printFoo]))
        threads.append(threading.Thread(target=foobar.bar, args=[printBar]))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print()