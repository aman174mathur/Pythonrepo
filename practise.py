#dynamically typed language?
#Python is a dynamically typed language, 
# which means that you don't have to
# declare the type of a variable when you create one.


#statically typed language?
#In statically typed languages,
# you have to declare the type of a variable when you create one.
# For example, in Java, you have to specify the type of a variable:
# int x = 5;
# String y = "Hello";
# In Python, you can create a variable without specifying the type:
# x = 5
# y = "Hello"

#compiled language?
#A compiled language is a programming language whose implementations are typically 
#compilers (translators that generate machine code from source code),
# and not interpreters (step-by-step executors of source code, where no pre-runtime translation takes place).
#The term is somewhat vague. In principle any language can be implemented with a compiler or with an interpreter.
#However, the term is usually used to emphasize that the implementation is a compiler.
#For example, C, C++, and Fortran are compiled languages.

#interpreted language?
#An interpreted language is a type of programming language for which most of its implementations execute instructions directly,
#without previously compiling a program into machine-language instructions.
#Theoretically, any language can be compiled or interpreted, so the categorization is not exclusive.
#For example, Perl, Python, Ruby, and shell scripts are interpreted languages.
#Python is an interpreted language, which means that it is not actually compiled into machine code.
#Instead, it is processed at runtime by the interpreter.

#What are *args and **kwargs?
#*args and **kwargs are mostly used in function definitions.
#*args and **kwargs allow you to pass a variable number of arguments to a function.
#Here's how you can use them:
#*args is used to send a non-keyworded variable-length argument list to the function.
#**kwargs allows you to pass keyworded variable-length of arguments to a function.
#Here is an example to help you understand the concept:
#*args
# def my_function(*args):
#     for arg in args:
#         print(arg)
# my_function(1, 2, 3)
# Output
# 1
# 2

# **kwargs
# def my_function(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
# my_function(first='a', second='b')



n=6
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n-i):
        if k==0 or k==n-i-1 or i==0:
            print(k+1,end="")
        else:
            print(" ",end="")
    print()

#reverse it 
n=6
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i+1):
        if k==0 or k==i or i==n-1:
            print(k+1,end="")
        else:
            print(" ",end="")
    print()

#how to remove substring from string?
#You can use the replace() method to remove a substring from a string.
#Here's an example:
# string = "Hello, World!"
# substring = "Hello, "
# new_string = string.replace(substring, "")
# print(new_string)
# Output
# World!

string="Hello, World!"
substr="Hello ,"
new_string=string.replace(substr,"")
print(new_string)


#create a pyhton func which takes a number as an argument and return the dictionary of a number as a key and true or false as a value
def is_even(n):
    return {n:True if n%2==0  else False}
print(is_even(5))


#reverse number triangle pattern
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n-i-1):
        print(k+1,end="")
    print()
#1234
#234
#34
#4
#solve this 
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n-i-1):
        if i==1:
            print(k+2,end=" ")
        elif i==2:
            print(k+3,end=" ")
        elif i==3:
            print(k+4,end=" ")
        else:
            print(k+1,end=" ")
    print()

#* * * * *
# *      *
  # *    *
  #   *  *
   #     *   
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(n-i):
        if k==0 or k==n-i-1 or i==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#find substring frequency in a string
str="RGRG"
#output={'a':3,'b':2,'ab':2,'ba':2,'aba':2,'bab':1,'abab':1,'baba':1}
freq={}
for i in range(len(str)):
    for j in range(i+1,len(str)+1):
        sub=str[i:j]
        if sub in freq:
            freq[sub]+=1
        else:
            freq[sub]=1
print(freq)

#find the frequency of each character in a string
str='aabcdeef'
#output=[2,1,1,1,2,1]
freq=[]
for i in range(len(str)):
    count=1
    for j in range(i+1,len(str)):
        if str[i]==str[j]:
            count+=1
    freq.append(count)
print(freq)\

#string in pyhton
# Define the number

n = 12345

# Convert number to list of integers
res = list(map(int, str(n)))

print(res) 




