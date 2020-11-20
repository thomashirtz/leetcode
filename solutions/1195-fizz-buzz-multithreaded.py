import threading
from threading import Semaphore
from typing import Callable


def printFizz():
    print("fizz", end="")

def printBuzz():
    print("buzz",end="")

def printFizzBuzz():
    print("fizzbuzz", end="")

def printNumber(x):
    print(x, end="")


class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.sem0 = Semaphore(1)
        self.sem3 = Semaphore(0)
        self.sem5 = Semaphore(0)
        self.sem15 = Semaphore(0)

    def fizz(self, printFizz):
        for i in range(3, self.n + 1, 3):
            if i % 15:
                self.sem3.acquire()
                printFizz()
                self._release(i + 1)

    def buzz(self, printBuzz):
        for i in range(5, self.n + 1, 5):
            if i % 15:
                self.sem5.acquire()
                printBuzz()
                self._release(i + 1)

    def fizzbuzz(self, printFizzBuzz):
        for i in range(15, self.n + 1, 15):
            self.sem15.acquire()
            printFizzBuzz()
            self._release(i + 1)

    def number(self, printNumber):
        for i in range(1, self.n + 1):
            if i % 3 and i % 5:
                self.sem0.acquire()
                printNumber(i)
                self._release(i + 1)

    def _release(self, i):
        if i % 3 and i % 5:
            self.sem0.release()
        elif i % 5:
            self.sem3.release()
        elif i % 3:
            self.sem5.release()
        else:
            self.sem15.release()


if __name__ == '__main__':
    examples = [1, 3, 5, 10, 15, 22]
    for example in examples:
        fb = FizzBuzz(example)

        threads = []
        threads.append(threading.Thread(target=fb.fizz, args=[printFizz]))
        threads.append(threading.Thread(target=fb.buzz, args=[printBuzz]))
        threads.append(threading.Thread(target=fb.fizzbuzz, args=[printFizzBuzz]))
        threads.append(threading.Thread(target=fb.number, args=[printNumber]))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print()