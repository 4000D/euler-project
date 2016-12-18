import _sieve
primes = _sieve.getPrimes(int(1e6))

def getDivisors(n) :
    ret = []

    for prime in primes :
        if n == 1 : return ret

        while n % prime == 0 :
            n /= prime
            ret.append(n)

    return ret


def isPandigital(*nums) :
    s = [0 for i in range(0, 10)]
    for n in nums :
        for c in str(n) :
            s[int(c)-1] += 1
    for _s in s :
        if _s > 1 : return False
    return True

'''
ans = 0

for c in range(1, int(1e5)) :
    if isPandigital(c) :
        divs = getDivisors(c)
        for div in divs :
            if isPandigital(c, div, c/div) :
                ans += c
                print c
                break

print ans
'''

'''
ans = set()

for a in range(1, int(1e5)) :
    if isPandigital(a) :
        for b in range(1, int(1e5)) :
            if isPandigital(a, b, a*b) :
                ans.add(a*b)

print sum(ans)
'''

ans = set()

# Permutation : nPn
def perm(arr, i) :
    global ans
    if i == len(arr) : 
        # do something here
        for _a in range(1, 8) : 
            for _b in range(_a + 1, 8) :
                __a = int(''.join(arr[:_a]))
                __b = int(''.join(arr[_a:_b]))
                __c = int(''.join(arr[_b:]))    

                t = sorted([__a, __b, __c])
                a = t[0]
                b = t[1]
                c = t[2]

                if a * b == c :
                    ans.add(c)

    # permutation part
    for _i in range(i, len(arr)) :
        arr[i], arr[_i] = arr[_i], arr[i]
        perm(arr, i+1)
        arr[i], arr[_i] = arr[_i], arr[i]
    return

arr = [str(i) for i in range(1, 10)]

perm(arr, 0)

print sum(ans)


