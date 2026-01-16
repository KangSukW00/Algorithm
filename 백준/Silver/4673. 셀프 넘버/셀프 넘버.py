natural_lst = set(range(1, 10001))
gen_lst = set()
 
for i in natural_lst :
    for j in str(i) :
        i += int(j)
    gen_lst.add(i)
 
self_numbers = natural_lst - gen_lst
for s in sorted(self_numbers) :
    print(s)