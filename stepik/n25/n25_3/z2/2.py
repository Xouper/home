def f(n):
    my_del = []
    d = 2
    while d * d < n:
        if n % d == 0:
            my_del.append(d)
            my_del.append(n // d)
        d += 1
        if len(my_del) == 2:
            m = my_del[1] - my_del[0]
            if m % 7 == 0 and m != 0:
                return m
            else:
                continue

k = 0
for i in range(850001, 1000000):
    if f(i) != -1 and f(i) is not None:
        print(i, f(i), end=' ')
        k += 1
        if k == 6:
            break
