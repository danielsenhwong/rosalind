from __future__ import division
f = open('rosalind_gc (3).txt', 'r')
fasta = f.readlines()
f.close()

r = range(0, len(fasta))
temp_id = str()
d = {}

for i in r:
    if fasta[i][0] != '>':
        if temp_id in d:
            d.update({temp_id: d[temp_id] + fasta[i].replace('\n', '')})
        else:
            d[temp_id] = fasta[i].replace('\n', '')
    else:
        temp_id = fasta[i][1:len(fasta[i])]

d_gc = {}
for key, value in d.items():
    d_gc[key] = (((value.count('G') + value.count('C')) / len(value)) * 100)

max_gc = max(d_gc, key=d_gc.get)
print(max_gc + ' ' + str(d_gc[max_gc]) + '%')

