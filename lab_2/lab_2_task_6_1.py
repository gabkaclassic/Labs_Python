def run():
    text = read_text().lower()
    write_solve(analyze_text(text))


def analyze_text(text):
    letters = dict()

    for l in text:
        if ord(l) in range(1040, 1104):
            letters.setdefault(l, 0)
            letters.update({l: letters.get(l) + 1})
    ln = sum(letters.values())

    for k in letters.keys():
        letters.update({k: letters.get(k)/ln})

    letters = dict(sorted(letters.items(), key=lambda items: items[1], reverse=True))

    return letters


def write_solve(solve):
    with open('./data/article_rus_solve.txt', 'w+', encoding='utf-8') as f:
        for k in solve.keys():
            f.write('{0}: {1}\n'.format(k, solve.get(k)))


def read_text():
    with open('./data/article_rus.txt', 'r+', encoding='utf-8') as f:
        text = f.read()
    return text
