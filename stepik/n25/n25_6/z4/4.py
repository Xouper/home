# Рассматриваются целые числа, принадлежащие числовому отрезку [416782; 498324], которые представляют собой произведение
# трёх различных простых делителей, оканчивающихся на одну и ту же цифру. В ответе через пробел запишите количество таких
# чисел и разницу между максимальным и минимальным из них.
def isprime(n):
    d = 2
    while d * d < n:
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
            if len(my_list) > 3:
                return 0
        d += 1
    if d * d == n and isprime(d):
        my_list.append(d)
    proizved = 1
    for x in my_list:
        proizved = proizved * x
    if len(my_list) == 3 and proizved == n:
        return my_list


k = 0
minim = 10**10
maxim = 0
for i in range(416782, 498324+1):
    f = deliteli(i)
    if f != 0 and f is not None and f[0] % 10 == f[1] % 10 == f[2] % 10:
        k += 1
        minim = min(minim, i)
        maxim = i
print(k, maxim-minim)
