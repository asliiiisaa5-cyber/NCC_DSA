x,y = map(int, input().split())
z,m = map(int, input().split())
if x == z and y == m:
    print("0")
elif x == z or y == m:
    print("1")
else:
    print("2")    
    
