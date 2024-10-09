a = [10,20,25,30,35]

b = [40,45,60,75,90]

c = []

for i in a:
    if i%2 != 0:
        c.append(i)

for i in b:
    if i%2 == 0:
        c.append(i) 

print(c)            