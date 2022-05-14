x = []
maxk = 0
for i in range(3, 65, 2):
    x.append(i**3)
for i in range(228224, 531135+1):
    k = 0
    for j in x:
        if i % j == 0 and i != j:
            k += 1
            maxk = j
    if k >= 4:
        print(i, k, maxk, end=' ')