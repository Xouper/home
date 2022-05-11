def f(n):
    my_del = []
    d = 2
    while d * d < n:
        if n % d == 0:
            my_del.append(d)
            my_del.append(n // d)
        if len(my_del) == 2:
            m = my_del[1] - my_del[0]
            if m % 100 == 18:
                return m
            else:
                return -1
        d += 1

k = 0
for i in range(860001, 1000000):
    if f(i) != -1 and f(i) is not None:
        print(i, f(i))
        k += 1
        if k == 5:
            break

