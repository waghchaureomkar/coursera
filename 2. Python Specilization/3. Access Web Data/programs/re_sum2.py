name = input('enter the file name:')
fh = open(name)
import re
#fh = open('re_sum2.txt')
ls = list()
for line in fh:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    s = 0
    for n in x:
        num = int(n)
        if s == 0:
            s = num
            continue
        s = num + s
    ls.append(s)
#print(ls)
sum = 0
for no in ls:
    if sum == 0:
        sum = no
        continue
    sum = sum + no
print(sum)
