import sieve
import numpy as np

primes = sieve.getPrimes(10000)

def d(n) :
    if n <= 1 : return 0 
    _f = [] # of factors
    _p = [] # thsi factor number
    
    # get factor info
    for prime in primes : 
        if prime > n : break

        _n = n
        cnt = 0

        while _n % prime == 0 :
            cnt += 1
            _n /= prime
    
        if cnt is not 0 :
            _f.append(cnt)
            _p.append(prime)

    return d2(_f, _p) - n

def d2(_f, _p) :
    if len(_f) is 0 : return 1
    f = _f.pop(0)
    p = _p.pop(0)

    _t = d2(_f, _p)

    return (np.array([p ** _i for _i in range(f + 1)]) * _t).sum()


n = range(25321)
dn = {_n : d(_n) for _n in n}
ans = set()
ans2 = []

for _n in dn :
    if dn[_n] in dn and dn[dn[_n]] == _n and dn[_n] is not _n :
        ans.add(_n)
        ans.add(dn[_n])
        ans2.append(_n)
        ans2.append(dn[_n])

print sum(ans)
print sum(ans2)


