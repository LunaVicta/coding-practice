def primeFactors(x):
    i = 2
    output = []
    while(i<x):
        if(x%i==0):
            output.append(i)
            x = int(x/i)
            i = 2
        if(i==2):
            i += 1
        else:
            i += 2
    if(x!=1):
        output.append(x)
    return output
print(primeFactors(600851475143))
