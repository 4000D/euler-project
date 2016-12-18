def gcf(a, b) :
    if a < b : return gcf(b, a)
    if b == 1 : return a

    if a % b == 0 : return b
    return gcd(b, a%b)

    
