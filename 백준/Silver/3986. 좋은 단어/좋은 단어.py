import sys
input = sys.stdin.readline
n = int(input().rstrip())
cnt = 0

for _ in range(n):
    stack = []
    _list = list(input().rstrip())
    for i in _list:
        if not len(stack):
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)

    if not len(stack):
        cnt += 1 

print(cnt)