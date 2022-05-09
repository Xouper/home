f = open('24-157.txt').read()
f = f.replace('RP', '1')
f = f.replace('PR', '1')
f = f.split('1')
m = 0
for i in f:
    m = max(m, len(i))
print(m+2)