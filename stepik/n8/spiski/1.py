letters = 'АМРТ'
my_list = []
k = 0
for x1 in letters:
    for x2 in letters:
        for x3 in letters:
            for x4 in letters:
                    k += 1
                    word = x1+x2+x3+x4
                    if k == 250:
                        print(word)