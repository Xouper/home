def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def kdel(n):
    d = 2
    my_del = [0]
    while d * d < n:
        if n % d == 0:
            if isprime(d) and isprime(n // d):
                my_del.append(d)
                my_del.append(n // d)
        d += 1
    return my_del


maxim = 0
k = 0
for i in range(125697, 190234+1):
    f = kdel(i)
    if len(f) != 1:
        f.remove(0)
        k += 1
        maxim = max(maxim, i)
print(k, maxim)
