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


prime_numbers = SieveOfEratosthenes(10000)

if __name__ == '__main__':

    print(prime_numbers)
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
            while True:
                div = divisor // x
                reminder = divisor % x
                if reminder == 0:
                    break
                divisors.append(div)
                reminders.append(reminder)
                divisor = reminder * 10
                if divisors[0] == div and reminders[0] == reminder and index != 0:
                    if (len(reminders) - 1) > max:
                        max = len(reminders) - 1
                        result = x
                    break
                index += 1
        print(result)
