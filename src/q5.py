import sieve
import math

def lcf(nums) :
    _lcf = 1

    # should be global... but
    primes = sieve.getPrimes(max(nums))

    for prime in primes :
        nums = [num for num in nums if num != 1]
        if len(nums) == 1 : return _lcf * num[0]

        maxCnt = 0
        for num in nums :
            cnt = 0
            while num % prime == 0 :
                num /= prime
                cnt += 1

            maxCnt = max(maxCnt, cnt)

        _lcf *= prime ** maxCnt

    return _lcf


print lcf(range(1, 21))
