def f(n):
    d = 2
    mindel = 10 ** 10
    while d * d <= n:
        if n % d == 0:
            if d % 10 == 8 and d != 8:
                mindel = min(mindel, d)
            elif (n // d) % 10 == 8 and (n // d) != 8:
                mindel = min(mindel, n // d)
        d += 1
    return mindel


k = 0
for i in range(500001, 10 ** 10):
    x = f(i)
    if x != 10 ** 10:
        print(i, x)
        k += 1
        if k == 5:
            break
