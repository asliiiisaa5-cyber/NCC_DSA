n = int(input())
x = str(input())
y =0
for i in range(1,n):
    if x[i] == x[i-1]:
        y = y +1
print(y)   
    
