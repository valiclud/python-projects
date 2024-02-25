def standard_dev(arr, n, mean):
    result = 0
    for x in arr:
        result += pow(x - mean, 2)
    return pow(result, 0.5)


def solve(arrx, arry):
    nx = len(arrx)
    ny = len(arry)
    meanx = sum(arrx) / nx
    meany = sum(arry) / ny
    rxy = 0
    for idx, x in enumerate(arrx):
        rxy += (arrx[idx] - meanx) * (arry[idx] - meany)
    rxy = rxy / (standard_dev(arrx, nx, meanx) * standard_dev(arry, ny, meany))
    print(format(rxy, '.3f'))


if __name__ == '__main__':
    arr1 = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
    arr2 = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
    solve(arr1, arr2)
