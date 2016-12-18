def getPrimes(_max) :
    primes = [True] * (_max + 1)
    primes[0] = primes[1] = False
    ret = []
    
    for i in range(2, _max + 1) :
        if primes[i] :
            ret.append(i)
            t = i * 2
            while t <= _max :
                primes[t] = False
                t += i
    return ret

