import sys
input = sys.stdin.readline

T = int(input())

arr = [1, 1, 1]

for i in range(3, 100):
    arr.append(arr[i-2] + arr[i-3])  

for _ in range(T):
    N = int(input().strip())  

    print(arr[N-1])