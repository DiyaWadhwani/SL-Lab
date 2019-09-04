class Person :
	def __init__(self,name,age) :
		self.name=name;
		self.age=age;

p1=Person('Diya',19)

print("\nName of Person is",p1.name)
print("\nAge of Person is",p1.age)
print("\n**Printing after deleting age attribute for p1**")
del p1.age
print("\nName of Person is",p1.name)
#print("\nAge of Person is",p1.age) errorr!!!
p1.age=10
print("\nNew age of Person is",p1.age,"\n")
del p1
print(p1.name)

