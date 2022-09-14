def example():
    l = list()
    list_input(l)
    print(count_steps1(l))



def list_input(l):

    try:
        arr = list(input('Array of integers: ').split(' '))
        for i in arr:
            l.append(int(i))
    except:
        print('Invalid values of integer!')
        exit(0)


def count_steps1(a):
    count = 0
    begin = end = 0

    while sum(a) > 0:

        if end > len(a):
            begin = end = 0

        if end == len(a) or a[end] == 0:
            if end <= begin:
                begin = 0
                end = 1
                continue

            while not a[begin:end].__contains__(0):
                decrement(begin, end, a)
                count += 1
            end += 1
            begin = end
        else:
            end += 1

        if begin > end:
            begin = 0
            end = 1


    return count


def decrement(begin, end, a):
    for i in range(begin, end):
        a[i] -= 1

