str1=input("Enter string ")
print("String length : ",len(str1));
a=slice(0,10,3)
print(str1[a])


x=["hello",4,"whatsup"];
print ("x=",x)
y=["Diya",20,x];
print ("y=",y)
print("sliced list:",y[1:3])
y[1]="Mango"
print("newlist :",y)
print("concatenated list:",x+y[:2])

#to copy or clone a list
#method 1: 
y=[4,5,"nice"]
y=list(y) 
print("new list:",y)
#method 2:
import copy
y=copy.copy(y)
print("new list:",y)
