import math
import _primarity

dict = {}
MAX = 1000000

def getNums(i) :

    ret = []
    s = str(i)

    for _i in range(len(s)) :
        s = s[1:] + s[0]
        ret.append(int(s))

    return ret

for i in range (1, MAX + 1) :
    if i not in dict or i % 10 != 0 :
        nums = getNums(i)
        r = [_primarity.test(num) for num in nums]

        if len([v for v in r if v]) == len(nums) :
            for num in nums :
                dict[num] = True

print sum([1 for v in dict.values() if v])
