n = int(input())
l = list(map(int, input().split()))

p = 0
u = 0

for i in l:
    if i > 0:
        p += i
    else:
        if p > 0:
            p -= 1
        else:
            u += 1
print(u)
