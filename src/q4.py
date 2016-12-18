import math

def check(num) :
    arr = [int(i) for i in str(num)]

    for i in range(len(arr) / 2) :
        if arr[i] != arr[-i-1] : return False

    return True

_max = 0

for i in range(100, 1000) :
    for j in range(i, 1000) :
        if check(i * j) :
            _max = max(_max, i*j)
