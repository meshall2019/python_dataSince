import pandas as pd

# The class of exploratory data analysis

# read data as data
data = pd.read_csv("train.csv")

# check the dimension of the table
def dimension_of_table():
   print("The dimension of the table is: ", data.shape)

#Look the data Set
def look_to_dataSet():
   print(dimension_of_table())

#check the summary of the variables
def summary_of_varibles():
   print(data.describe(include=['O']))

