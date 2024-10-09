a = 45000
b = 10000
c = 10000
e = 0
if (a - b) > 0:
    a = a - b
    if (a-c) > 0:
        a = a-c
        e = c*0.10
        if a > 0:
            e = e + (a*0.2)
            print(f'Income tax is {e}')
    else:
        e = a*0.1
        print(f'Income tax is {e}')    
else:
    print(f'Income tax is {e}')
