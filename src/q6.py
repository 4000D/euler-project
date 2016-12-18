
SoSq = sum(map(lambda x : x ** 2 , range(1, 100 + 1)))
SqoS = ( (1 + 100) * 100 / 2 ) ** 2

print abs(SoSq - SqoS)
