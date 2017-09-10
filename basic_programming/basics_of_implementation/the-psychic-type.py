n = int(input())

arr = [0] * 1002
for i, v in enumerate(list(map(int, input().split()))):
    arr[i + 1] = v

s, e = map(int, input().split())

if s == e:
    print('Yes')
elif arr[s] == s:
    print('No')
else:
    found = False
    c = 0

    while not found:
        if c == n:
            break
        s = arr[s]
        if s == e:
            found = True
        c += 1

    print('Yes' if found  else 'No')
