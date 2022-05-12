def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


k = 1
for i in range(2943444,2943529+1):
    if isprime(i):
        print(k, i, end=' ')
        k += 1