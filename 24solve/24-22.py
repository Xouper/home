# Автор: А.Н. Носкин

""" идея А.М. Кабанов"""
with open("k7a-2.txt") as F:
  s = F.readline() # считали строку

k = 0 # начальная длина цепочки из "A,С, D"
Max = 0 # макс длина цепочки из "A,С, D"
for c in s:
  if c in 'ACD':
    k += 1
    if k > Max:
      Max = k # перезаписали Макс длину
  else:
      k = 0 # другая буква - сбрасываем счетчик
print(Max)








