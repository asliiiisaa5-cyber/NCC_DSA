n, x = map(int, input().split())
y = 0
for i in range(n):
    a, b = input().split()
    b = int(b)
    if a == '+':
        x += b
    else:  
        if x >= b:
            x -= b
        else:
            y+= 1
print(x, y)       
