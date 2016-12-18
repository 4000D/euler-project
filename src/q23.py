import sieve

MAX = 28123
primes = sieve.getPrimes(MAX + 2)


def getDivInfo(n, primes) :
    f = [] # n = p^f * ....
    p = [] 

    for prime in primes :
        if n < prime : break

        _n = n
        cnt = 0

        while _n % prime == 0 :
            cnt += 1
            _n /= prime

        if cnt > 0 :
            f.append(cnt)
            p.append(prime)

    return (f, p)


'''
just repeat :: 
    n /= p
    ret += p 
'''
def sumOfDivs(f, p) :
    if len(f) == 0 : return 1

    ret = 0
    
    _f = f.pop(0)
    _p = p.pop(0)
    _t = sumOfDivs(f, p)

    return sum([_p ** i for i in range(_f + 1)]) * _t


on = [] # Over Number..?
for n in range(2, MAX+2) :
    f,p = getDivInfo(n, primes)
    if sumOfDivs(f,p) - n > n : on.append(n)

sumOf2ONs = set()

for i in range(len(on)) :
    for j in range(i, len(on)) :
        if on[i] + on[j] > MAX : break
        sumOf2ONs.add(on[i] + on[j])

print ((MAX + 1) * MAX) / 2 - sum(sumOf2ONs)
