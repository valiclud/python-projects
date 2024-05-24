import calendar


def getSundays(datefrom, dateto):
    if (datefrom[0] > dateto[0]):
        return 0
    if datefrom[2] != 1:
        datefrom[1] += 1
        if datefrom[1] > 12:
            datefrom[1] = 1
            datefrom[0] += 1
    yearFrom = datefrom[0] % 400 + 400
    yearTo = dateto[0] % 400 + 400
    if yearFrom > yearTo:
        yearTo += 400
    monthTo = dateto[1]
    if (dateto[0] - datefrom[0]) > 400:
        mult = (dateto[0] - datefrom[0]) // 400
        yearTo += mult * 400
    count = 0
    while True:
        actual = calendar.monthrange(yearFrom, datefrom[1])
        if actual[0] == 6:
            count += 1
        if yearFrom >= yearTo and datefrom[1] >= monthTo:
            break
        datefrom[1] += 1
        if datefrom[1] > 12:
            yearFrom += 1
            datefrom[1] = 1
    return count


if __name__ == '__main__':
    n = int(input())
    for x in range(n):
        datefrom = list(map(int, input().split(' ')))
        dateto = list(map(int, input().split(' ')))
        print(getSundays(datefrom, dateto))
