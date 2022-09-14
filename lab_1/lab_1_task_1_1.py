
def example():
    s = ''
    while len(s) <= 0:
        s = input('S-string: ').lower()
    x = input('virus-string: ').lower()

    while s.__contains__(x):
        s = s.replace(x, '')
    print('Answer: ', s if not len(s) == 0 else '(Empty string)')