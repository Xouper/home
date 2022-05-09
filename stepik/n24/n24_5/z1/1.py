f = open('24-j9.txt').read()
k = 0
for i in range(len(f)//2):
    if f[i] == f[len(f)-i-1]:
        k += 1
print(k)
