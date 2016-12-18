# https://en.wikipedia.org/wiki/Primality_test
def isPrime(n) :
    if n <= 1 : return False
    elif n <= 3 : return True
    elif n % 2 == 0 or n % 3 == 0 : return False

    i = 5
    while i * i <= n :
        if n % i == 0 or n % (i + 2) == 0 : return False
        i += 6

    return True

def maxPrime(a, b) :
    i = 0

    while isPrime(i ** 2 + a * i + b) :
        i += 1

    return i

ans = 0
max = 0
for _a in range(-1000, 1000) :
    for _b in range(-1000, 1000) :
        _max = maxPrime(_a, _b)

        if max < _max :
            max = _max
            ans = _a * _b

print ans

