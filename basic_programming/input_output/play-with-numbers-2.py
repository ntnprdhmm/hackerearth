from math import floor

n, q = list(map(int, input().split()))
arr = [0] * (n+1)

# precalculate sums (start at index 1, not 0)
for i, v in enumerate(list(map(int, input().split()))):
    arr[i + 1] = arr[i] + v

for _ in range(q):
    l, r = list(map(int, input().split()))
    print(int(floor((arr[r] - arr[l-1]) / (r-l + 1))))
