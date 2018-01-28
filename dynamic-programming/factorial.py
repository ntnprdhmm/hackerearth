dp = [0 for _ in range (100001)]
dp[0] = dp[1] = 1

def fac(n):
    if dp[n] == 0:
        dp[n] = fac(n-1) * n
    return dp[n] % (10**9+7)

for _ in range(int(input())):
    print(fac(int(input())))
