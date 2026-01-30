x,h = map(int,input().split())
y= list(map(int,input().split()))
r =0
for I in y:
    if I > h:
        r = r+2
    else:
        r = r+1   
print(r)       
