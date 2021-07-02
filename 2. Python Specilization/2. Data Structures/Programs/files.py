#ex7.1  Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for lx in fh:
    ly = lx.rstrip()
    inp = ly.upper()
    print(inp)
#inp = fh.read()
#up=inp.upper()
#print(up)
