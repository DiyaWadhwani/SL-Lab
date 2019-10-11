def oddRange(n1,n2):
    l=[]
    for i in range(n1,n2+1):
        if i%2!=0:
            l.append(i)
    return l
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
print(oddRange(num1,num2))
