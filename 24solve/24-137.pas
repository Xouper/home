﻿// Автор В.Н. Шубинкин
##
ReadLines('24-s1.txt').Where(s -> s.Count(t -> t = 'J') > s.Count(t -> t = 'E')).Count.Print;

// Вместо Count(t -> t = 'J') можно было бы воспользоваться CountOf('J'),
// но на экзамене может быть установлена недостаточно свежая версия PascalABC.NET

// Научиться программировать в таком стиле можно на бесплатном курсе Александра Осипова
// "PascalABC.NET: современный код" на платформе Stepik