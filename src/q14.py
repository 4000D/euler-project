# use DP

dic = {1 : 1}

def calc(n) :
    if n in dic : return dic[n]

    if n % 2 == 0 :
        dic[n] = 1 + calc(n / 2)
    else :
        dic[n] = 1 + calc(3 * n + 1)
    return dic[n]

_max = 0
_i = 1

for i in range(1, int(1e6) + 1) :
    if _max < calc(i) :
        _max = dic[i]
        _i = i
    

print _max, _i
