def SieveOfEratosthenes(n):
    result = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1 ):
        if prime[p]:
            result.append(p)
    return result

if __name__ == '__main__':
    prime_numbers = SieveOfEratosthenes(10000)
    n = int(input())
    for _ in range(n):
        inp = int(input())
        max = 0
        result = 0
        for x in prime_numbers:
            if x >= inp:
                break
            reminders = []
            divisors = []
            index = 0
            divisor = 10
            reminder = 1
            while reminder != 0:
                div = divisor // x
                reminder = divisor % x
                divisors.append(div)
                reminders.append(reminder)
                index += 1
                divisor = reminder * 10
                if divisors[0] == div and reminders[0] == reminder and index != 1:
                    if (index - 1) > max:
                        max = index - 1
                        result = x
                    break
        print(result)
