def sistem(num, base):
    new_num = ''
    while num > 0:
        new_num = str(num % base) + new_num
        num //= base
    return new_num

s = 8**4024 - 4**1605 + 2**1024 - 126
print(sistem(s,2).count('1'))