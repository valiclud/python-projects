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
def reciprocalcycles():
    prime_numbers = SieveOfEratosthenes(10000)
    result = {}
    for x in prime_numbers:
        index = 1
        divisor = 10
        divisor_0 = divisor // x
        reminder_0 = divisor % x
        divisor = reminder_0 * 10
        reminder = reminder_0
        while reminder != 0:
            div = divisor // x
            reminder = divisor % x
            divisor = reminder * 10
            if divisor_0 == div and reminder_0 == reminder:
                result[x] = index
                break
            index += 1
    return result

if __name__ == '__main__':
    cycles = reciprocalcycles()
    n = int(input())
    for _ in range(n):
        max = 0
        result = 0
        inp = int(input())
        for x in cycles:
            if inp <= x:
                break
            if cycles[x] > max:
                max = cycles[x]
                result = x
        print(result)
