def example():
    l = list()
    list_input(l)
    print(count_steps(l))

def list_input(l):
    try:
        arr = list(input('Array of integers: ').split(' '))
        for i in arr:
            l.append(int(i))
    except:
        raise Exception("Invalid values of integer!")

def count_steps(a):
    count = 0
    begin = end = 0

    while sum(a) > 0:
        if end == len(a) or a[end] == 0:
            m = min(a[begin:end]) if begin != end else a[begin]
            decrement(begin, end, m, a)
            count += m
            end += 1
            begin = end
            if end >= len(a):
                begin = end = 0
        else:
            end += 1

    return count

def decrement(begin, end, min, a):
    for i in range(begin, end):
        a[i] -= min