def f(n):
    d = 2
    chet = 1
    while d * d < n:
        if n % d == 0:
            if d % 2 == 0:
                chet += 1
            if (n // d) % 2 == 0:
                chet += 1
            if chet > 3:
                return chet
        d += 1
    if d * d == n and d % 2 == 0:
        chet += 1
    return chet


k = 0
for i in range(101000000, 102000000+1):
    if i % 2 == 0:
        if f(i) == 3:
            print(i)