colors = set()	#set함수를 이용하여 중복 자동 제거

for _ in range(2):
    parents = input().split()
    for p in parents:
        colors.add(p)

birdColor_lst = sorted(list(colors)) # 사전 순 정렬

for i in birdColor_lst:
    for j in birdColor_lst:
        print(i, j)