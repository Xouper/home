for n in range(100, 300):
    n2 = bin(n)[2:]
    if n2.count('0') == n2.count('1'):
        n2 = n2 + n2[-1]
    elif n2.count('0') > n2.count('1'):
        n2 = n2 + '1'
    else:
        n2 = n2 + '0'
    if n2.count('0') == n2.count('1'):
        n2 = n2 + n2[-1]
    elif n2.count('0') > n2.count('1'):
        n2 = n2 + '1'
    else:
        n2 = n2 + '0'
    if n2.count('0') == n2.count('1'):
        n2 = n2 + n2[-1]
    elif n2.count('0') > n2.count('1'):
        n2 = n2 + '1'
    else:
        n2 = n2 + '0'
    if int(n2,2) % 4 == 0:
        print(n)
