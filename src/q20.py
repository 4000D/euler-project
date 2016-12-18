memo = [1]

def fib(n) :
    if len(memo) - 1 < n : 
        memo.append( n * fib(n-1))
    return memo[n]

print sum([int(s) for s in str(fib(100))])
