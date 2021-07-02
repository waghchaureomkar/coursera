#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below


name = input("Enter file:")
fh = open(name)
#fh = open('mbox.txt')
di = dict()
for line in fh:
    if  not line.startswith('From '): continue
    line = line.rstrip()
    words = line.split()
    wd = words[5]
    w = wd.split(":")
    #print(w[0])
    x = w[0]
    di[x] = di.get(x,0)+1
#print(di)
for k,v in sorted(di.items()):
    print(k,v)
    
