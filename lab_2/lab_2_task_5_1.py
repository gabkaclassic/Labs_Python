from os.path import getsize as size
from os import listdir as files
from os.path import join

def run():
    limits = input_limits()
    print('Number of files which has size between {0} and {1} KB: {2}'.format(limits[0], limits[1], count_files(limits)))

def count_files(limits):
    count = 0
    path = './data/example'
    for file in files(path):
        if int(size(join(path, file))/1024) in range(limits[0], limits[1]):
            count += 1

    return count

def input_limits():
    left = input('Enter the left border: ')
    while not (left.isdigit() and int(left) > 0):
        left = input('Enter the left border: ')
    left = int(left)
    right = input('Enter the right border: ')
    while not (right.isdigit() and int(right) > left):
        right = input('Enter the right border: ')
    right = int(right)

    return [left, right]