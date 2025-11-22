n = int(input())
num = list(map(int, input().split()))

count1 = 1   # 증가 길이
count2 = 1   # 감소 길이
ans = 1

for i in range(1, n):
    # 증가 방향
    if num[i] > num[i-1]:
        count1 += 1
        count2 = 1
    # 감소 방향
    elif num[i] < num[i-1]:
        count2 += 1
        count1 = 1
    # 같을 때
    else:
        count1 += 1
        count2 += 1

    ans = max(ans, count1, count2)

print(ans)
