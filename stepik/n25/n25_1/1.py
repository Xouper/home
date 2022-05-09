import time

t = time.time()
def deliteli(n):
    d = 2
    kd = 0
    del_list = []
    while d * d < n:
        if n % d == 0:
            kd += 2
            del_list.append(d)
            del_list.append(n // d)
        d += 1
    if d * d == n:
        del_list.append(d)
    return del_list

maxim = 0
for i in range(123456789, 223456789+1):
    if i ** 0.5 == int(i ** 0.5):
        f = deliteli(i)
        if len(f) == 3:
            f.sort()
            print(i, f, f[-1])
print(time.time()-t)