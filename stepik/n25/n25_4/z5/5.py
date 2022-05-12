def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def kpdel(n):
    d = 2
    my_deliteli = []
    while d * d < n:
        if n % d == 0:
            if isprime(d):
                my_deliteli.append(d)
            if isprime(n // d):
                my_deliteli.append(n // d)
        d += 1
    return sum(my_deliteli)


k = 0
for i in range(650000, 1000000):
    S = kpdel(i)
    if S % 11 == 0 and S != 0:
        print(i, S, end=' ')
        k += 1
        if k == 5:
            break