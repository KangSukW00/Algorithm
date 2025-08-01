import sys
input = sys.stdin.readline
n = int(input())
dp = list(float(input()) for _ in range(n))
for i in range(1,n):
    dp[i] = max(dp[i], dp[i-1] * dp[i])
print("%0.3f" % max(dp))