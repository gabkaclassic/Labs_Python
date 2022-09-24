def hofstadter_f_m(number: int) -> (int, int):
    count = 0
    while count < number:
        def F(n: int) -> int:
            return 1 if n == 0 else n - M(F(n - 1))

        def M(n: int) -> int:
            return 0 if n == 0 else n - F(M(n - 1))

        yield F(count), M(count)
        count += 1


print('№2')

while True:
    n = input('Enter n: ')
    if not n.isdigit():
        print('Enter positive integer or zero')
        continue
    for i in hofstadter_f_m(int(n)):
        print(i)
