#Case Study 1: Employee Salary Management
#Scenario:
#A company wants to store and analyze employee salary data. You need to create a system where:
#1. Employees are stored in a dictionary with employee ID as key and (name, department,
#salary) as values.
#2. Implement functions to:
#o Increase the salary of all employees in a particular department by a given
#percentage.
#o Find the employee with the highest salary.
#o Filter employees earning more than a given amount.

#Hints:
# Use a dictionary to store employee data.
# Use loops to iterate and modify salaries.
# Use tuple unpacking when retrieving data.


'''class Employee:
    employees = {}

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        Employee.employees[self.emp_id] = (self.name, self.department, self.salary)

    def increase_salary(self, department, percentage):
        for emp_id, (name, dept, salary) in Employee.employees.items():
            if dept == department:
                new_salary = salary + (salary * percentage / 100)
                Employee.employees[emp_id] = (name, dept, new_salary)
                print(f"Salary of {name} increased by {percentage}%")

    def find_highest_salary(self):
        highest_salary = 0
        highest_paid_employee = None
        for emp_id, (name, dept, salary) in Employee.employees.items():
            if salary > highest_salary:
                highest_salary = salary
                highest_paid_employee = (emp_id, name, dept, salary)
        return highest_paid_employee

    def filter_employees(self, amount):
        filtered_employees = []
        for emp_id, (name, dept, salary) in Employee.employees.items():
            if salary > amount:
                filtered_employees.append((emp_id, name, dept, salary))
        return filtered_employees

# Use
emp1 = Employee(1, "John", "IT", 5000)
emp2 = Employee(2, "Jane", "HR", 6000)
emp3 = Employee(3, "Doe", "IT", 7000)

print(Employee.employees)
emp1.increase_salary("IT", 10)
print(emp1.find_highest_salary())
print(emp1.filter_employees(5000))'''


#Case Study 2: Student Performance Analysis
#Scenario:
#A school maintains student records with their scores in different subjects. You need to:
#1. Store students in a list of tuples where each tuple contains (name, math_score,
#science_score, english_score).
#2. Implement functions to:
#o Find the student with the highest average marks.
#o Sort students based on total marks.
#o Find students who scored below 40 in any subject (failed students).

#ints:
# Use a list of tuples to store data.
# Use loops and conditional statements to process the data.
# Use the sorted() function to sort based on total marks.


'''class student:
    students = []
    def __init__(self,name,math_score, science,english):
        self.name=name
        self.math_score=math_score
        self.science_score=science
        self.english_score=english
        self.students.append((name,math_score,science,english))
    
    def find_highest_average(self):
        highest_average=0
        highest_average_student=None
        for name, math_score, science, english in self.students:
            average=(math_score+science+english)/3
            if average>highest_average:
                highest_average=average
                highest_average_student=(name, math_score, science, english)
        return highest_average_student

    def sort_students(self):
        return sorted(self.students, key=lambda x: x[1] + x[2] + x[3], reverse=True)
    
    def find_failed_students(self):
        failed_students=[]
        for name, math_score, science, english in self.students:
            if math_score < 40 or science < 40 or english < 40:
                failed_students.append((name, math_score, science, english))
        return failed_students

#Test the functions
student1=student("jhon",56,78,89)
student2=student("jane",78,90,56)
student3=student("doe",30,35,40)
print(student1.find_highest_average())
print(student1.sort_students())
print(student1.find_failed_students())'''

#Case Study 3: Unique Word Counter
#Scenario:

#You are given a paragraph of text. You need to:
#1. Extract all unique words from the paragraph.
#2. Count the frequency of each word.
#3. Display the top 5 most common words.
#Hints:
# Use a set to store unique words.
# Use a dictionary to maintain word counts.
# Use loops to iterate and count words.
# Use sorted() with lambda to get the top 5 words.


'''class UniqueWordCounter:
    def __init__(self,paragraph):
        self.paragraph=paragraph
        self.unique_words=set()

    def extract_unique_words(self):
        words=self.paragraph.split()
        for word in words:
            self.unique_words.add(word)
        return self.unique_words

    def count_word_frequency(self):
        word_count = {}
        for word in self.unique_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

    def top_5_words(self):
        word_count = self.count_word_frequency()
        # Sort the word count dictionary by value in descending order and get the top 5 words
        top_5_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]
        return top_5_words
#use

paragraph1= UniqueWordCounterLorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s)

print(paragraph1.extract_unique_words())
print(paragraph1.count_word_frequency())
print(paragraph1.top_5_words())'''


#Case Study 4: E-commerce Product Catalog
#Scenario:
#You are developing a product catalog system for an e-commerce store. You need to:
#1. Store products as a dictionary, where keys are product IDs and values are (name, category,
#price).
#2. Implement functions to:
# Get all products in a specific category.
#o Find the most expensive product.
#o Identify and remove duplicate product names using a set.

#Hints:
# Use a dictionary for product data.
# Use a set to remove duplicate names.
# Use loops and conditional statements to find the most expensive product.


'''class platform:
    def __init__(self, products):
        self.products= products
        self.unique_names = set()
        self.most_expensive_product = None
        self.most_expensive_price = 0

    def get_all_products_in_category(self):
        # Get all products in a specific category
        category = input("Enter the category: ")
        category_products = {}
        for product_id, product in self.products.items():
            if product[1] == category:
                category_products[product_id] = product
                print(f"Product ID: {product_id}, Name: {product[0]}, Price: {product[2]}")
        return category_products
    
    def find_most_expensive_product(self):
        # Find the most expensive product
        for product_id, product in self.products.items():
            if product[2] > self.most_expensive_price:
                self.most_expensive_product = product
                self.most_expensive_price = product[2]
        return self.most_expensive_product

    def remove_duplicate_names(self):
        # Identify and remove duplicate product names using a set
        for product_id, product in self.products.items():
            self.unique_names.add(product[0])
        return self.unique_names

#use
products = { 1: ('Product A', 'digital', 100), 2: ('Product B', 'Electronics', 200), 3: ('Product C', 'Clothing', 300 ) }
platform = platform(products)
print(platform.get_all_products_in_category())
print(platform.find_most_expensive_product())
print(platform.remove_duplicate_names())'''  


#Case Study 5: Movie Recommendation System
#Scenario:
#A streaming service wants to recommend movies based on user interests. You need to:
#1. Store users and their watched movies as a dictionary:
#users = {
#&quot;Sam&quot;: {&quot;Inception&quot;, &quot;Titanic&quot;, &quot;Avengers&quot;},
#&quot;Mohit&quot;: {&quot;Inception&quot;, &quot;Avatar&quot;, &quot;Jurassic Park&quot;},

#quot;Raj&quot;: {&quot;Titanic&quot;, &quot;Avatar&quot;, &quot;Harry Potter&quot;}
#}
#2. Implement functions to:
#o Find common movies between two users (movies they both watched).
#o Suggest new movies for a user based on what their friends watched.
#o Find the most-watched movie among all users.

#Hints:
# Use sets to find common and suggested movies.
# Use dictionaries for user-movie mapping.
# Use loops to analyze data.


'''{
    "Sam": {"Inception", "Titanic", "Avengers"},
    "Mohit": {"Inception", "Avatar", "Jurassic Park"},
    "Raj": {"Titanic", "Avatar", "Harry Potter"}
}'''

'''class movierecommender():
    def __init__(self, users):
        self.users = users

    def find_common_movies(self, user1, user2):
        return self.users[user1].intersection(self.users[user2])

    def suggest_movies(self, user):
        all_movies = set()
        for movies in self.users.values():
            all_movies.update(movies)
        return all_movies - self.users[user]

    def most_watched_movie(self):
        movie_count = {}
        for movies in self.users.values():
            for movie in movies:
                if movie in movie_count:
                    movie_count[movie] += 1
                else:
                    movie_count[movie] = 1
        return max(movie_count, key=movie_count.get)

# define the users dictionary
users = {
    "Sam": {"Inception", "Titanic", "Avengers"},
    "Mohit": {"Inception", "Avatar", "Jurassic Park"},
    "Raj": {"Titanic", "Avatar", "Harry Potter"}
}

# create an instance of the class
recommender = movierecommender(users)
print(recommender.find_common_movies("Sam", "Mohit"))
print(recommender.suggest_movies("Sam"))
print(recommender.most_watched_movie())'''



#Case Study 6: Traffic Violation Analysis (Dictionaries, Lists, Loops)
#Scenario:
#A city traffic department wants to analyze violations. 
 
# You need to:
#1. Store data in a dictionary, where keys are license plate numbers, and values are (driver
#name, violation type, fine amount).
#  2. Implement functions to:
#o Find the driver with the highest fine. 
# o Count violations per driver. 
# o Identify the most common violation type.

#  Hints:  Use a dictionary to store violation data.
#   Use a loop to analyze violations. 
#  Use a secondary dictionary to track counts.

'''from collections import defaultdict

class trafficviolation():
    def __init__(self):
        self.traffic_data = {}
        self.violation_counts = {}
        self.common_violation = defaultdict(int)
        self.highest_fine_driver = None
        self.highest_fine = 0

    def highest_fine(self):
        if not self.highest_fine_driver:
            return "No data available"
        else:
            return self.highest_fine_driver 
        
    def count_violations(self):
        for driver, violations in self.traffic_data.items():
            self.violation_counts[driver] = len(violations)
        return self.violation_counts
        
    def most_common_violation(self):
        for driver, (name, violation, fine) in self.traffic_data.items():
            self.common_violation[violation] += 1
        for violation, count in self.common_violation.items():
            if count == max(self.common_violation.values()):
                return violation
            return "No data available"
        
        
#use

violation = trafficviolation()
violation.traffic_data = { "ABC123": ("John Doe", "Speeding", 100), "DEF456": (" Jane Doe", "Red Light", 200), "ABC123": ("John Doe", "Speeding", 100) }
print(violation.traffic_data)
violation.highest_fine_driver = max(violation.traffic_data, key=lambda x: violation.traffic_data[x][2])
print(violation.highest_fine_driver)
violation.highest_fine = violation.traffic_data[violation.highest_fine_driver][2]
print(violation.highest_fine)
print(violation.count_violations())
print(violation.most_common_violation())'''


#Case Study 7: Grocery Store Inventory Management (Sets, Dictionaries, Loops)
#Scenario:
#A grocery store needs to track available and sold-out items. You need to:
#1. Maintain two sets:
#o available_items = {"Milk", "Bread", "Eggs", "Rice", "Sugar"}
#o sold_out_items = {"Eggs", "Sugar"}
#2. Implement functions to:
#o Get all available items (remove sold-out items).
#o Add new stock to available items. 
# o Check if an item is in stock. Hints:
#   Use sets to manage available and sold-out items. 
#  Use set operations (difference, union, intersection).


'''available_items = {"Milk", "Bread", "Eggs", "Rice", "Sugar"}
sold_out_items = {"Eggs", "Sugar"}

def get_available_items(available_items, sold_out_items):
    return available_items - sold_out_items

def add_new_stock(new_stock):
    available_items.add(new_stock)
    return available_items

def check_item_in_stock(item):
    return item in available_items

# Use
print(get_available_items(available_items, sold_out_items))
print(add_new_stock("Butter"))
print(check_item_in_stock("Milk"))'''


#Case Study 8: Social Media Hashtag Analysis (Dictionaries, Sets, Loops)
#Scenario:

#A social media company wants to analyze trending hashtags. You need to:

#1. Store hashtag usage in a dictionary where keys are hashtags, and values are usage counts. 
# 2. Implement functions to:
#o Find the top 3 trending hashtags.
# o Filter out hashtags with low usage (less than a given threshold). 
#o Identify common hashtags used by two users (use sets).
#Hints: 
# Use a dictionary to count occurrences. 
# Use sorting to get top hashtags. 
# Use sets to compare hashtag usage across users

'''hashtags = {"yolo":2,"happy":3,"joy":2,"good":5, "yass":6,"queen":7}
threshold = 2

def find_top_trending():
    return sorted(hashtags, key=hashtags.get, reverse=True)[:3]

def filter_low_usage(threshold):
    return {k: v for k, v in hashtags.items() if v >= threshold}

def common_hashtags(user1_hashtags, user2_hashtags):
    return list(user1_hashtags & user2_hashtags)

# Use
user1_hashtags = {"yolo", "happy", "joy"}
user2_hashtags = {"happy", "good", "queen"}
print(find_top_trending())
print(filter_low_usage(threshold))
print(common_hashtags(user1_hashtags, user2_hashtags))'''


#Case Study 9: Airline Ticket Booking System (Lists, Tuples, Loops)
#Scenario:
#An airline company needs to manage ticket bookings. You need to:
#1. Store bookings in a list of tuples where each tuple contains (passenger_name,
#flight_number, seat_number).

#2. Implement functions to:
#o Find all passengers on a specific flight. 
#o Check if a seat is already booked. 
#o Sort passengers by flight number. 

# Hints: 
#  Use a list of tuples to store bookings. 
#  Use loops to filter and find passengers. 
#  Use sorting for better organization.


''''bookings=[("jhon",'12A1',32), ("jane",'12A1',33),("jim",'12A2',34), ("jim",'12A2',35)]

def find_passengers(flight_number):
    return [p for p in bookings if p[1] == flight_number]

def check_seat(flight_number, seat_number):
    for p in bookings:
        if p[1]==flight_number and p[2]==seat_number:
            return "seat occupied"
        return " seat available"
    
def sort_passengers():
    return sorted(bookings,key=lambda x: x[1])

#use
print( find_passengers('12A1'))
print(check_seat('12A1', 32))
print(sort_passengers())'''




#Case Study 10: Library Book Management (Dictionaries, Lists, Sets, Loops)
#Scenario:
#A library maintains a record of books and their borrowers. 
# You need to:
#1. Store books in a dictionary where keys are book titles, and values are (author,
#borrower_name or None if available). 
# 2. Implement functions to:
#o Get a list of all available books. 
# o Find books borrowed by a specific person.
#o Identify duplicate books using a set. 
# Hints: 
#  Use a dictionary to track books. 
#  Use loops to filter available books. 
#  Use a set to find duplicate books.

books = {
    "Maths by RD": ("RD Sharma", "Rahul"),
    "Physics by HC Verma": ("HC Verma", None),
    "Chemistry by OP Tandon": ("OP Tandon", "Sonia"),
    "Biology by Campbell": ("Campbell", None),
    "Maths by RD": ("RD Sharma", "Ankit")
}

def get_all_av_books():
    return [book for book, (author, borrower) in books.items() if borrower is None]

def find_books_borrowed(name):
    return [book for book, (author, borrower) in books.items() if borrower == name]

def find_duplicate(name):
    return [book for book, (author, borrower) in books.items() if book in books and books[book][0] == author]


#use
print(get_all_av_books())
print(find_books_borrowed("Rd Sharma"))
print(find_duplicate("Maths by RD"))