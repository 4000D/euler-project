import _factorial

MAX = int(1e5)
ans = 0

for i in range (3, MAX) :
    if i == sum([_factorial.fact(int(c)) for c in str(i)]) :
        ans += i
        print i
 
print ans
