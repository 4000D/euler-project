memo = [1,2]

while memo[-1] < 4e6 :
    memo.append(memo[-1] + memo[-2])

print sum([x for x in memo if x % 2 == 0])

""" SHORT VERSION

"""

