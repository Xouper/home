my_set = set()
my_list = [int(i) for i in range(50,101)]
for n in range(4, 1000):
    n2 = bin(n)[2:]
    if n2.count('1') > n2.count('0'):
        n2 = n2 + '0'
    else:
        n2 = n2 + '1'
    if len(n2) % 2 == 0:
        n2 = n2[:int(len(n2) / 2) - 1] + n2[int(len(n2) / 2) + 1:]
    else:
        n2 = n2[:int(len(n2) / 2) - 1] + n2[int(len(n2) / 2) + 2:]
    if int(n2, 2) in my_list:
        my_set.add(int(n2, 2))
print(len(my_set))
