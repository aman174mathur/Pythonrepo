class Employee:
    location = "Bangalore"

    def __init__(mkb, name, age, salary): #constructor here is __init__ and it is called when object is created
        mkb.name = name
        mkb.age = age
        mkb.salary = salary
    
    def getInfo(mkb):
        print(f"name of employee is {mkb.name}")
        print(f"age of employee is {mkb.age}")
        print(f"salary of employee is {mkb.salary}")
        print(f"location of employee is {mkb.location}")

e= Employee("Gautam", 25, 100000)
e.getInfo()
a= Employee("Amit", 30, 200000)
a.getInfo()


class dog:
    def __init__(self,name,breed):#constructor with 'self' keyword
        self.name=name#'self.name' binds to the instance attribute
        self.breed=breed

    def bark(self):
        print(f"{self.name} is barking")
        print(f"{self.breed} is the breed of {self.name}")


dog1=dog("Tommy","German Shepherd")
dog2=dog("Spike","Bulldog")

#acess attributes and methods of class
dog1.bark()
dog2.bark()


#Task 1 to create a claculator class
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1+self.num2
    
    def sub(self):
        return self.num1-self.num2
    
    def mul(self):
        return self.num1*self.num2
    
    def div(self):
        if self.num2!=0:
            return self.num1//self.num2
        else:
            return "Division by zero is not possible"
        
calc=Calculator(10,5)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())

#Task 2 to create a class of bank account
class BankAccount:
    def __init__(self,account_holder_name,balance=0):
        self.account_holder_name=account_holder_name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return ("amount deposited ","new balance is ",self.balance)
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            return ("amount withdrawn ","new balance is ",self.balance)
        else:
            return "Insufficient balance"
    
    def check_balnace(self):
        print("current balance is ",self.balance)
    
acc1=BankAccount("Gautam",1000)
print(acc1.deposit(500))
print(acc1.withdraw(200))
acc1.check_balnace()

#Task 3 to create a class of student
class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    
    def display_details(self):
        print(f"Name of student is : {self.name}")
        print(f"Age of student is : {self.age}")
        print(f"Marks of student is:  {self.marks}")
    
    def has_passed(self):
        if self.marks>=40:
            print("student has :passed")
        else:
            print("student has : failed")

s1=student("gautam",20,78)
s1.display_details()
s1.has_passed()

