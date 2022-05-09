f = open('k7b-2.txt').read()
k = 0
kmax = 0
for i in range(len(f)):
    if (k%4==0 and f[i] == 'D') or (k%4==1 and f[i] == 'B') or (k%4==2 and f[i] == 'A') or (k%4 == 3 and f[i] == "C"):
        k += 1
        kmax = max(kmax,k)
    else:
        k = 1
print(kmax)
