from datetime import datetime as dt

DATE_FORMAT = '%d.%m.%Y'


def nearest_date(*strings: str) -> str:
    dates = list(sorted(map(lambda s: dt.strptime(s, DATE_FORMAT), strings)))
    currentDate = dt.now()
    d = dict()

    for date in dates:
        d.update({abs(currentDate - date): date})

    return d[min(d.keys())].strftime(DATE_FORMAT)


print('№3')

print(nearest_date("05.09.2022", "07.09.2022"))
print(nearest_date("01.01.2050", "12.04.2011", "31.12.1970"))
