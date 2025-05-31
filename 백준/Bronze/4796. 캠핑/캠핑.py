cnt=1
while True:
    l,p,v=map(int,input().split())
    if l==p==v==0:break
    result= l*(v//p)+l if v%p>l else l*(v//p)+v%p
    print(f"Case {cnt}: {result}")
    cnt+=1