def SieveOfEratosthenes(n):
    result = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            result.append(p)
    return result

def is_prime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

import random
def power(x, y, p):
    res = 1;
    x = x % p;
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1;  # y = y/2
        x = (x * x) % p;

    return res;
def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4);

    x = power(a, d, n);

    if (x == 1 or x == n - 1):
        return True;

    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;

        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
    return False;
def isPrime(n, k):
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;
    return True;

if __name__ == '__main__':
    n = int(input())
    index = 1
    shift = 0
    result = {}
    primes = 0
    notPrimes = 1
    while True:
        shift += 2
        for y in range(0, 4):
            index += shift
            result[index] = shift + 1
            if isPrime(index, 3):
                primes += 1
            else:
                notPrimes += 1
        if (primes / (notPrimes + primes)) * 100 < n:
            break
    print(result[index])



