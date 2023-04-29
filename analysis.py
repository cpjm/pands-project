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
import  pandas as pd

#############
#DEFINE VARS
#############
fs=11 # font size for the plot text
legend_fs=6  # font size for the legend text


#def yes_or_no from https://stackoverflow.com/questions/47735267/while-loop-with-yes-no-input-python
def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return 1
    elif reply[0] == 'n':
        return 0
    else:
        return yes_or_no("Please Enter (y/n): ")
     
# function that takes in a dataset and filename 
# and saves the plot to a PDF file.
def render_dataset(indf, title,ylabel, xlabel,legend_title,legend_ol,save_filename,
                   save_filename_type,display_plot_yn):
    plt.hist(indf)
    plt.title(title, fontsize=fs)
    plt.ylabel(ylabel, fontsize=fs)
    plt.xlabel(xlabel, fontsize=fs)
    plt.legend(title=legend_title)
    plt.legend(legend_ol, fontsize = legend_fs)
    plt.savefig(save_filename, save_filename_type)
    #plt.show()
    plt.close()
    
print("Starting iris data set analysis...")

# controls whether to display the plots on the screen. Default to Yes. Useful for "debugging".
while True:
   reply = str(input('Display plots on screen (y/n): ')).lower().strip()
   if reply == 'y':
      display_plots_to_screen=True  
      break
   elif reply == 'n':
      display_plots_to_screen=False  
      break
   else:
      print("Please enter either y/n")
      continue
        
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
if display_plots_to_screen: print(df.describe(''))
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

#def render_dataset(*indf, title,ylabel, xlabel,legend_title,legend_ol,save_filename,
# save_filename_type="png",display_ploy_yn):
df_list1=histogram_df.drop('Class',axis=1)
df_list2=['Sepal Length', 'Sepal Width','Petal Length','Petal Width']
print ("/n********/n")

# render_dataset(df_list1, 
#                "TEST Frequency of each Sepal and Petal lengths & widths",
#                "TEST Frequency", 
#                "TEST Length",
#                "Class of iris",
#                df_list2,
#             "sepal_and_petal_lengths.png",
#                "png",
#                "Y")

#Histogram of the Sepal and Petal lengths for all 3 classes or iris
plt.hist(histogram_df.drop('Class',axis=1))
plt.title('Frequency of each Sepal and Petal lengths & widths', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Sepal Length', 'Sepal Width','Petal Length','Petal Width'], fontsize = legend_fs)
plt.savefig("sepal_and_petal_lengths.png", format="png")
if display_plots_to_screen: plt.show()

#Class subsets
#col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
setosa_data = histogram_df[histogram_df['Class'] == 'Iris-setosa']
versicolor_data = histogram_df[histogram_df['Class'] == 'Iris-versicolor']
virginica_data = histogram_df[histogram_df['Class'] == 'Iris-virginica']
#Sepal width subset
setosa_sepalWidth_data = histogram_df[histogram_df['Class'] == 'Iris-setosa']['Sepal_Width']
versicolor_sepalWidth_data = histogram_df[histogram_df['Class'] == 'Iris-versicolor']['Sepal_Width']
virginica_sepalWidth_data = histogram_df[histogram_df['Class'] == 'Iris-virginica']['Sepal_Width']
#Sepal length subset
setosa_sepalLen_data = histogram_df[histogram_df['Class'] == 'Iris-setosa']['Sepal_Length']
versicolor_sepalLen_data = histogram_df[histogram_df['Class'] == 'Iris-versicolor']['Sepal_Length']
virginica_sepalLen_data = histogram_df[histogram_df['Class'] == 'Iris-virginica']['Sepal_Length']
#Petal width subset
setosa_PetalWidth_data = histogram_df[histogram_df['Class'] == 'Iris-setosa']['Petal_Width']
versicolor_PetalWidth_data = histogram_df[histogram_df['Class'] == 'Iris-versicolor']['Petal_Width']
virginica_PetalWidth_data = histogram_df[histogram_df['Class'] == 'Iris-virginica']['Petal_Width']
#Petal length subset
setosa_PetalLen_data = histogram_df[histogram_df['Class'] == 'Iris-setosa']['Petal_Length']
versicolor_PetalLen_data = histogram_df[histogram_df['Class'] == 'Iris-versicolor']['Petal_Length']
virginica_PetalLen_data = histogram_df[histogram_df['Class'] == 'Iris-virginica']['Petal_Length']

#########################################
# COMBINED IRIS CLASSES PLOTS 
#########################################

#COMBINED CLASSES - SEPAL WIDTH plot
plt.hist([setosa_sepalWidth_data,versicolor_sepalWidth_data,virginica_sepalWidth_data])
plt.title('Frequency of each Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
plt.savefig("frequency_sepal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - SEPAL LENGTH plot
plt.hist([setosa_sepalLen_data,versicolor_sepalLen_data,virginica_sepalLen_data])
plt.title('Frequency of each Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
plt.savefig("frequency_sepal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - PETAL WIDTH plot
plt.hist([setosa_PetalWidth_data,versicolor_PetalWidth_data,virginica_PetalWidth_data])
plt.title('Frequency of each Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
plt.savefig("frequency_Petal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - PETAL LENGTH plot
plt.hist([setosa_PetalLen_data,versicolor_PetalLen_data,virginica_PetalLen_data])
plt.title('Frequency of each Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
plt.savefig("frequency_Petal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################

######################################
# SETOSA CLASS plots
######################################

#SETOSA CLASS - SEPAL WIDTH plot
plt.hist([setosa_sepalWidth_data])
plt.title('Frequency of each Setosa Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
plt.savefig("frequency_setosa_sepal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - SEPAL LENGTH plot
plt.hist([setosa_sepalLen_data])
plt.title('Frequency of each Setosa Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
plt.savefig("frequency_setosa_sepal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - PETAL WIDTH plot
plt.hist([setosa_PetalWidth_data])
plt.title('Frequency of each Setosa Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
plt.savefig("frequency_setosa_Petal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - PETAL LENGTH plot
plt.hist([setosa_PetalLen_data])
plt.title('Frequency of each Setosa Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
plt.savefig("frequency_setosa_Petal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################

######################################
# VERISICOLOR CLASS plots
######################################

#VERISICOLOR CLASS - SEPAL WIDTH plot
plt.hist([versicolor_sepalWidth_data])
plt.title('Frequency of each versicolor Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)
plt.savefig("frequency_versicolor_sepal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VERISICOLOR CLASS - SEPAL LENGTH plot
plt.hist([versicolor_sepalLen_data])
plt.title('Frequency of each versicolor Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)
plt.savefig("frequency_versicolor_sepal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VERISICOLOR CLASS - PETAL WIDTH plot
plt.hist([versicolor_PetalWidth_data])
plt.title('Frequency of each versicolor Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)
plt.savefig("frequency_versicolor_Petal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VERISICOLOR CLASS - PETAL LENGTH plot
plt.hist([versicolor_PetalLen_data])
plt.title('Frequency of each versicolor Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)
plt.savefig("frequency_versicolor_Petal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################



######################################
# VIRGINICA CLASS plots
######################################

#VIRGINICA CLASS - SEPAL WIDTH plot
plt.hist([virginica_sepalWidth_data])
plt.title('Frequency of each Virginica Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)
plt.savefig("frequency_veriscolor_sepal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VIRGINICA CLASS - SEPAL LENGTH plot
plt.hist([virginica_sepalLen_data])
plt.title('Frequency of each Virginica Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)
plt.savefig("frequency_veriscolor_sepal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VIRGINICA CLASS - PETAL WIDTH plot
plt.hist([virginica_PetalWidth_data])
plt.title('Frequency of each Virginica Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)
plt.savefig("frequency_veriscolor_Petal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VIRGINICA CLASS - PETAL LENGTH plot
plt.hist([virginica_PetalLen_data])
plt.title('Frequency of each Virginica Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)
plt.savefig("frequency_veriscolor_Petal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################







#3.3 
#Outputs a scatter plot of each pair of variables

#3.4
#Performs any other analysis you think is appropriate

