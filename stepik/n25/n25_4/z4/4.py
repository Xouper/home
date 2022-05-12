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
    return my_deliteli


for i in range(25317, 51237+1):
    deliteli = kpdel(i)
    if len(deliteli) >= 6:
        print(i, max(deliteli), end=' ')
