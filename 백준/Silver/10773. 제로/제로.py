import sys
input = sys.stdin.readline

stack = []
k = int(input())

for _ in range(k):
    N = int(input())
    if N == 0:
        stack.pop()
    else:
        stack.append(N)
print(sum(stack))