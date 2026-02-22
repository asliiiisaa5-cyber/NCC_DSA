x,y = map(int,input().split())  
t = 3*x
r = 2*y
w = 1
while t<=r:
    w = w+1
    t = 3*t
    r = 2*r
print(w)
        
