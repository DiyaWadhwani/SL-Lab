#list of even numbers and reversing them
list1=input("Enter list of numbers :")
list1=list1.split(' ')
list2=[x for x in list1 if int(x) % 2 == 0]
print("List of even numbers : ",list2)
list2.reverse()
print("Reversed list :",list2)
