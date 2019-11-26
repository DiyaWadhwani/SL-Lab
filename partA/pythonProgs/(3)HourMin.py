def hoursMinutes(n):
    h=n//60
    m=n%60
    s=str(h)+":"+str(m)
    return s
num=int(input("Enter time: "))
print(hoursMinutes(num))
