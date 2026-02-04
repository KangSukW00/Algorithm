n = int(input())
d = [0] * (n+1) #단순히 재귀적으로 풀 때 과도한 시간이 걸리는 것을 방지하기 위해 dp로 풀어준다.

if n == 1:
    d[1] = 1
    print(d[1])
elif n == 2:
    d[2] = 1
    print(d[2])
else:
    d[1] = 1 #인덱스 에러를 해결하기 위해 이렇게 써주어야 한다.
    d[2] = 1
    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2] # 재귀함수를 이용해 풀이
    print(d[n])