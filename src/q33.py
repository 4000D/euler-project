import _gcf
from operator import truediv


def f(u1, u2, d1, d2) :
    org = truediv(u1*10 + u2, d1*10 + d2)
    t1 = truediv(u1, d2) if d2 != 0 else -1
    t2 = truediv(u2, d1) if d1 != 0 else -1
    return org == t1 or org == t2

u = 1
d = 1

for _u1 in range (1, 10) :
    for _u2 in range (0, 10) :
        for _d1 in range (1, 10) :
            for _d2 in range(0, 10) :
                if _u1 != _d1 and _u2 != _d2 and _u1 * 10 + _u2 < _d1 * 10 + _d2 and f(_u1, _u2, _d1, _d2) :
                    u *= _u1 * 10 + _u2
                    d *= _d1 * 10 + _d2
                    print 'u :', _u1, _u2
                    print 'd :', _d1, _d2

print d / _gcf.gcf(u, d)

