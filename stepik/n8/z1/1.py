letters = '0123456789'
chet = '02468'
nechet = '13579'
k = 0
for x1 in '2468':
    for x2 in nechet:
        for x3 in chet:
            for x4 in nechet:
                for x5 in chet:
                    for x6 in nechet:
                        for x7 in chet:
                            for x8 in nechet:
                                if x1 != x3 and x1 != x5 and x1 != x7 and x3 != x5 and x3 != x7 and x5 != x7:
                                    if x2 != x4 and x2 != x6 and x2 != x8 and x4 != x6 and x4 != x8 and x6 != x8:
                                        if x8 == '5':
                                            k += 1

for x1 in nechet:
    for x2 in chet:
        for x3 in nechet:
            for x4 in chet:
                for x5 in nechet:
                    for x6 in chet:
                        for x7 in nechet:
                            for x8 in chet:
                                if x1 != x3 and x1 != x5 and x1 != x7 and x3 != x5 and x3 != x7 and x5 != x7:
                                    if x2 != x4 and x2 != x6 and x2 != x8 and x4 != x6 and x4 != x8 and x6 != x8:
                                        if x8 == '0':
                                            k += 1
print(k)