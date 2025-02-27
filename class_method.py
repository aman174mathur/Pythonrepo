#a class method is a method that operates on the class itself rather than an instance of a class.
#it is defiend using the @ class decorator and takes cls refrence as the first parameter .

'''class Employee:
    company_name = "tech solutions"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company_name( cls, new_name):
        cls.company_name = new_name

#use
emp1= Employee("sam",7000)
emp2= Employee("john",8000)

#acess the class attribute
print(Employee.company_name)

#change the class attribute using class method
Employee.change_company_name("tech solutions pvt ltd")
print(Employee.company_name)

emp1.company_name
emp1.change_company_name('farji company')
print(emp1.company_name)

Employee.change_company_name("rebel")
print(emp2.company_name)'''

#Static method
# a static method is a method that does not operate on either the class or the instance of the class.
# it behaves like a regular function but is defined inside a class for logical grouping.
# it is marked with the @staticmethod decorator. 

#features of static method
# 1. it does not require self or cls as parameter 
# 2. we cannot modify class or instance attributes
# 3. it is useful for multitiy or helper methods that do not rely on the class or instance state.

'''class Mathoperations:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def subtract(a, b):
        return a-b
    
#use
print(Mathoperations.add(10,20))
print(Mathoperations.subtract(10,20))'''

#use case 2 

'''class Employee:
    location = "jaipur"

    def __init__(self,name,role):
        self.name=name
        self.role=role

    def get_location(self):
        print("name of the employee is:",self.name, "and role is :", self.role)

    @staticmethod
    def Newinfo():
        print("new employee is joining the company")

#use
a= Employee("rahul","software engineer")
a.get_location()
a.Newinfo()'''


#SUPER MEthoD : is used to call a method from a parent class in the context of inheritance.
#it allows us to avoid explicly reffering to the parent clas and makes the code more maintanable.

# FEATURES:
# access parents class method or attributes 
#useful in multi-level or multiple inheritance
# helps in code repetitation 

#use case 1
class Parent :
    def __init__(self,name):
        self.name=name
    
    def greet(self):
        print("hello ",self.name,"i am from parent class")

class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    
    def greet(self):
        super().greet()
        print("heelo iam ",self.name,"years old and from the child class")

#usage
a=Child("rahul",25)
a.greet

#why we use polymorphism?
# it allows objects of  different classes to be treated as objects of a common super class
# it enables a single interface to represent different underline forms, this makes the code more flexible , reusable, and eaiser to extend . 

#OVERRIDING:
#it is a feature in oops where a subclass provide a specific implemntation for a method that is already defined in its parentclass.
# the overrriden method in the subclass will be executed instead of the one in the parent class when called on an instance of the subclass.

# class Vehicle:
#     def move(self):
#         print("vehicle is moving")

# class Car(Vehicle):
#     def move(self):
#         print("car is moving")

# class Bike(Vehicle):
#     def move(self):
#         print("bike is moving")

# vehilcle =Vehicle()
# c=Car()
# b=Bike()

# vehilcle.move()
# c.move()
# b.move()

#OVERLOADING: allows the same function to behave differntly based on the number or 
# type of arguments passed to it.

# while python does not support method overloading directly it can be mimied using 
# default argument values or by checking argument types.

def greet(name = "geust"):
    print("hello",name)

# greet()  #default name is geust
greet("raj")

#RECURSION : in python it reffers to a process where a functions calls itself to solve samller instance
# of the same problem.
# in oops it can be used within class method to perform repetitive tasks.
# KEY FEATURES:
# base case --> 
# a condition that stops the recursion to prevent infinite calls .

# recusive case --->
# the part where the function calls itself with a modified argument

class Factorial:
    def calculate_factorial(self,n):
        if n==0 or n==1:
            return 1
        else:
            #recursive
            return n*self.calculate_factorial(n-1)
        
cal=Factorial()
number= 5
result= cal.calculate_factorial(number)
print("factorial of",number,"is",result)
