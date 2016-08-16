f = open('rosalind_hamm.txt', 'r')
l = f.readlines()
f.close()

s = l[0]
t = l[1]
r = range(0, len(s))

dh = 0
for i in r:
    if s[i] != t[i]:
        dh = dh + 1

print dh
