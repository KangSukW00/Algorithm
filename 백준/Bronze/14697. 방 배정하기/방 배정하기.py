import sys
input=sys.stdin.readline

a,b,c,n = map(int, input().split())
res = 0
for i in range(0, n+1, a):
    for j in range(0, n+1-i, b):
        for k in range(0, n-i-j+1, c):
            if i+j+k==n:
                res = 1
print(res)