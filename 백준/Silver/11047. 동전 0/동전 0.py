# 1. 계산대 안에 있는 돈의 수와 거슬러 줄 돈을 구합니다.
N, K = map(int, input().split())  # N : 화폐 종류수, K : 거슬러 줄 돈

# 2. 계산대에 있는 화폐들을 리스트의 형태로 입력받습니다.
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

# 3. 그리디 알고리즘으로 거슬러 줍니다.
answer = 0
for coin in coins:
    if K >= coin:
        answer += K // coin   # 해당 동전 개수만큼 더하기
        K %= coin             # 나머지 금액 갱신
        if K == 0:            # 더 이상 거슬러 줄 돈이 없으면 종료
            break

print(answer)  # 거슬러 준 동전 + 화폐의 수
