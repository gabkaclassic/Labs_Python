from csv import reader as read
from csv import writer as write


def run():
    data = input_data()
    write_result(get_champions(data))


def get_champions(data):
    sort_players(data)
    result = list()
    count = 1

    for i in range(len(data) - 1):
        result.append([data[i].name, count])
        if data[i].more_than(data[i + 1]):
            count += 1
    result.append([data[-1].name, count])

    return result


def write_result(result):
    with open('./data/results.csv', 'w+', encoding='utf-8') as f:
        writer = write(f, delimiter=';')
        writer.writerow(['Спортсмен', 'Место'])
        writer.writerows(result)


def input_data():
    result = list()

    with open('./data/players.csv', 'r+', encoding='utf-8') as f:
        rows = read(f, delimiter=';')
        for row in rows:
            result.append(row)

    result = list(map(lambda r: Player(r), result[1:]))

    return result


def sort_players(data):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if not data[j].more_than(data[j + 1]):
                p = data[j]
                data[j] = data[j + 1]
                data[j + 1] = p


class Player:

    def __init__(self, row):
        self.name = row[0]
        self.wins = int(row[1])
        self.optional = int(row[2])

    def more_than(self, other):
        if self.wins > other.wins:
            return True
        elif other.wins > self.wins:
            return False
        else:
            return self.optional > other.optional

    def __str__(self):
        return '; '.join([self.name, str(self.wins), str(self.optional)])
