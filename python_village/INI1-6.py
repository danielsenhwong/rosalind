# INI1
import this

# INI2
a = 906
b = 810
output = a**2 + b**2
print(output)

# INI3
text = 'LYTPlatemysigf1TW8lD9UZ0qkpLbGQ1XygGCKiWZ5s40DP0au09p6lJPfl9s3KPwLvC073LjHDUNyPZ5rIX7DWx1FDeFV3SqgiuIoXfkXv8pJHKifK15ziffNFqvPswmurinuserjni6dyQjDnPWKzib16cFSN.'
a = 3
b = 10
c = 128
d = 134
output = text[a:b+1] + ' ' + text[c:d+1]
print(output)

# INI4
total = 0
a = 4625
b = 9225
r = range(a, b+1)
for i in r:
    if i % 2 == 1:
        total = total + i

print(total)

# INI5
f = open('/Users/dsw2107/Downloads/rosalind_ini5 (3).txt', 'r')
l = f.readlines()
lines = range(1,len(l)+1,2)
j = open('/Users/dsw2107/Downloads/rosalind_ini5_out.txt', 'w')
for n in lines:
    j.write(l[n] + '\n')

j.close()

# INI6
s = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
l = len(s)
d = {}
for word in s.split(' '):
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
 
for key, value in d.items():
    print(key + ' ' + str(value) + '\n')

