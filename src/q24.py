'''
find a_i where 1M = sum of a_i * i! 
answer is [a_9][a_8] .... [a_0]
'''
import _fib

K = int(1e6)

A = [0] * 10
F = sorted([_fib.fib(i) for i in range(10)], reverse=True)

for i in range(10) :
    while K > F[i] :
        K -= F[i]
        A[i] += 1

L = range(10)
for a in A :
    print L.pop(a)
