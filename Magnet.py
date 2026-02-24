n = int(input())
t = []
for i in range(n):
    x = input()    
    t.append(x)
r= 1
for i in range(1, n):
    if t[i] != t[i - 1]:
        r += 1
print(r)        
        
    
    
    
