# Brute Force

import os
import math

def test(n):
    if n < 10:
        return False

    _n = n
    digits = 0 # sum of digits

    # calc `digits`
    while n > 0:
        n, r = n / 10, n % 10
        digits += r

    n = _n

    if n == 1 and digits == 1: return True
    if digits == 1: return False

    # check n ^ k == digits wrt some k.
    # math.log can't be used due to floating point calculation...
    while n % digits == 0:
        n = n / digits

    return n == 1

def main():
    startTime = os.times()[-1]

    l = [i ** j for i in range(1, 100) for j in range(1, 10)]
    l = filter(test, list(set(l)))
    l = sorted(l)

    endTime = os.times()[-1]

    print("Answer : %d" % l[29])
    print("elapsed time: %.4f sec" % (endTime - startTime))

if __name__ == '__main__':
    main()
