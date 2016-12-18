import _fib

i = 0

while True :
    if len(str(_fib.fib(i))) == 1000 :
        break
    i += 1

print i
