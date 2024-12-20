import sys
input = sys.stdin.readline
N = int(input())
dp = [0]*1001
dp[1]=1    #sk
dp[2]=2    #cy
dp[3]=1    #sk
for n in range(4,N+1):
    dp[n] = min(dp[n-1],dp[n-3]) + 1
if dp[N] % 2 == 1:
    print('SK')
else:
    print('CY')
    