import math as m


def run():
    k = input('Enter positive integer: ')

    while not (k.isdigit() and (int(k) in range(1, 10000)) and m.ceil(int(k)) == int(k)):
        k = input('Enter positive integer: ')
    k = int(k)

    print(search_magic_digit(k))


def search_magic_digit(k):
    count = 0
    d = 10
    while count < k:
        d += 9
        if is_magic(d):
            count += 1
    return d


def is_magic(d):
    s = 0
    while d > 0:
        s += d % 10
        d //= 10
        if s > 10:
            return False

    return s == 10
