if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        try:
            num = list(map(int, input().split(' ')))
            print(num[0] // num[1])
        except ZeroDivisionError as e1:
            print("Error Code:", e1)
        except ValueError as e2:
            print("Error Code: {0}".format(e2))

