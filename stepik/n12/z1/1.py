s = '1' * 201
while '1111' in s:
    s = s.replace('1111', '22', 1)
    s = s.replace('222', '1', 1)
print(s)
print(s.count('1'))