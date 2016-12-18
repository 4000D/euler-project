
def isPalindrome(s) : # s must be string
    for i in range(len(s)/2) :
        if s[i] != s[-i-1] :
            return False

    return True # or return s == s[::-1]

MAX = int(1e6)
ans = 0

for i in range(MAX + 1) :
    if isPalindrome(str(i)) and isPalindrome(bin(i)[2:]) :
        ans += i

print ans
