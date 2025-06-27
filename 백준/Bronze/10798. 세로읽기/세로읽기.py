import sys
input = sys.stdin.readline

numList=[]
for _ in range(5):
    numList.append(list(input().rstrip()))
for i in range(15):
    for j in range(5):
        if i < len(numList[j]):
            print(numList[j][i], end='')