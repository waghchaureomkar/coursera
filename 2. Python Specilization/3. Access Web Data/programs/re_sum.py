#name = input('enter the file name:')
#fh = open(name)
import re
fh = ('Why should you learn to write programs? 7746 12 1929 8827 Writing programs (or programming) is a very creative  7 and rewarding activity.  You can write programs for  many reasons, ranging from making your living to solving 8837 a difficult data analysis problem to having fun to helping 128 someone else solve a problem.  This book assumes that  everyone needs to know how to program ...')
#fh = open('re_sum.txt')
#for line in fh:
    #line = line.rstrip()
x = re.findall('[0-9]+',fh)
#print(x)
sum = 0
for y in x:
    z = int(y)
    sum = sum + z
print(sum)