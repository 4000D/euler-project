def word2pt(w, dic) :
    return sum([dic[c] for c in w])

dic = {chr(i) : i - 97 + 1 for i in range(97, 122 + 1)}
names = []

with open('names.txt') as f :
    for line in f :
        names.extend([w[1:-1].lower() for w in line.split(',')])

names.sort()

ans = 0

for i in range(len(names)) :
    ans += (i+1) * word2pt(names[i], dic)

print ans







