a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)

for i in range(10):   # 0 ~ 9
    cnt = 0
    for j in result:  # 결과의 각 자리
        if j == str(i):
            cnt += 1
    print(cnt)