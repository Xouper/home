# проблема если послелний элемент число
f = open('24-1.txt').read()
l = []
num = ''
for i in range(len(f)):
    if f[i].isdigit() :
        num = num + f[i]
    elif num != '':
        l.append(num)
        num = ''
for x in l:
    if int(x) % 2 ==  0:
        l.remove(x)
print(min(l))