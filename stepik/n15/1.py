for a in range(-100,1000):
    fl = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (((y**2 <= a) <= (y < 12)) and ((x < 11) <= (x**2 < a))) == False:
                fl = False
                break
        if fl == False:
            break
    if fl == True:
        print(a)