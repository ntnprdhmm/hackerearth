def sieve_of_eratosthene(n):
    primes = []

    l = range(2, n+1)
    while len(l):
        primes.append(l[0])

        temp = []
        for i in range(1, len(l)):
            if l[i] % l[0] != 0:
                temp.append(l[i])
        l = temp

    return primes

print(' '.join(list(map(str, sieve_of_eratosthene(int(input()))))))
