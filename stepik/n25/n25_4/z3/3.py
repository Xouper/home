def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def kpdel(n):
    d = 2
    k = 0
    while d * d < n:
        if n % d == 0:
            if isprime(d):
                k += 1
            if isprime(n // d):
                k += 1
        d += 1
    if d * d == n and isprime(d):
        k += 1
    return k


result = 0
for i in range(2, 20000+1):
    f = kpdel(i)
    if f > 3 and isprime(i) is False:
        result += 1
print(result)
