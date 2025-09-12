from collections import deque

N = int(input())
dq = deque()

dq.appendleft(N)

#N-1부터 1까지 차례대로 새로운 카드를 맨 앞에 넣습니다.
for n in range(N - 1, 0, -1):
    dq.appendleft(n)
    #덱의 맨 뒤 카드를 꺼내서 맨 앞으로 옮기는 과정을 n번 반복합니다.
    for j in range(n):
        moveCard = dq.pop()
        dq.appendleft(moveCard)

print(*dq)