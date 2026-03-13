case = int(input())
answer = 0

for _ in range(case):
    a, b, c = sorted(map(int, input().split()))
    
    if a == b == c:
        answer = max(answer, 10000 + a*1000)
        
    elif a == b or b == c:
        answer = max(answer, 1000 + b*100)
        
    else:
        answer = max(answer, 100 * c)

print(answer)