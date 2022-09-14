from random import randint as rand


def generate_IP(IP_list):
    for i in range(10000):
        IP_list.append(
            str(rand(1, 255)) + '.' + str(rand(1, 255)) + '.' + str(rand(1, 255)) + '.' + str(rand(1, 255)) + '\n')


def run():
    IP_list = list()
    generate_IP(IP_list)
    write_list(IP_list)


def write_list(data):
    with open('./data/ip.log', 'w+') as f:
        f.writelines(data)
