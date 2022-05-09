f = open('24-1.txt').read()
k = 0
m = 0
tec = 0
flag = -1
for i in range(len(f)-1):
    if f[i] < f[i+1] and flag == -1:
        k += 1
        if k > m:
            m = k
            tec = i
    else:
        k = 1
print(tec - m + 3)



