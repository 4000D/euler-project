# f(n) = 4 * n^2 + (n-1) * (1 + 2 + 3) + f(n-1)
# f(1) = 1

def f(n) :
    if n <= 1 : return 1

    return 4 * n ** 2 + 6 * (n-1) + f(n-1)

n = 1001
_f = 1
i = 1

while i < n :
    i += 2
    _f += 4 * i ** 2 - 6 * (i - 1)

print _f
