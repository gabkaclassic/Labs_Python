from random import randint as rand


def run():
    generate_files()


def generate_files():
    for i in range(100):
        with open('./data/example/{0}.txt'.format(i), 'wb') as f:
            f.seek(rand(1, 100) * 1024 - 1)
            f.write(b'\0')
