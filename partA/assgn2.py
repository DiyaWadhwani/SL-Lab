class Student:
	def __init__(self,name,age,marks):
		self.name=name
		self.age=age
		self.marks=marks
		
	def display (self):
		print("\nName is",self.name,"\nAge is",self.age,"\nMarks are",self.marks)	
	
	def accept (self):
		self.name=input("Enter name ")
		self.age=input("Enter age ")
		self.marks=input("Enter marks ")


s1=Student('Diya',20,[80,85,88])
s2=Student('Yash',18,[70,85,95])
s1.accept()
s2.accept()
s1.display()
s2.display()

