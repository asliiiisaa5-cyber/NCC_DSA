n = int(input())
r =0
for i in range(n):
    x,y,z = map(int,input().split())
    if x+y+z==3 or x+y+z==2:
        r+=1
print(r)
          
    
        
        
