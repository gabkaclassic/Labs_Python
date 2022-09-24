from typing import Tuple


def reducer(fraction: Tuple[int, int]) -> Tuple[int, int]:
    n, m = fraction
    for i in range(1, min(fraction) + 1):
        if fraction[0] % i == 0 and fraction[1] % i == 0:
            n //= i
            m //= i

    return n, m


def enter_fraction():
    while True:
        n = input('Enter n: ').strip()
        if not n.isdigit():
            print('Please, only integer')
        else:
            break
    n = int(n)
    while True:
        m = input('Enter m: ').strip()
        if not m.isdigit() or int(m) == 0:
            print('Please, only integer which not equals 0')
        else:
            break
    m = int(m)

    return n, m


while True:
    result = reducer(enter_fraction())
    print(result[0], '/', result[1])
    print(result)
