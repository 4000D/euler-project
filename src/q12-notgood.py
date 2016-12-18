import math
import sieve

def getTriNum(n) : # return n-th triangle-number
    return sum(range(1, n+1))

def getDivisors(n, primes) : # [3,2,5] : 2^3 * 3^2 * 5^5
    ret = [0] * int(math.sqrt(len(primes)))
    _ret = [] # domain specific
    lastIdx = 0

    for i in range(len(ret)) :
        prime = primes[i]
        _n = n
        cnt = 0
        while _n % prime == 0 :
            _n /= prime 
            cnt += 1
            
        if cnt is not 0 : 
            lastIdx = i
            ret[i] = cnt 
            _ret.append(cnt + 1) # include power of 0

    # return ret[0:lastIdx+1]
    return _ret

def getNumDivs(divs) :
    if len(divs) is 0 : return 1
    return reduce(lambda a, b : a * b, divs)


ans = 1
primes = sieve.getPrimes(int(2e6))

# while ans < 30 :
while True :
    ans += 1
    tri = getTriNum(ans)
    divisors = getDivisors(tri, primes)
    totalDivs = getNumDivs(divisors)

    # print tri, divisors, totalDivs

    if totalDivs > 500 :
        print tri
        break
