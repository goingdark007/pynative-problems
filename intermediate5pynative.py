a = [10,20,60,30,20,40,30,60,70,80]
b = []
n = len(a)
i = 0
while i<n:
    print(i)
    p = a.count(a[i])
    if p > 1:
        b.append(a[i])
    
    i += 1
print(b)           