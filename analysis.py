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
import seaborn as sns

#############
#DEFINE VARS
#############
fs=11 # font size for the plot text
legend_fs=6  # font size for the legend text


     
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

#3.2
#Saves a histogram of each variable to png files
#As histgrams deal with numeric columns only, we
#need to remove the non-numerical column i.e. the class flower description
working_df = df # make a working copy of the dataset

#def render_dataset(*indf, title,ylabel, xlabel,legend_title,legend_ol,save_filename,
# save_filename_type="png",display_ploy_yn):
df_list1=working_df.drop('Class',axis=1) # we don't need the Class column, so we can drop it here
df_list2=['Sepal Length', 'Sepal Width','Petal Length','Petal Width'] # These are our column names

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
plt.hist(working_df.drop('Class',axis=1)) #here we dont need the Class column, so drop removes it
plt.title('Frequency of each Sepal and Petal lengths & widths', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Sepal Length', 'Sepal Width','Petal Length','Petal Width'], fontsize = legend_fs)
plt.savefig("histogram_sepal_and_petal_lengths.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()


#Class subsets
#Sepal width subset
sepalWidth_data = working_df['Sepal_Width']
#Sepal length subset
sepalLength_data = working_df['Sepal_Length']
#Petal width subset
petalWidth_data = working_df['Petal_Width']
#Petal length subset
petalLength_data = working_df['Petal_Length']


#col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
#subclass specific data for the 3 Classes
setosa_data = working_df[working_df['Class'] == 'Iris-setosa']
versicolor_data = working_df[working_df['Class'] == 'Iris-versicolor']
virginica_data = working_df[working_df['Class'] == 'Iris-virginica']


#Sepal Class specific width subset
setosa_sepalWidth_data = working_df[working_df['Class'] == 'Iris-setosa']['Sepal_Width']
versicolor_sepalWidth_data = working_df[working_df['Class'] == 'Iris-versicolor']['Sepal_Width']
virginica_sepalWidth_data = working_df[working_df['Class'] == 'Iris-virginica']['Sepal_Width']
#Sepal Class specific length subset
setosa_sepalLen_data = working_df[working_df['Class'] == 'Iris-setosa']['Sepal_Length']
versicolor_sepalLen_data = working_df[working_df['Class'] == 'Iris-versicolor']['Sepal_Length']
virginica_sepalLen_data = working_df[working_df['Class'] == 'Iris-virginica']['Sepal_Length']
#Petal Class specific width subset
setosa_PetalWidth_data = working_df[working_df['Class'] == 'Iris-setosa']['Petal_Width']
versicolor_PetalWidth_data = working_df[working_df['Class'] == 'Iris-versicolor']['Petal_Width']
virginica_PetalWidth_data = working_df[working_df['Class'] == 'Iris-virginica']['Petal_Width']
#Petal Class specific length subset
setosa_PetalLen_data = working_df[working_df['Class'] == 'Iris-setosa']['Petal_Length']
versicolor_PetalLen_data = working_df[working_df['Class'] == 'Iris-versicolor']['Petal_Length']
virginica_PetalLen_data = working_df[working_df['Class'] == 'Iris-virginica']['Petal_Length']

################################################
# SCATTER PLOT - All sepal and petal lengths 
################################################
# Seaborn plot
#lineplot 
#sns.lineplot(x="Sepal_Length", y="Sepal_Width", data=working_df)
#scatter plot
grph = sns.lmplot( x="Sepal_Length" , y="Petal_Length" , data=working_df, hue='Class', legend=False)
plt.title("Scatter plot - combined sepal and petal lengths")
plt.ylabel('Sepal', fontsize=fs)
plt.xlabel('Petal', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen
plt.savefig("scatter_all_sepal_petal_lengths.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#############################################
# SCATTER PLOT - Setosa sepal and petal lengths
#############################################
# First attempt at scatter plot
# Seaborn plot
#lineplot 
#sns.lineplot(x="Sepal_Length", y="Sepal_Width", data=working_df)
#scatter plot
grph=sns.lmplot(x="Sepal_Length" , y="Petal_Length", data=setosa_data, hue='Class', legend=False)
plt.title("Scatter plot - Setosa sepal and petal lengths")
plt.xlabel('Sepal', fontsize=fs)
plt.ylabel('Petal', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen
plt.savefig("scatter_setosa_sepal_petal_lengths.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#################################################
# SCATTER PLOT - Versicolor sepal and petal lengths 
#################################################
# Seaborn plot
#scatter plot
grph=sns.lmplot(x="Sepal_Length" , y="Petal_Length", data=versicolor_data, hue='Class', legend=False)
plt.title("Scatter plot - Versicolor sepal and petal Lengths")
plt.xlabel('Sepal', fontsize=fs)
plt.ylabel('Petal', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen
plt.savefig("scatter_versicolor_sepal_petal_lengths.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#################################################
# SCATTER PLOT - Virginica sepal and petal Lengths 
#################################################
# Seaborn plot
#scatter plot
grph=sns.lmplot(x="Sepal_Length" , y="Petal_Length", data=virginica_data, hue='Class', legend=False)
plt.title("Scatter plot - virginica sepal and petal Lengths")
plt.ylabel('Sepal', fontsize=fs)
plt.xlabel('Petal', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen
plt.savefig("scatter_virginca_sepal_petal_lengths.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()



#########################################
# ALL IRIS CLASSES PLOTS - HISTOGRAM 
#########################################

#ALL CLASSES - SEPAL WIDTH plot
plt.hist([setosa_sepalWidth_data,versicolor_sepalWidth_data,virginica_sepalWidth_data])
plt.title('Frequency of each Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Sepal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
plt.savefig("histogram_frequency_sepal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - SEPAL LENGTH plot
plt.hist([setosa_sepalLen_data,versicolor_sepalLen_data,virginica_sepalLen_data])
plt.title('Frequency of each Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Sepal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
plt.savefig("histogram_frequency_sepal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - PETAL WIDTH plot
plt.hist([setosa_PetalWidth_data,versicolor_PetalWidth_data,virginica_PetalWidth_data])
plt.title('Frequency of each Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Petal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
plt.savefig("histogram_frequency_petal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - PETAL LENGTH plot
plt.hist([setosa_PetalLen_data,versicolor_PetalLen_data,virginica_PetalLen_data])
plt.title('Frequency of each Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Petal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
plt.savefig("histogram_frequency_petal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################

######################################
# SETOSA CLASS plots - HISTOGRAM
######################################

#SETOSA CLASS - SEPAL WIDTH plot
plt.hist([setosa_sepalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Sepal Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
plt.savefig("histogram_frequency_setosa_sepal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - SEPAL LENGTH plot
plt.hist([setosa_sepalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Sepal Length', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
plt.savefig("histogram_frequency_setosa_sepal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - PETAL WIDTH plot
plt.hist([setosa_PetalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Petal Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
plt.savefig("histogram_frequency_setosa_Petal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - PETAL LENGTH plot
plt.hist([setosa_PetalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/
plt.title('Frequency of each Setosa Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Petal Length', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
#plt.width = 1
#plt.tight_layout()
#plt.figsize=(2,5) # ref https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
plt.savefig("histogram_frequency_setosa_Petal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################

######################################
# VERISICOLOR CLASS plots - HISTOGRAM
######################################

#VERISICOLOR CLASS - SEPAL WIDTH plot
plt.hist([versicolor_sepalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each versicolor Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Sepal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)
plt.savefig("histogram_frequency_versicolor_sepal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VERISICOLOR CLASS - SEPAL LENGTH plot
plt.hist([versicolor_sepalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Versicolor Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Sepal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)
plt.savefig("histogram_frequency_versicolor_sepal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VERISICOLOR CLASS - PETAL WIDTH plot
plt.hist([versicolor_PetalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Versicolor Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Petal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)
plt.savefig("histogram_frequency_versicolor_Petal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VERISICOLOR CLASS - PETAL LENGTH plot
plt.hist([versicolor_PetalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Versicolor Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Petal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)
plt.savefig("histogram_frequency_versicolor_Petal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################



######################################
# VIRGINICA CLASS plots - HISTOGRAM
######################################

#VIRGINICA CLASS - SEPAL WIDTH plot
plt.hist([virginica_sepalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Sepal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)
plt.savefig("histogram_frequency_virginica_sepal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VIRGINICA CLASS - SEPAL LENGTH plot
plt.hist([virginica_sepalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Sepal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)
plt.savefig("histogram_frequency_virginica_sepal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VIRGINICA CLASS - PETAL WIDTH plot
plt.hist([virginica_PetalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Petal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)
plt.savefig("histogram_frequency_virginica_petal_width.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VIRGINICA CLASS - PETAL LENGTH plot
plt.hist([virginica_PetalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Petal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)
plt.savefig("histogram_frequency_virginica_petal_length.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################


#3.3 
#Outputs a scatter plot of each pair of variables

#3.4
#Performs any other analysis you think is appropriate

