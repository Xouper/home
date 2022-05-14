def deliteli(n):
    d = 2
    my_deliteli = []
    mindel = n
    while d * d < n:
        if n % d == 0:
            my_deliteli.append(d)
            my_deliteli.append(n // d)
            if mindel == n:
                mindel = d
        d += 1
    if d * d == n:
        my_deliteli.append(d)
    my_deliteli.sort()
    flag = 1
    for y in range(len(my_deliteli) - 1):
        if my_deliteli[y] + 10 == my_deliteli[y+1]:
            flag += 1
    if flag == len(my_deliteli):
        return mindel
    else:
        return -1


for i in range(854321, 1087654+1):
    f = deliteli(i)
    if f != -1 and f != i:
        print(i, f, end=' ')