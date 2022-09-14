def run():
    list_IP = list()
    read_IP(list_IP)
    mask = input_mask()
    write_solved_IP(list_IP, mask)


def write_solved_IP(list_ip, mask=''):
    with open('./data/ip_solve.log', 'w+') as f:
        for ip in list_ip:
            solve = multiply(ip, mask)
            f.write(solve + '\n')


def multiply(ip, mask):
    ip = list(map(lambda x: int(x), ip.split('.')))
    mask = list(map(lambda x: int(x), mask.split(' ')))

    return '.'.join(list(map(lambda x, y: str(x & y), ip, mask)))


def read_IP(l):
    with open('./data/ip.log', 'r+') as f:
        for line in f.readlines():
            l.append(line)


def input_mask():
    mask = input('Enter the mask: ')

    return mask
