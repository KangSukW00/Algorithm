import sys
input = sys.stdin.readline
 
N = int(input())
my_list = sorted(list(map(int, input().split())))
M = int(input())
check_list = list(map(int, input().split()))
 
for card in check_list:
    low, high = 0, N-1 # 이진탐색 index
    exist = False
 
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] > card: # 중간값보다 작은 경우
            high = mid - 1
        elif my_list[mid] < card: # 중간값보다 큰 경우
            low = mid + 1
        else: # 검색값이 존재하는 경우
            exist = True
            break
    
    print(1 if exist else 0, end=" ")
