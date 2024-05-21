# print("0.208").
def standard_dev(arr, mean):
    result = sum([pow(item - mean, 2) for item in arr])
    return pow(result, 0.5)


def solve(arrx, arry):
    meanx = sum(arrx) / len(arrx)
    meany = sum(arry) / len(arry)
    rxy = 0
    for idx, x in enumerate(arrx):
        rxy += (arrx[idx] - meanx) * (arry[idx] - meany)
    rxy = rxy / (standard_dev(arrx, meanx) * standard_dev(arry, meany))
    beta = rxy * (standard_dev(arry, meany) / standard_dev(arrx, meanx))

    print(format(beta, '.3f'))


if __name__ == '__main__':
    arr1 = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
    arr2 = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
    solve(arr1, arr2)


def get_regr_slope(x, y):
    xy = [a * b for a, b in zip(x, y)]
    n = len(x)
    x_2 = [a * a for a in x]
    num = n * sum(xy) - sum(x) * sum(y)
    denom = n * sum(x_2) - sum(x) ** 2
    slope = num / denom
    print("%.3f" % slope)
    print("done")
