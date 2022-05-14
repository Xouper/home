def kdel(n):
    d = 2
    k = 0
    while d *d < n:
        if n % d == 0:
            k += 2
        d += 1
    if d * d == n:
        k += 1
    if k % 13 == 0:
        return k
    else:
        return 0


for i in range(26600, 28100+1):
    f = kdel(i)
    if f != 0:
        print(i, f, end=' ')