
maxNum = 1000

checkRule = lambda x : (x % 3 == 0) or (x % 5 == 0)

answers = [x for x in range(1, maxNum) if checkRule(x)]

print sum(answers)

