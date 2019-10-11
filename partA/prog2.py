students={'1MS17IS039':'Deeksha','1MS17IS040':'Dhruthick','1MS17IS041':'Diya','1MS17IS148':'Harshubh'}
list=["value1","value2","value3","value4"]
list2=[]
j=0
for i in students:
	print("key is ",i," Value is ",students[i])
	list[j]=students[i]
	#list2[j]=i
	j=j+1

print(list)
#print(list2)
print(students.keys())
print(students.values())
print(students.items())
