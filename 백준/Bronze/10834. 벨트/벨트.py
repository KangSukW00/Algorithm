N = int(input())
r = 0
ans = 1

for _ in range(N):
    a, b, s = map(int, input().split())
    if s==1:
        r = (r+1)%2		#if(r == 1): r = 1 - r	#if w: c = not c
    ans=(ans*b)/a		#ans*(b/a)는 에러남 , 계산 순서에 따른 실수 계산의 정수화 오류
    
print(r, int(ans))