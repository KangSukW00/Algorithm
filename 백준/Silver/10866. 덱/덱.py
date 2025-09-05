import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 명령의 개수 입력받기
n = int(input())

# 명령어를 입력받아 리스트에 저장
cmd = [input() for _ in range(n)]

# 덱 초기화
deque = []

# 입력받은 명령어를 하나씩 처리
for c in cmd:
    # push_front X: 정수 X를 덱의 앞에 삽입
    if 'push_front' in c.split()[0]:
        deque.insert(0, c.split()[1])
    # push_back X: 정수 X를 덱의 뒤에 삽입
    elif 'push_back' in c.split()[0]:
        deque.append(c.split()[1])
    # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력
    # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif 'pop_front' in c:
        print(deque.pop(0)) if deque else print(-1)
    # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력
    # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif 'pop_back' in c:
        print(deque.pop(-1)) if deque else print(-1)
    # size: 덱에 들어있는 정수의 개수를 출력
    elif 'size' in c:
        print(len(deque))
    # empty: 덱이 비어있으면 1을, 아니면 0을 출력
    elif 'empty' in c:
        print(0) if deque else print(1)
    # front: 덱의 가장 앞에 있는 정수를 출력
    # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif 'front' in c:
        print(deque[0]) if deque else print(-1)
    # back: 덱의 가장 뒤에 있는 정수를 출력
    # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif 'back' in c:
        print(deque[-1]) if deque else print(-1)