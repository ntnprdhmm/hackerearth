"""
    Count how many time a given integer is divisible by 2
"""
def count_divisible_by_2(n):
    if n == 1 or n == 0:
        return n

    power = 0
    value = 1
    while value*2 <= n:
        value *= 2
        power += 1
    return power + 1

n, q = map(int, input().split())
arr = [0] * (n+1)

for i, v in enumerate(list(map(int, input().split()))):
    arr[i+1] = count_divisible_by_2(v) + arr[i]

for _ in range(q):
    # read range
    l, r = map(int, input().split())
    # count the number of turns that can be played in the given range
    nb_turns = arr[r] if l == 1 else arr[r] - arr[l-1]
    # print winner
    print("Mishki" if nb_turns % 2 == 1 else "Hacker")
