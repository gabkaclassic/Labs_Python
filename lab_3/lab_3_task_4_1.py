from typing import List
from random import randint as rand


def check_digit(sequence: List[int], x: int) -> object:
    for i in range(len(sequence)):
        current_sum = 0
        for j in range(i, len(sequence)):
            current_sum += sequence[j]
            if current_sum > x:
                break
            elif current_sum == x:
                return sequence[i:j+1]

    return False


def generate_sequence(length: int) -> List[int]:
    return [rand(1, 100) for i in range(length)]


while True:
    length = input('Enter number of elements in sequence: ')
    if not length.isdigit():
        print('Enter positive integer')
        continue
    seq = generate_sequence(int(length))

    print('Sequence:', seq)
    x = input('Enter X: ')
    if not x.isdigit():
        print('Enter positive integer')
        continue
    print(check_digit(seq, int(x)))
