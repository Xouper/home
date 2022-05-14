def kdel(n):
    k = 1
    d = 2
    while d * d < n:
        if n % d == 0:
            if d % 2 == 0:
                k += 1
            if (n // d) % 2 == 0:
                k += 1
            if k > 3:
                return False
        d += 1
    if d * d == n and d % 2 == 0:
        k += 1
    if k == 3:
        return True
    else:
        return False


for i in range(101000000, 102000000+1, 2):
    if int((i //2) ** 0.5) == (i // 2) ** 0.5:
        f = kdel(i)
        if f:
            print(i, end=' ')

