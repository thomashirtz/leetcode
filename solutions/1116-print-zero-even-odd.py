import threading
from typing import Callable
from threading import Semaphore

def printNumber(x):
    print(x, end="")


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.semaphore_zero = Semaphore(1)
        self.semaphore_even = Semaphore(0)
        self.semaphore_odd = Semaphore(0)

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.semaphore_zero.acquire()
            printNumber(0)
            (self.semaphore_odd if i % 2 else self.semaphore_even).release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.semaphore_even.acquire()
            printNumber(i)
            self.semaphore_zero.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.semaphore_odd.acquire()
            printNumber(i)
            self.semaphore_zero.release()


if __name__ == '__main__':
    examples = [2, 5]
    for example in examples:
        zeo = ZeroEvenOdd(example)

        threads = []
        threads.append(threading.Thread(target=zeo.zero, args=[printNumber]))
        threads.append(threading.Thread(target=zeo.even, args=[printNumber]))
        threads.append(threading.Thread(target=zeo.odd, args=[printNumber]))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print()