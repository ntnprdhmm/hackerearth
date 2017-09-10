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

def filter_values(arr, low, high):
    filtered = []

    for v in arr:
        if v >= low and v <= high:
            filtered.append(v)

    return filtered

def transform(s):
    temp = []
    for i in range(len(s)):
        temp.append(chr(find_closest_prime(ord(s[i]))))
    return ''.join(temp)

def find_closest_prime(v):
    if v < ascii_primes[0]:
        return ascii_primes[0]

    for i in range(1, len(ascii_primes)):
        if ascii_primes[i] > v:
            if (ascii_primes[i] - v) >= (v - ascii_primes[i-1]):
                return ascii_primes[i-1]
            else:
                return ascii_primes[i]

    return ascii_primes[-1]


ascii_primes = filter_values(sieve_of_eratosthene(122), 65, 122)

for _ in range(int(input())):
    input(), print(transform(input()))
