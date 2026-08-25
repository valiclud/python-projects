'''
Created on 2. 6. 2024

@author: valic
'''

if __name__ == '__main__':
    expected_dev = round((2/3)**0.5, 3)
    expected_n = 0
    for x in range(0, 10000):
        n = x / 100
        avg = (1+2+3+n)/4
        sum_n = 0
        for i in range(1, 4):
            sum_n = sum_n + (i-avg)**2
        sum_n = sum_n + (n-avg)**2
        dev = round((sum_n / 4)**0.5, 3)
        if dev == expected_dev:
            expected_n = n
    print(expected_n)               