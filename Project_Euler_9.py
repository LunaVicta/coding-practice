a = 4
notSolved = True
while(notSolved and a < 333):
    b = a+1
    #print("a: "+str(a))
    maxB = (1000-a)/2
    while(b < maxB):
        #print("\tb: "+str(b))
        #print("\t(100-a)/2 :"+str(maxB))
        if(a**2+b**2 == (1000-a-b)**2):
            notSolved = False
            print("solved")
            print(a)
            print(b)
            print(1000-a-b)
            print(a*b*(1000-a-b))
        b += 1
    a += 1
print("done")
