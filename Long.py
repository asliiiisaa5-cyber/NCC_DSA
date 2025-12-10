x = int(input())
for i in range(x):
    m = input()
    if len(m) < 11:
        print(m)
    else:
        print(m[0] + str(len(m)-2) + m[-1])
