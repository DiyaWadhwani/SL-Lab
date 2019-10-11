#prog for a temperature converter, menu driven

def CtoF(temp):
	ftemp=temp*(9/5)+32
	return ftemp

def FtoC(temp):
	ctemp=(temp-32)*(5/9)
	return ctemp

def CtoK(temp):
	ktemp=temp+273.15
	return ktemp

def KtoC(temp):
	ctemp=temp-273.15
	return ctemp
	
print("Temperature converter\n1.Celsius to Farenheit\n2.Farenheit to Celsius\n3.Celsuis to Kelvin\n4.Kelvin to Celsius\n5.Exit")
choice=input("Enter your choice:")
if choice=='5':
	exit(0)
temp=float(input("Enter the temperature:"))

if choice=='1':
	print(CtoF(temp))
elif choice=='2':
	print(FtoC(temp))
elif choice=='3':
	print(CtoK(temp))
elif choice=='4':
	print(KtoC(temp))
else:
	print("Enter valid choice")
	

