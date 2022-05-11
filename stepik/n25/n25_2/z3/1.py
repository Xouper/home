def f(n):
    d = 2
    kd = 2
    my_list = []
    my_list.append(1)
    while d * d < n:
        if n % d == 0:
            my_list.append(d)
            my_list.append(n // d)
            kd += 2
        d += 1
    if d * d == n:
        my_list.append(d)
        kd += 1
    if sum(my_list) > n:
        return 1
    else:
        return 0

k = 0
for i in range(2, 20000+1):
    if f(i) == 1:
        k += 1
print(k)