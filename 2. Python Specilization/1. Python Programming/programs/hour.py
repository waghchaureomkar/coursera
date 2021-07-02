sh = input('enter hours:')
sr = input('enter rate:')
try:
    fh = float(sh)
    fr = float(sr)
except:
    print('error, plz enter numeric input')
    quit()
print(fh,fr)
if fh > 40 :
    reg = fr * fh
    otp = (fh - 48.0) * (fr * 0.5)
    xp = reg + otp 
else:
    xp = fh * fr
print('Pay:',xp)  