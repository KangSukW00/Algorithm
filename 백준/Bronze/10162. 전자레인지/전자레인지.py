t = int(input())

# 작동 시간
oper_time = [300, 60, 10]
ans = []
count = 0 

# 10으로 나누어 떨어지지 않으면 -1 출력 <= 버튼 최소 단위인 10으로 나누어져야 버튼가능
if t % 10 != 0:
    print(-1)

else:
  # 각 전자레인지 작동 횟수 구하기
  for i in oper_time:
    count = t // i
    ans.append(count)
    t %= i
  # a, b, c 작동 횟수를 공백을 두고 출력
  print(ans[0], ans[1], ans[2])