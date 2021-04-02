primes = [2]
i = 3
while(len(primes)<10001):
    e = 0
    b = True
    while(e<len(primes) and b):
        b = not (i%primes[e]==0)
        e += 1
    if(b):
        primes.append(i)
    i += 2
print(primes[10000])
