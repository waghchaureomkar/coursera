#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program 
#creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
fh = open(name)
count = dict()
wd =list()
for line in fh :
    line = line.rstrip()
    words = line.split()
    if not line.startswith("From ") : continue
    #print(words[1])
    wd.append(words[1])
    #for word in words:
        #count[word]= count.get(word,0)+1
#print(wd)
for x in wd :
    count[x]= count.get(x,0)+1
print(count)
largest = -1
theword = None
for k,v in count.items():
    if v > largest :
        largest = v
        theword = k
print(theword,largest)
