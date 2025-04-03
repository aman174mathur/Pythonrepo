class Bankaccount:
    def __init__(self, account_holder,balance):
        self.__account_holder = account_holder
        self.__balance = balance
    
    #getter for account holder
    def get_account_holder(self):
        return self.__account_holder
    
    #getter for balance
    def get_balance(self):
        return self.__balance
    
    #method to deposit money
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            return f"deposit successful: {self.__balance}"
        else:
             return "invalid amount"
        
    # method to withdraw money
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"withdraw successful: {self.__balance}"
        else:
            return "invalid amount"

#using the class 
account = Bankaccount("John",1000)
print(account.get_account_holder())
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))

#attempt to acess private attribute directly(not allowed)
#print(account.__balance)
#error : Attribute error'''


#question 2 student data 

class Student:
    def __init__(self,name,grade):
        self.name = name #public attribute
        self.__grade = grade #private attribute

    #getter for grade
    def get_grade(self):
        return self.__grade
    
    #setter for grade(with validation)
    def set_grade(self, new_grade):
        if 0<=new_grade <=100:
            self.__grade = new_grade
            return f"grade updated: {self.__grade}"
        else:
            return "invalid grade must be between 0 and 100"
        
#using the class
student= Student("John",85)
print(student.name)
print(student.get_grade())
print(student.set_grade(90))
print(student.set_grade(120))
print(student.get_grade())
#attempt to access private attribute directly(not allowed)
print(student.set_grade(150))
#invalid grade must be between 0 and 100

#CAASE STDY : HEALTH MANAGEMENT SYSTEM
'''developa system to manage the health of patients
patient details (name , age and medical history) should be private.print
only authorized methods can retrive or upadate medical history.
provide a method to add new medical records while keeping previous data secure.'''

'''class patient:
    def __init__(self,name , age):
        self.__name=name
        self.__age=age
        self.__medical_history=[]
    
    def add_medical_records(self,record):
        self.__medical_history.append(record)
        return f"medical record added for : {self.__name}"
    
    def get_medical_history(self):
        return f"medical history for : {self.__name}: {self.__medical_history}"
    
#use
patient1= patient("John",25)
print(patient1.add_medical_records("2023:flu"))
print(patient1.add_medical_records("2024:fever"))
print(patient1.get_medical_history())
#print(patient1.__medical_history)'''

#CASE STUDY: online exam system
'''class exam:
    def __init__(self,name_of_student):
        self.__name_of_student=name_of_student
        self.__score=[]

    def add_score(self,score,subject):
        if 0<= score <=100:
            self.__score.append({"subject":subject,"score":score})
            return f"score added for : {subject}:{score}"
        return "invalid score! must be between 0 and 100"
    
    def get_scores(self):
        return f"score for : {self.__name_of_student}:{self.__score}"
    
    def calculate_total_score(self):
        if not self.__score:
            return "no scores available"
        total= sum(items["score"] for items in self.__score)
        return f"Average score : {total/len(self.__score):.2f}"

#use
exam = exam("sam")
print(exam.add_score(90,"math"))
print(exam.add_score(80,"marathi"))
print(exam.add_score(100,"english"))
print(exam.get_scores())
print(exam.calculate_total_score())

#explain the __init__ func'''

'''class Bankaccount:
    def __init__(self,account_holder,balance):
        self.__amount_holder=account_holder
        self.__balance=balance
    
    #getter for account holder
    def get_account_holder(self):
        return self.__account_holder

    #Getter for balance
    def get_balance(self):
        return self.__balance
    
    #method to deposit
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            return ("deposit successful",self.__balance)
        else:
            return "invalid deposit amount!"

    #method to withdraw money
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance+=amount
            return("withdraw succseful",self.__balance)
        else:
            return "invalid amount"

#using the class 
account = Bankaccount("John",1000)
print(account.get_account_holder())
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))'''

'''class student:
    def __init__(self,name,grade):
        self.name=name
        self.__grade=grade
    
    #getter for grade
    def get_grade(self):
        return self.__grade

    #setter for grade
    def set_grade(self,new_grade):
        if 0<=new_grade<=100:
            self.__grade = new_grade
            return "grade update successfully"
        else:
            return "invalid grade!"

#use
student = student("rohit",85)
print(student.name)
print(student.get_grade())
print(student.set_grade(90))
print(student.get_grade())
#invalid grade
print(student.get_grade(150))'''

''''class Patient:
    def __init__(self,name,age):
        self.__name=name
        self.__medical_records=[]
        self.__age=age
    
    def add_medical_records(self,record):
        self.__medical_records.append(record)
        return ("medical record added for ",self.__name)

    def get_medical_history(self):
        return f"medical history for ,{self.__name}:{self.__medical_records}"

#use
patient1=Patient("rohit",30)
print(patient1.add_medical_records("2023:flu"))
print(patient1.add_medical_records("2024:fever"))
print(patient1.get_medical_history())
#print(patient1.__medical_history)'''

'''class exam:
    def __init__(self,name_of_student):
        self.__name_of_student=name_of_student
        self.__score=[]

    def add_score(self,score,subject):
        if 0<= score <=100:
            self.__score.append({"subject":subject,"score":score})
            return f"score added for : {subject}:{score}"
        return "invalid score! must be between 0 and 100"
    
    def get_scores(self):
        return f"score for : {self.__name_of_student}:{self.__score}"
    
    def calculate_total_score(self):
        if not self.__score:
            return "no scores available"
        total= sum(items["score"] for items in self.__score)
        return f"Average score : {total/len(self.__score):.2f}"

#use
exam1=exam("aamn")
print(exam1.add_score(10,"math"))
print(exam1.add_score(20,"english"))
print(exam1.get_scores())
print(exam1.calculate_total_score())'''

#INHERITANCE
class Employee:
    def __init__(self,loacation):
        self.__location=loacation
    def get_location(self):
        print("name of location is :",self.__location)

class Manager(Employee):
    def get_project(self):
        print("project name is working....")

sam= Employee('jaipur')
#sam.get_location()
Mohit = Manager('delhi')
Mohit.get_project()
Mohit.get_location()