for a in range(1, 100):
    fl = True
    for x in range(1, 1000):
        if ((x & 85 == 0) <= ((x & 54 != 0)<= (x & a != 0))) == False:
            fl = False
    if fl == True:
        print(a)
