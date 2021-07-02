#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for 
#the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate 
#of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to 
#convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.


sh = input('enter hour:')
sr = input('enter rate:')
try:
    fh = float(sh)
    fr = float(sr)
except:
    print('error,enter numric input')
    quit()
print ('hour:',fh,'rate:',fr)
if fh > 40 :
    a = (fh - 40.0) * (fr * 1.5)
    b = (40 * fr)
    Pay = a + b
else :
    Pay = fh * fr
print (Pay)