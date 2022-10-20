from multiprocessing import Pool
from random import randint as rand
from time import time


def generate_sequence(N):
    return [rand(1, 100) for _ in range(N)]


def rij(ij):
    (i, j) = ij
    return 1 / (1 + abs(P[i] - Q[j]))


def without_module():
    N = len(P)
    start_time = time()
    for i in range(N):
        for j in range(N):
            rij((i, j))
    print('Without module:', time() - start_time, 'seconds')


def with_module():
    start_time = time()
    pool = Pool(8)
    pool.map(rij, [(i, j) for i in range(N) for j in range(N)])
    print('With module:', time() - start_time)


N = 5000
P = generate_sequence(N)
Q = generate_sequence(N)


def start():
    # without_module()
    with_module()
