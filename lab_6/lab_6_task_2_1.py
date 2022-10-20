from multiprocessing import Semaphore
from threading import Thread
from time import sleep

semaphore = Semaphore(1)


def lock(number):
    while True:
        semaphore.acquire()
        print('Thread:', number)
        sleep(0.5)
        semaphore.release()


for i in range(10):
    thread = Thread(
        target=lock,
        args={i}
    )
    thread.start()
