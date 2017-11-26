# Brute Force

import os

def f(a): # sub main func
    startTime = os.times()[-1]

    _max = a ** 2
    _ret = 0

    n = 0
    while True:
        n += 1

        r1 = ((a-1) ** n) % _max
        r2 = ((a+1) ** n) % _max

        _ret = max(_ret, (r1 + r2) % _max)


        if r1 == r2:
            endTime = os.times()[-1]
            print("f(%d) elapsed %.3f sec" % (a, endTime - startTime))
            return _ret


def main():
    startTime = os.times()[-1]
    ret = sum([f(a) for a in range(3, 1000 + 1)])
    endTime = os.times()[-1]
    print("total elapsed %.3f sec" % (endTime - startTime))
    print("Answer : %d" % ret)


if __name__ == '__main__':
    main()
