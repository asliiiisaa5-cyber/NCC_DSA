s = input()
p = 'a'
r = 0
for i in s:
    v = abs(ord(i) - ord(p))
    r += min(v, 26 - v)
    p = i
print(r)
        
    
    
    
