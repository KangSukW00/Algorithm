N = int(input())
T, P = [0], [0]

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
dp = [0] * (N+6)
for i in range(N,0,-1):
    if i + T[i] > N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])

print(dp[1])