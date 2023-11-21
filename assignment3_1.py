hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter rate per hour")
r = float(rate)
if h<=40:
    l=h*r
    print(l)
else :
    u=40*r
    h=h-40
    h=h*r*1.5
    h=u+h
    print(h)
