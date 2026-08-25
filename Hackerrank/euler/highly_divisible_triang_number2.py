def sieveOfEratosthenes(n):
    result = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] is True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            result.append(p)
    return result

if __name__ == '__main__':
    primes = sieveOfEratosthenes(2000000)
    print(len(primes))
    n = int(input())
    for _ in range(n):
        a = 0
        t = 0
        cnt = 0
        div = int(input())
        if div == 1:
            print(3)
            continue
        while cnt <= div :
            cnt = 1
            a = a + 1
            t = t + a
            tt = t
            for i in range(140000) :
                if primes[i] * primes[i] > tt:
                    cnt = 2 * cnt
                    break
                exponent = 1
                while tt % primes[i] == 0:
                    exponent = exponent + 1
                    tt = tt // primes[i]
                if exponent > 1:
                    cnt = cnt * exponent
                if tt == 1:
                    break
        print(t)