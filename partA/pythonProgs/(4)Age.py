from datetime import date,datetime
def ageConvert(d,m,y):
    dob=date(y,m,d)
    today=date.today()
    return today-dob
d=int(input("Enter day: "))
m=int(input("Enter month: "))
y=int(input("Enter year: "))
print("Age: ",ageConvert(d,m,y).days//365)
