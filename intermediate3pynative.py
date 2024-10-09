a = [10,20,30,40,50,60,70,80,90,100]
n = len(a)
i = 0
while i < n:
    p = a[i]
    if p < 50:
        a.remove(p)
        n -= 1
    else:
        i += 1
print(a)      