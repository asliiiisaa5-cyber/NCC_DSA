x = str(input())
y =0
w =0
for I in x:
    if I.isupper():
        y = y+1
    if I.islower():
        w = w+1
if y > w:
    print(x.upper())
  
elif w > y:
    print(x.lower())
else:
     print(x.lower())         
