def computepay(h,r):
    if h > 40 :
        a = (h - 40.0) * (r * 1.5)
        b = (40 * r)
        c = a + b 
    else:
        c = h * r
    return c
hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
    p = computepay(h,r)
except:
    print('error, enter numeric output:')
    quit()
print("Pay",p)