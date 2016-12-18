memo = [1]

u'''
confused Factorial with Fibonacci until Q25
'''
def fact(n) :
    if len(memo) > n : return memo[n]
    memo.append(n * fact(n-1))
    return memo[n]
