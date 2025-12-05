# 도화지를 여유 있게 102x102로 생성 (테두리를 0으로 감싸기 위함)
arr = [[False for _ in range(102)] for _ in range(102)] 
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    # 좌표를 1씩 밀어서 중앙에 위치시킴 (0번 인덱스 접근 방지)
    for i in range(x+1, x+11): 
        for j in range(y+1, y+11):
            arr[j][i] = True

total = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(1, 102): # 1부터 101까지 탐색
    for j in range(1, 102):
        if arr[j][i] == True:
            tmp = 0 # 이번에는 '빈칸(흰색)'의 개수를 세는 게 더 직관적일 수 있습니다.
            
            # 기존 로직(검은색 세기) 유지 시:
            for k in range(4):
                if arr[j+dy[k]][i+dx[k]] == True:
                    tmp += 1
            
            if tmp == 3: total += 1
            elif tmp == 2: total += 2
            
print(total)