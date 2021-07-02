#Ex.8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
fname = input("Enter file name: ")
fh = open(fname)
#y = None
z = list()
for line in fh :
    lst = line.rstrip()
    x = lst.split()
    for y in x :
        z.append(y)
#print(z)
seen = set()
result = []
for item in z:
    if item not in seen:
        seen.add(item)
        result.append(item)
result.sort()
print(result)

