f = open('24-157.txt').read().split('QW')
m = 0
for i in f:
    m = max(m, len(i))
print(m+2)