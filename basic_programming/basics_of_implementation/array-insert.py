n, q = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        a[x] = y
    else:
        print(sum(a[x:y+1]))
