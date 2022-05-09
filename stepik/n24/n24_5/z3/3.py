f = open('24-153.txt').read()
# tec = 0
# k = 0
# last = 0
# flag = -1
# for i in range(len(f)):
#     if f[i] == 'A' and flag == -1:
#         tec = i
#         flag = 0
#     elif f[i] == 'A' and flag != -1:
#         continue
#     elif f[i] == 'F' and flag == 0:
#         last = i
#         flag = -1
#     if 6 <= last - tec <= 10:
#         k += 1
#         last = 0
#         tec = 0
# print(k)
k = 0
for i in range(len(f)-5):
    if f[i] == 'A':
        for z in range(i+6, i + 10):
            if f[z] == 'F':
                k += 1
print(k)
