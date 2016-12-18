MAX = int(1e6)
ans = 0

for i in range (2, MAX) :
    if i == sum([int(c) ** 5 for c in str(i)]) :
        ans += i
        print i

print ans


