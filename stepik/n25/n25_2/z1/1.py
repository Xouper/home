def delit(n):
    d = 2
    kd = 0
    list_of_del = []
    while d * d < n:
        if n % d == 0:
            list_of_del.append(d)
            list_of_del.append(n // d)
            kd += 2
        if kd > 6:
            return list_of_del
        d += 1
    if d * d == n:
        list_of_del.append(d)
        kd += 1
    return list_of_del


k = 0
minim = 6 * 10**7 + 1
for i in range(50000000, 60000000+1):
    if i % 911 == 0:
        deliteli = delit(i)
        if len(deliteli) == 6 and 911 in deliteli:
            k += 1
            minim = min(minim,i)
print(k, minim)


# def delit(n):
#     d = 2
#     kd = 0
#     while d * d < n:
#         if n % d == 0:
#             kd += 2
#         if kd > 6:
#             return kd
#         d += 1
#     if d * d == n:
#         kd += 1
#     return kd
#
#
# k = 0
# minim = 6 * 10**7 + 1
# for i in range(50000000, 60000000+1):
#     if i % 911 == 0:
#         if delit(i) == 6:
#             minim = min(minim, i)
#             k += 1
# print(k, minim)