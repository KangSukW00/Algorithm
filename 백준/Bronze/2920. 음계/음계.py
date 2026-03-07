melodys = list(map(int,input().split()))

if melodys == sorted(melodys):
    print("ascending")
elif melodys == sorted(melodys,reverse=True):
    print("descending")
else:
    print("mixed")