import math

target = 600851475143
div = 2

while target != 1:
    while target % div == 0 :
        target /= div
    div += 1 # for better performance, seive div

print div - 1
