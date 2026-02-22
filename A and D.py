n = int(input())
x = str(input())
y = x.count("D")
t = x.count("A")
if y<t:
    print("Anton")
elif y>t:
    print("Danik")  
else:
    print("Friendship")      
