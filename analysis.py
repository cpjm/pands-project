# This program will process the iris datset.
# it will produce a number of (hopefully!) meaningful plots on the data.
#
# Opening and reading the 'iris.data' csv file.
# My code re-used code from this article:- 
# https://www.w3schools.com/python/pandas/pandas_csv.asp
#
# Author: Ciaran Moran
# 
# 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#############
#DEFINE VARS

#############
fs=11 # font size for the plot text
legend_fs=6  # font size for the legend text

# function that takes in a dataset and filename 
# and saves the plot to a PDF file.
def save_dataset_to_pdf():
    #somethine here
    dummy_var=1
    

##############
#Load the data
##############
#The column info from iris.names, this denotes the columns in the csv
#7. Attribute Information:
#   1. sepal length in cm
#   2. sepal width in cm
#   3. petal length in cm
#   4. petal width in cm
#   5. class: 
#      -- Iris Setosa
#      -- Iris Versicolour
#      -- Iris Virginica
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
#ref https://www.w3schools.com/python/pandas/pandas_csv.asp#gsc.tab=0
df = pd.read_csv('data/iris.data',names=col_names)
#debug print(df.to_string()) 




#3.1
# Generate useful summary info to the outout file "iris_summary.txt"
#ref https://pandashowto.com/how-to-save-dataframe-as-text-file/
#I analyse this data further and what it means in my research
#df.to_string("myfile.txt")
#ref https://www.w3schools.com/python/pandas/ref_df_describe.asp
#debug print(df.describe())
df.describe().to_string("iris_summary.txt")
print(df.describe(''))
# print(df[["Sepal_Length"]].describe(include="all"))
# print(df[["Sepal_Width"]].describe(include="all"))
# print(df[["Petal_Length"]].describe(include="all"))
# print(df[["Petal_Width"]].describe(include="all"))
# print(df[["Class"]].describe(include="all"))
# print(df[["Class","Sepal_Length"]].describe(include="all"))
# print(df[["Class","Sepal_Width"]].describe(include="all"))
# print(df[["Class","Petal_Length"]].describe(include="all"))
# print(df[["Class","Petal_Width"]].describe(include="all"))

#3.2
#Saves a histogram of each variable to png files
#As histgrams deal with numeric columns only, we
#need to remove the non-numerical column i.e. the class flower description

histogram_df = df # make a working copy of the dataset

#Histogram of the Sepal and Petal lengths for all 3 classes or iris
plt.hist(histogram_df.drop('Class',axis=1))
plt.title('Frequency of each Sepal and Petal lengths & widths', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Sepal Length', 'Sepal Width','Petal Length','Petal Width'], fontsize = legend_fs)
plt.savefig("sepal_and_petal_lengths.png", format="png")
plt.show()

#Class subsets
#col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
setosa_data = histogram_df[histogram_df['Class'] == 'Iris-setosa']
versicolor_data = histogram_df[histogram_df['Class'] == 'Iris-versicolor']
virginica_data = histogram_df[histogram_df['Class'] == 'Iris-virginica']
#Class width subset
setosa_sepalWidth_data = histogram_df[histogram_df['Class'] == 'Iris-setosa']['Sepal_Width']
versicolor_sepalWidth_data = histogram_df[histogram_df['Class'] == 'Iris-versicolor']['Sepal_Width']
virginica_sepalWidth_data = histogram_df[histogram_df['Class'] == 'Iris-virginica']['Sepal_Width']
#Class length subset
setosa_sepalLen_data = histogram_df[histogram_df['Class'] == 'Iris-setosa']['Sepal_Length']
versicolor_sepalLen_data = histogram_df[histogram_df['Class'] == 'Iris-versicolor']['Sepal_Length']
virginica_sepalLen_data = histogram_df[histogram_df['Class'] == 'Iris-virginica']['Sepal_Length']

#Plot based on class width subset data
plt.hist([setosa_sepalWidth_data,versicolor_sepalWidth_data,virginica_sepalWidth_data])
plt.title('Frequency of each Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
plt.savefig("frequency_sepal_width.png", format="png")
plt.show()

#Plot based on class length subset data
plt.hist([setosa_sepalLen_data,versicolor_sepalLen_data,virginica_sepalLen_data])
plt.title('Frequency of each Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
plt.savefig("frequency_sepal_length.png", format="png")
plt.show()


#Variable 1 - sepal length

#Variable 2 - sepal width

#Variable 3 - petal length

#Variable 4 - petal width




#3.3 
#Outputs a scatter plot of each pair of variables

#3.4
#Performs any other analysis you think is appropriate

