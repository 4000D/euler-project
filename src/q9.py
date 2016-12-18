def f(a) :
    for _b in range(a+1, 1000) :
        _c = 1000 - _b - a

        b = min(_b, _c)
        c = max(_b, _c)

        if a ** 2 + b ** 2 == c ** 2 :
            return a * b * c

    return False


for i in range (1, 999) :
    ret = f(i)

    if ret :
        print ret
        break 





