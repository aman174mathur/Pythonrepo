# pandas --> open source library that is used for data manipulation and analysis

# for installing pandAS
# !pip install pandas for jyupyter
# pip install pandas for vs

# data structure of pandas
# 1. series ---> it is one - dimnensional array and it shows only values not columns
# 2. data frame ---> it is two dimensional array and it shows both values and columns

# series --->.

import pandas as pd

# a= pd.Series([1,34,56,78])
# print(a)  # output: 0    1

# type(a)

# output: pandas.core.series.Series

# DATAFRAME
# Q1 we have to create employee data using dictionary?
a = { 
"Emp ID": [1,2,3,4,5,6,7,8], 
"Emp Name": ['Sam', 'Raj', 'Mohit', 'Sam', 'Gorav', 'Mohit', 'Mohit', 'Garvit'], 
"Department": ['IT', 'Sales', 'IT', 'Operations', 'HR', 'IT', 'Operations', 'HR'], 
"Working_hours": [8,9,9,9,9,8,8,8], 
"Salary" : [23000,25000,35000,31000, 28000,26000, 30000, 34000] 
} 
print(type(a))

df = pd.DataFrame(a)
print(df)

#how do you export our dataframe into csv file?
# steps = 
# 1. import pandas as pd
# 2. df.to_csv('filename.csv', index=False)
# 3. index = False = does not show index in csv file
df.to_csv('employee.csv',index = False)

#how do you import our dataframe into csv file?
# steps =
# 1. import pandas as pd
# 2. df = pd.read_csv('filename.csv')
'''df = pd.read_csv('employee.csv')
print(df)'''

#how do you import our dataframe into jupyter notebook?
# open a folder in which you have datadets
#copy the folder loc
#paste it into jupyter notebook
'''df = pd.read_csv("paste_folder_location//file_name.csv")'''


##how do you import our dataframe into google colab notebook?
# 1. upload the csv file into google drive  
# 2. mount the google drive into google colab
# 3. import pandas as pd
# 4. df = pd.read_csv('paste_folder_location//file_name.csv')
# 5. df.head() to see the data


#10 rows min 5 col 
# stu_id
# stu_name
# stream
# fee_str # type: ignore
# sem

# make data on jy
# operate in colab

student_data = {
    "student_name": ["sam", "john", "jane", "jack", "jill" , "ram", "sham", "sam", "john", "jane"],
    "student_id": [101,102, 103 , 104 , 105 , 106 , 107, 108, 109, 110],
    "student_stream": ["maths", "biology", "humanities","maths","biology", "humanities", "maths", "biology", "humanities", "maths"],
    "fee_structure": [1000, 2000, 3000, 1000, 2000, 3000, 1000, 2000, 3000, 1000],
    "semester": [1, 2, 3, 1, 2, 3 , 1, 2, 3, 1]
}

# create a dataframe
df = pd.DataFrame(student_data)
df.to_csv( 'student_data.csv', index=False)


#how do you save a dataframe in jupyter notebook in csv 
# 1. import pandas as pd
# 2. df = pd.DataFrame(student_data)
# 3. df.to_csv('filename.csv', index=False)

