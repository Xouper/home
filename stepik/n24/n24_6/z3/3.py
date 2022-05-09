f = open('24-5.txt').read()
k = 0
m = 0
step = 0
for i in range(len(f)-1):
    if f[i+step] + f[i+step+1] == '()':
        k += 1
        m = max(m, k)
        step += 1
    else:
        k = 0
        step = 0
print(m)