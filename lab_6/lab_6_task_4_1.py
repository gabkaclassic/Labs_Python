from threading import Thread, Barrier
from requests import get
from time import time

urls = [
    "https://orioks.miet.ru",
    "https://www.miet.ru",
    "https://tproger.ru",
    "https://habr.com",
    "https://github.com",
    "https://www.w3schools.com/",
    "https://www.speedcoder.net",
    "https://javarush.ru",
    "https://coderlessons.com",
    "https://typerun.top"
]

barrier = Barrier(len(urls) + 1)


def download_page(url):
    print("Were downloaded", len(get(url).text), "characters from", url)


def one_thread():
    start_time = time()
    for url in urls:
        download_page(url)
    print('One thread:', time() - start_time)
    barrier.reset()


def download_and_wait(url):
    download_page(url)
    barrier.wait()


def multi_thread():
    start_time = time()

    for url in urls:
        Thread(target=download_and_wait, args=[url]).start()

    barrier.wait()

    print('Multi thread:', time() - start_time)


def start():
    one_thread()
    multi_thread()
