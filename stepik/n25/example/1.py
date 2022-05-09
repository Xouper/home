def koldel(n):
    d = 2
    masdel = []
    masdel.append(1)
    masdel.append(n)
    while d * d < n:
        if n % d == 0:
            masdel.append(d)
            masdel.append(n // d)
        d += 1
    if d * d == n:
        masdel.append(d)
    return masdel



for i in range(193136, 193223 + 1):
    f = koldel(i)
    if len(f) == 6:
        f.sort()
        print(i, f)