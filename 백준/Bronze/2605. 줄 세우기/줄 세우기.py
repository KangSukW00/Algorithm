N = int(input())
arr = list(map(int, input().split()))
bucket = []

for i in range(N):
    bucket.insert(i-arr[i], i+1)

print(*bucket)