def palindrome(x):
    y = str(x)
    for i in reversed(y):
        y = y+i
    return int(y)
x = 999
while(x>1):
    i = 999
    while(i>99):
        if((palindrome(x))%i==0 and (palindrome(x))/i>99 and (palindrome(x))/i<1000):
            print((palindrome(x)))
            print((palindrome(x))%i)
            print(i)
            break
        i-=1
    if(i>99):
        break
    x-=1
print(palindrome(x))
