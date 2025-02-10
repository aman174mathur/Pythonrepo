# 1️⃣ Filter Even and Odd Numbers
# Problem:
# You have a list of numbers. Separate even and odd numbers into two different lists.

# Example Input:
numbers = [10, 23, 45, 66, 78, 89, 92]

# Example Output:
# Even numbers: [10, 66, 78, 92]
# Odd numbers: [23, 45, 89]

lista=[]
listb=[]

for i in numbers:
    if i%2==0:
        lista.append(i)
    else:
        listb.append(i)
print(lista)
print(listb)


# 2️⃣ Find the Largest and Smallest Number
# Problem:
# Given a list of numbers, find the largest and smallest number in the list.

# Example Input:
numbers = [5, 12, 8, 3, 20, 15]

# Example Output:
# Largest: 20, Smallest: 3

largest=numbers[0]
smallest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
if i<smallest:
    smallest=i
print("largest:",largest)
print("smallest:",smallest)

# 3️⃣ Count Positive, Negative, and Zero
# Problem:
# Given a list of numbers, count how many are positive, negative, and zero.

# Example Input:
numbers = [3, -1, 0, 4, -2, 7, 0, -6]

# Example Output:
# Positive: 3, Negative: 3, Zero: 2

positive=0
negetive=0
zero=0

for i in numbers:
    if i>0:
        positive+=1
    elif i<0:
        negetive+1
    elif i==0:
        zero+=1

print("positive: ", positive)
print("negetive: ",negetive)
print("zero: ",zero)


# 4️⃣ Sum of List Elements
# Problem:
# Find the sum of all elements in a given list.

# Example Input:
numbers  = [4, 7, 1, 9, 3]

# Example Output:
# Sum: 24

sum=0
for i in numbers:
    sum=sum+i
print("sum: ",sum)


# 5️⃣ Reverse a List Without Using reverse()
# Problem:
# Given a list, reverse it manually.

# Example Input:
numbers = [1, 2, 3, 4, 5]

# Example Output:
# Reversed List: [5, 4, 3, 2, 1]

reverse= numbers[::-1]
print(reverse)

# 6️⃣ Find Duplicate Elements in a List
# Problem:
# Find and print all duplicate elements from a list.

# Example Input:
numbers = [1, 3, 5, 3, 7, 9, 1, 5]

# Example Output:
# Duplicate Elements: [1, 3, 5]

duplicates=[]
for i in numbers:
    if numbers.count(i)>1:
            if i not in duplicates:
                duplicates.append(i)
print(duplicates)

# 7️⃣ Remove Duplicates from a List
# Problem:
# Given a list with duplicate elements, remove duplicates without using set().

# Example Input:
numbers = [2, 4, 6, 8, 4, 2, 10, 6]

# Example Output:
# List without duplicates: [2, 4, 6, 8, 10]

notduplicate=[]
for i in numbers:
    if numbers.count(i)==1:
        notduplicate.append(i)
    else:
        continue
print(notduplicate)

#8️⃣ Find the Second Largest Number
# Problem:
# Find the second largest number in a given list.

# Example Input:
numbers = [4, 8, 12, 5, 18, 9]

# Example Output:
# Second Largest: 12

secondlargest=[]
numbers.sort()
print(numbers[-2])

# 9️⃣ Check If a List is Sorted (Ascending Order)
# Problem:
# Check whether a given list is sorted in ascending order.

# Example Input:
numbers2 = [2, 5, 7, 10, 15]

# Example Output:
# List is sorted


numbers2 = [2, 5, 7, 10, 15]

for i in range(0,len(numbers2)-1):

    if numbers2[i]<=numbers2[i+1]:
        print("List is sorted")
        break
    else:
        print("List is not sorted")



# 🔟 Count the Frequency of Each Element in a List
# Problem:
# Count how many times each element appears in the list.

# Example Input:
numbers = [2, 3, 4, 2, 3, 5, 2]

# Example output : 
# 2 appears 3 times
# 3 appears 2 times
# 4 appears 1 time
# 5 appears 1 time

count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for num, count in count_dict.items():
    print(f"{num} appears {count} time")

# 1️1. Rotate a List by K Positions
# Problem:
# Given a list and an integer k, rotate the list to the right by k positions.

# # Example Input:
numbers = [1, 2, 3, 4, 5]
k = 2


# # Example output : 
# Rotated List: [4, 5, 1, 2, 3]

rotate=numbers[-k:]+numbers[:-k]
print(rotate)