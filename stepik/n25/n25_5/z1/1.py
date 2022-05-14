def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def deliteli(n):
    d = 2
    my_list = []
    while d * d < n:
        if n % d == 0:
            if isprime(d):
                my_list.append(d)
            if isprime(n // d):
                my_list.append(n // d)
        d += 1
    if d * d == n and isprime(d):
        my_list.append(d)
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            for z in range(j+1, len(my_list)):
                if my_list[i] * my_list[j] * my_list[z] == n:
                    return True
    return False

k = 0
minim = 10**10
for m in range(158928, 345293+1):
    ans = deliteli(m)
    if ans == True:
        if minim == 10**10:
            minim = m
        k += 1
print(k, minim)