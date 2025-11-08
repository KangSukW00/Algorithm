# 첫째 줄부터 셋째 줄까지 입력
for _ in range(3):
    n = str(input())
    current_max = 1 # 현재까지의 최댓값
    cnt = 1 # 연속해서 나온 구간의 길이
    # 여덟 자리의 양의 정수
    for i in range(1, 8):
        # 연속해서 같은 숫자가 나오면 길이 + 1
        if n[i-1] == n[i]:
            cnt += 1
        # 다른 숫자가 나오면 현재까지의 최댓값을 갱신하고, 연속해서 나온 구간의 길이 초기화
        else:
            current_max = max(current_max, cnt)
            cnt = 1
    current_max = max(current_max, cnt)
    print(current_max)
