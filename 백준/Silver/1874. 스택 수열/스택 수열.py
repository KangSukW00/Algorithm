n = int(input())
stack = []
temp = []
dsc = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:       
        stack.append(cur)
        temp.append("+")
        cur += 1

    if stack[-1] == num:    
        stack.pop()         
        temp.append("-")
    else:                   
        print("NO")         
        dsc = 1           
        break               

if dsc == 0:
    for i in temp:
        print(i)