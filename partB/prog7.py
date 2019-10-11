#to read list of elements

el = input("Enter list of elements : ")
el = el.split(' ')

def remove_dups(list1):
	list2=[]
	for item in list1:
		if item not in list2:
			list2.append(item)
	return list2

print(remove_dups(el))
	
