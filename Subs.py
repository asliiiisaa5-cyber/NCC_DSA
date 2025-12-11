x,y = map(int, input().split())
for I in range(y):
    if x%10 != 0:
        x = x -1
    elif x%10 ==0:
        x = x //10
print(x)         
