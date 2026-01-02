import sys
input = sys.stdin.readline

N = int(input())
B = [list(input().strip()) for _ in range(N)] # .strip()을 추가하여 줄바꿈 문자 제거 추천

def checkBoard():
    max_cnt = 1 # [수정 2] 변수 초기화 필요
    for i in range(N):
        # 가로 확인
        cnt = 1
        for j in range(1, N):
            if B[i][j] == B[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        
        # 세로 확인
        cnt = 1
        for j in range(1, N): # [수정 1] rnage -> range 오타 수정
            if B[j][i] == B[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
            
    return max_cnt

result = 1 # 아무것도 안 바꿨을 때의 초기값 계산 필요할 수 있음 (N=1일 때 등 고려)

for i in range(N):
    for j in range(N):
        # 오른쪽과 교환 (범위 체크)
        if j + 1 < N:
            B[i][j], B[i][j+1] = B[i][j+1], B[i][j]
            result = max(result, checkBoard())
            B[i][j], B[i][j+1] = B[i][j+1], B[i][j] # 원상복구

        # 아래쪽과 교환 (범위 체크)
        if i + 1 < N:
            # [수정 3] 로직 수정: j+1이 아니라 j와 비교해야 함
            B[i][j], B[i+1][j] = B[i+1][j], B[i][j]
            result = max(result, checkBoard())
            B[i][j], B[i+1][j] = B[i+1][j], B[i][j] # 원상복구

print(result)