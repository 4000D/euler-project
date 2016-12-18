L = [1,2,5,10,20,50,100,200]
memo = [[-1 for i in range(len(L) + 1)] for j in range (201)]
def f(_p, i) :
    print 'p, i :', _p, i
    if _p > 200 : return 0
    if i == len(L) : 
        return _p == 200

    if memo[_p][i] != -1 : return memo[_p][i]

    memo[_p][i] = f(_p + L[i], i) + f(_p, i+1)
    return memo[_p][i]


print f(0, 0)
