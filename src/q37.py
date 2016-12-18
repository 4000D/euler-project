import _sieve

primes = _sieve.getPrimes(int(1e6))[4:]

ans = 0
cnt = 0

for prime in primes :
    if cnt == 11 : break
    s = str(primes)

    a = True

    for i in range(len(s)) :
        s1 = int(s[i:])
        s2 = int(s[:max(i,1)])
        print s1, s2
        if s1 not in primes or s2 not in primes :
            a = False
            break

    if a :
        ans += prime
        cnt += 1

print ans


