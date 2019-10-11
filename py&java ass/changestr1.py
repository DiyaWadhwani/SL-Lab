def Change(str2):
	x = list(str2)
	y=[]
	vowels=['a','e','i','o','u']
	for i in range (0,len(str2)):
		if x[i]=='Z':
			x[i]=='a'
		else :
			y.append(ord(x[i])+1)
			x[i]=chr(y[i])
		if x[i] in vowels:
			x[i]=x[i].upper()
	return "".join(x)
	
str1 = str(input("Enter string:\n"))
print("New String is : ",Change(str1))
