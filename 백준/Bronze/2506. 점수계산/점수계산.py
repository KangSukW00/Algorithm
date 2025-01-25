N = int(input())
data = list(map(int, input().split()))

score = ans = 0
for i in range(N):
    if data[i]:
        score += 1
    else:
        score = 0
    ans += score
print(ans)