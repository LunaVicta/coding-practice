primes = [2]
i = 3
while(primes[-1]<2000000):
    e = 0
    b = True
    while(e<len(primes) and b):
        b = not (i%primes[e]==0)
        e += 1
    if(b):
        print(i)
        primes.append(i)
    i += 2
print(sum(primes))
