x = 121
y = 125

def palindrome(n):
    a = n
    i = 1
    e = 0
    while i <= 3:
        c = a%10
        e = e*10 + c
        a = a//10
        i += 1
    if e == n:
        print(f'{n} is a palindrome number')
    else:
        print(f'{n} is not a palindrome number')
palindrome(x)
palindrome(y)