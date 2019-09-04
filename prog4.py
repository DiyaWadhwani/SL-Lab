class Person :
	def __init__(self,name,age) :
		self.name=name;
		self.age=age;

p1=Person('Deeksha',20)
p2=Person('Diya',19)
print("\nName of Person #1 is",p1.name)
print("\nAge of Person #1 is",p1.age)
print("\nName of Person #2 is",p2.name)
print("\nAge of Person #2 is",p2.age)
p2.age=10
print("\nModified age of Person #2 is",p2.age,"\n")

