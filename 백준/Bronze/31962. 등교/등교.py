N, X = map(int, input().split())

bus = []
for _ in range(N):
    S, T = map(int, input().split())
    if S + T <= X:
        bus.append(S)

if bus:
    bus.sort(reverse=True)
    print(bus[0])
else:
    print(-1)
