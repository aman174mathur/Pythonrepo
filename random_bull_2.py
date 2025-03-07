# def day_of_week(d, m, y):
#     # Predefined month codes for each month
#     month_code = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

#     # Adjust year for January and February
#     if m < 3:
#         y -= 1  # If month is January or February, treat them as part of the previous year

#     # Calculate the year code
#     year_code = (y % 100) + (y % 100) // 4

#     # Adjust year code for the century
#     year_code = (year_code + (y // 100) // 4 + 5 * (y // 100)) % 7

#     # Calculate the day of the week and return the value as an integer
#     return (d + month_code[m - 1] + year_code) % 7

# # Input: day, month, and year
# day = 15
# month = 6
# year = 1995

# # Calculate the day of the week using the formula-based approach
# day_of_week_result = day_of_week(day, month, year)

# # Output the result as an integer (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
# print(day_of_week_result)
# year repetition 
# q1 which year will be  repeated for 2008?
# 2008 is a leap year
#  2008+ 28 = 2036 --> year

#  q2 which year is repeated for 2010?
# 2010 is not a leap year
# 2010+11=2021
#  q3 which year is repeated for 2009?
# 2009 is not a leap year
# 2009+11!=2020
# 2009 +6 = 2015

# {28,11,6}
# 28 is for leap year
# 11 is for non leap year
# 6 is for non leap year with 29 days in february

# the population of town is  189000 
#  4/9 from them are males and rest are females 
#  50% males are married . find % of married population?

#  4/9 * 189000 = 84000 males
# find % of married males
# 50% of 84000 = 42000

#  50% of 84000 = 42000 married males
#  42000 / 189000 = 0.2222
#  0.2222 * 100 = 22.22%

# fraction is increasesd by 20% and after tthat neumerator increaes by 240% and denominator is increased to 150% so that the result becomees 1 1/5 . what is the 
# original fraction?
#  let the original fraction be x/y
#  x/y * 1.2 = 1.2x/1.2y
# 1.2x/1.2y * 2.4x/1. 5y = 1.2x*2.4x/1.2y*1
# 1.2x*2.4x/1.2y*1.5
# 2.88x^2/1.8y = 1.2/1
# 2.88x^2 = 1.8y
# 2.88x^2 = 1.8y
# 2.88x^2 = 1.8y
# 2.88x^2 = 1.8y

# rama expenditure and savings are in the ratio of 5:3 if her income increases by 12% and her expenditure increases by 15% then by how much percent will her savings increase?
# let the original expenditure be 5x and original savings be 3x
# 5x + 3x = 8x
# 8x * 1.15 = 9.2x
# 8x * 1.15 = 9.2x
# 8x * 1.15 = 9.2x

import pandas as pd 

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print(df)
# giving null values of the dataframe
print(df.isnull().sum())
#droping rows with missing values
print(df.dropna())

print(df['Age'].value_counts())
# rename columns
df  = df.rename(columns = {'Age': 'new_age'})
print(df)
#filtered in dataframe 
filtered_df = df[df ['new_age'] > 30]
print(filtered_df)
# loc and iloc 
#loc method [row_range , column_name]  Label based slection
x=df.loc[0:1,['new_age','Salary']]
print(x)
#iloc method [row_range , column_name]   position based indexing
y= df.iloc[0:1,[0,2]]
print(y)
#group by function
df_grouped = df.groupby('new_age')['Salary'].sum()
print(df_grouped)
# sort values in ascending order
df_sorted = df.sort_values(by='new_age', ascending=False)
print(df_sorted)
# p= df['new_age'] = pd.to_datetime(df['new_age'])
# print(p)

d=df['new_age'][2] = 45
print(d)

i=df.info()
print(i)
des = df.describe()
print(des)
