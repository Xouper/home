for a in range(-1000, 10001):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if not (((y + 2*x) < a) or (x > 20) or (y > 30)):
                fl = False
                break
        if not fl:
            break
    if fl:
        print(a)
