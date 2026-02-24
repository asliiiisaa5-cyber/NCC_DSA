n = int(input())
ca = list(map(int, input().split()))
l = 0
r = n - 1
s = 0
d = 0
t = 0  
while l <= r:
    if ca[l] > ca[r]:
        c= ca[l]
        l += 1
    else:
        c=ca[r]
        r -= 1
    if t == 0:
        s+=c
    else:
        d+=c
    t= 1-t  
print(s,d) 
    
        
    
    
    
