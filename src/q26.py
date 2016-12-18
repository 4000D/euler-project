def calc(d) :
    if d % 10 == 0 : return 1

    R = [1]
    ans = 0

    while ans == 0 :
        _r = R[-1]

        if _r == 0 : return 0

        while _r / d == 0 :
            _r *= 10

        _r %= d

        if _r in R :
            ans = len(R) - R.index(_r)
        else :
            R.append(_r)

    return ans

ans = 0
max = 0

for i in range(1, 1000) :
    _max = calc(i)
    if max < _max :
        print 'max, i : ', _max, i
        max = _max
        ans = i

print ans

