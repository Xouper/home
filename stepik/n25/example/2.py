def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def our_del(n):
    d = 2
    my_del = []
    chet_del = [0]
    nechet_del = [0]
    while d * d < n:
        if n % d == 0:
            if d % 2 == 0:
                chet_del.append(d)
            else:
                nechet_del.append(d)
            if n // d == 0:
                chet_del.append(n // d)
            else:
                nechet_del.append(n // d)
        d += 1
    if d * d == n:
        if d % 2 == 0:
            chet_del.append(d)
        else:
            nechet_del.append(d)
    my_del.append(max(chet_del))
    my_del.append(max(nechet_del))
    return my_del


k = 0
for i in range(250156, 500000):
    deliteli = our_del(i)
    if deliteli != [0,0]:
        razn = abs(deliteli[0] - deliteli[1])
        if isprime(razn) and razn % 10 == 9:
            print(i, razn, end=' ')
            k += 1
            if k == 5:
                break
