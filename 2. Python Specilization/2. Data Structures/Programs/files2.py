#EX.7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x = 0
y = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x= x + 1
    ls = line.find('0')
    z = float(line[ls:])
    y = y + z
    #print(line)
    #print(x)
    #print(y)
print("Average spam confidence:",y/x)
