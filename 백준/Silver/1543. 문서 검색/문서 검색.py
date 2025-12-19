doc = input()
word = input()
res = 0

while True:
    idx = doc.find(word)
    if idx == -1:
        break
    
    res += 1
    doc = doc[idx+len(word):]
    
print(res)