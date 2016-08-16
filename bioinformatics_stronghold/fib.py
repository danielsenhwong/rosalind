# Bioinformatics Stronghold
# Problem fib

n = 31
k = 2
r = range(2,n)
f = []
f.append(1)
f.append(1)
for i in r:
    f.append(f[i-1] + (k * f[i-2]))

print f[-1]
