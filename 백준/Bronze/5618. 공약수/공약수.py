import sys
input = sys.stdin.readline

n = int(input())
N_List = list(map(int, input().split()))
N_Min = min(N_List)


for i in range(1, N_Min + 1):
    count = 0
    for j in N_List:
        if j % i == 0:
            count += 1
        else:
            break
    if count == n:
        print(i)