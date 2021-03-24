f0 = 1
f1 = 1
x = 0
while(f1<4000000):
    temp = f0 + f1
    f0 = f1
    f1 = temp
    if(f1%2==0):
        x+=f1
print(x)
