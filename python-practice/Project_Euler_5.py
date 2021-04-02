def GCF(a,b):
    i = 2
    while(i<=a and i<=b):
        if(a%i==0 and b%i==0):
            return i * GCF(a/i,b/i)
        i+=1
    return 1
def LCM(a,b):
    return a*b/GCF(a,b)
x = 20
for i in range(19,1,-1):
    x = LCM(x,i)
print(x)
