﻿// Автор: В.Н. Шубинкин

begin
  var s := ReadAllText('24-2.txt');
  var k := 1;
  var maxim := 0;
  var pos := 1;
  for var i := 2 to length(s) do
    if s[i] > s[i - 1] then
    begin
      k += 1;
      if k > maxim then
      begin
        maxim := k;
        pos := i;
      end
    end
    else k := 1;
  write(pos - maxim + 1)
end.