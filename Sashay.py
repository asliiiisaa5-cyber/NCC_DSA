t = int(input())
for i in range(t):
    n = int(input())
    y =list(map(int, input().split()))
    y.sort() 
    x = max(y)-min(y)
    print(x)      
