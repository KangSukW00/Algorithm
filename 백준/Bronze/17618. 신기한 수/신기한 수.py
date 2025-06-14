import sys
input = sys.stdin.readline

N = int(input())
count = 0

for i in range(1, N+1):
    tmp = str(i)
    divisor_sum = 0
    for j in tmp:
        divisor_sum += int(j)
    if i % divisor_sum == 0:
        count += 1
print(count)