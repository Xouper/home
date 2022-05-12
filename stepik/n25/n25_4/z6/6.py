def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def result(n):
    d = 2
    my_del = []
    while d * d < n:
        if n % d == 0:
            my_del.append(d)
            my_del.append(n // d)
            if len(my_del) == 2 and isprime(my_del[-1]) is False:
                return my_del[-1]
        d += 1
    return 0

k = 0
for i in range(650001, 1000000):
    ans = result(i)
    if ans != 0:
        print(i, ans, end=' ')
        k += 1
        if k == 6:
            break
