F = [1, 1, 1]

def fib(n) :
    if len(F) >  n : return F[n]
    F.append(fib(n-1) + fib(n-2))
    return F[n]

