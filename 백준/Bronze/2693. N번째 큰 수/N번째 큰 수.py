T = int(input())

for i in range(T) :
    s = list(map(int, input().split()))
    s.sort(reverse=True) # 내림차순 정렬
    print(s[2])