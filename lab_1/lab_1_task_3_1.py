def example():
    d = dict()
    input_dict(d)
    show_unique_values(d)


def input_dict(d):
    n = input('Number of rows: ')
    while not n.isdigit():
        n = input('Number of rows: ')
    n = int(n)

    for i in range(n):
        inf = input('(' + str(i) + ') ').split(' ')
        while not (len(inf) == 3 and inf[0].isdigit() and inf[1].isdigit() and inf[2].isdigit()):
            print('Enter three integer values, please:')
            inf = input('(' + str(i) + ') ').split(' ')

        ticket = inf[0] + ' ' + inf[1]
        d.setdefault(ticket, set())
        d.get(ticket).add(inf[2])

def show_unique_values(d):
    for k in d.keys():
        print(k, '-', len(d.get(k)))






