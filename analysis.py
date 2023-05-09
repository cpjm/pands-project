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
import os

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
    if os.path.isfile(save_filename): os.remove(save_filename) 
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
#      -- Iris-setosa
#      -- Iris-versicolour
#      -- Iris-virginica
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
#ref https://www.w3schools.com/python/pandas/pandas_csv.asp#gsc.tab=0
df = pd.read_csv('data/iris.data',names=col_names)
#debug print(df.to_string()) 

print("___HEAD___________")
print(df.head())
#input("Press Enter to continue...")
print("___TAIL___________")
print(df.tail())
#input("Press Enter to continue...")
print("___DTYPES___________")
print(df.dtypes)
print("___DESCRIBE___________")
print(df.describe())
input("Press Enter to continue...")

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
df_list1=working_df.drop('Class',axis=1).copy() # we don't need the Class column, so we can drop it here
df_list2=['Sepal Length', 'Sepal Width','Petal Length','Petal Width'] # These are our column names

print("START - df.describe(ALL) 1:- ")
df_list1.describe(include='all') 
print("END - df.describe() 1:- ")

# render_dataset(df_list1, 
#                "TEST Frequency of each Sepal and Petal lengths & widths",
#                "TEST Frequency", 
#                "TEST Length",
#                "Class of iris",
#                df_list2,
#             "sepal_and_petal_lengths.png",
#                "png",
#                "Y")

######################################################################
# Histogram of the Sepal and Petal lengths for all 3 classes or iris
######################################################################
#plt.hist(working_df.drop('Class',axis=1)) #here we dont need the Class column, so drop removes it
plt.hist(df_list1)
plt.title('Frequency of each Sepal and Petal lengths & widths', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length & Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Sepal Length', 'Sepal Width','Petal Length','Petal Width'], fontsize = legend_fs)

save_filename="01_histogram_sepal_and_petal_lengths.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

print("1.\n")
df_list1.describe()
input("Press Enter to continue...")


#Class subsets
#Sepal width subset
#pd.DataFrame().assign(Courses=df['Courses'], Duration=df['Duration'])
sepalWidth_data = working_df[['Sepal_Width']]
#print("sepalWidth_data.describe()>")
#sepalWidth_data.describe()

#Sepal length subset
sepalLength_data = working_df[['Sepal_Length']]
#print("sepalLength_data.describe()>")
#df.describe()
#working_df.describe()
#sepalLength_data.describe()

#print("QUITTING!!!!!")
#quit()


#Petal width subset
petalWidth_data = working_df[['Petal_Width']]
print("petalWidth_data.describe()>")
petalWidth_data.describe()
#Petal length subset
petalLength_data = working_df[['Petal_Length']]
print("petalLength_data.describe()>")
petalLength_data.describe()
#input("Press Enter to continue...")


#col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
#subclass specific data for the 3 Classes
setosa_data = working_df[working_df['Class'] == 'Iris-setosa']
versicolor_data = working_df[working_df['Class'] == 'Iris-versicolor']
virginica_data = working_df[working_df['Class'] == 'Iris-virginica']

#print("setosa_data :" , len(setosa_data.index))
#print("versicolor_data :" , len(versicolor_data.index))
#print("virginica_data :" , len(virginica_data.index))
#input("Press Enter to continue...")

#Sepal Class specific width subset
setosa_sepalWidth_data = working_df[working_df['Class'] == 'Iris-setosa']['Sepal_Width']
versicolor_sepalWidth_data = working_df[working_df['Class'] == 'Iris-versicolor']['Sepal_Width']
virginica_sepalWidth_data = working_df[working_df['Class'] == 'Iris-virginica']['Sepal_Width']
#print("setosa_sepalWidth_data :" , len(setosa_sepalWidth_data.index))
#print("versicolor_sepalWidth_data :" , len(versicolor_sepalWidth_data.index))
#print("virginica_sepalWidth_data :" , len(virginica_sepalWidth_data.index))
#input("Press Enter to continue...")

#Sepal Class specific length subset
setosa_sepalLen_data = working_df[working_df['Class'] == 'Iris-setosa']['Sepal_Length']
versicolor_sepalLen_data = working_df[working_df['Class'] == 'Iris-versicolor']['Sepal_Length']
virginica_sepalLen_data = working_df[working_df['Class'] == 'Iris-virginica']['Sepal_Length']
#print("setosa_sepalLen_data :" , len(setosa_sepalLen_data.index))
#print("versicolor_sepalLen_data :" , len(versicolor_sepalLen_data.index))
#print("virginica_sepalLen_data :" , len(virginica_sepalLen_data.index))
#input("Press Enter to continue...")

#Petal Class specific width subset
setosa_PetalWidth_data = working_df[working_df['Class'] == 'Iris-setosa']['Petal_Width']
versicolor_PetalWidth_data = working_df[working_df['Class'] == 'Iris-versicolor']['Petal_Width']
virginica_PetalWidth_data = working_df[working_df['Class'] == 'Iris-virginica']['Petal_Width']
#print("setosa_PetalWidth_data :" , len(setosa_PetalWidth_data.index))
#print("versicolor_PetalWidth_data :" , len(versicolor_PetalWidth_data.index))
#print("virginica_PetalWidth_data :" , len(virginica_PetalWidth_data.index))
#input("Press Enter to continue...")

#Petal Class specific length subset
setosa_PetalLen_data = working_df[working_df['Class'] == 'Iris-setosa']['Petal_Length']
versicolor_PetalLen_data = working_df[working_df['Class'] == 'Iris-versicolor']['Petal_Length']
virginica_PetalLen_data = working_df[working_df['Class'] == 'Iris-virginica']['Petal_Length']
#print("setosa_PetalLen_data :" , len(setosa_PetalLen_data.index))
#print("versicolor_PetalLen_data :" , len(versicolor_PetalLen_data.index))
#print("virginica_PetalWidth_data :" , len(virginica_PetalWidth_data.index))
#input("Press Enter to continue...")
# iterating the columns
#print("virginica_PetalWidth_data.columns:")
#for col in pd.DataFrame(virginica_PetalWidth_data).columns:
#    print(col)
#input("Press Enter to continue...")

# MAX, MIN, MEAN and MEDIAN values set here 
# for each class and also sepal and petal.
PETAL_LENGTH_MIN=petalLength_data.min
PETAL_LENGTH_MAX=petalLength_data.max
PETAL_LENGTH_MEAN=petalLength_data.mean
PETAL_LENGTH_MEDIAN=petalLength_data.median
PETAL_WIDTH_MIN=petalWidth_data.min
PETAL_WIDTH_MAX=petalWidth_data.max
PETAL_WIDTH_MEAN=petalWidth_data.mean
PETAL_WIDTH_MEDIAN=petalWidth_data.median

'''
print("*********************************************************")
print("PETAL_LENGTH_MIN")
print("PETAL_LENGTH_MAX")
print("PETAL_LENGTH_MEAN")
print("PETAL_LENGTH_MEDIAN")
print("PETAL_WIDTH_MIN")
print("PETAL_WIDTH_MAX")
print("PETAL_WIDTH_MEAN")
print("PETAL_WIDTH_MEDIAN")
print(PETAL_LENGTH_MIN)
print(PETAL_LENGTH_MAX)
print(PETAL_LENGTH_MEAN)
print(PETAL_LENGTH_MEDIAN)
print(PETAL_WIDTH_MIN)
print(PETAL_WIDTH_MAX)
print(PETAL_WIDTH_MEAN)
print(PETAL_WIDTH_MEDIAN)
print("*********************************************************")
input("Press Enter to continue...")
'''

SEPAL_LENGTH_MIN=str(sepalLength_data.min)
SEPAL_LENGTH_MAX=str(sepalLength_data.max)
SEPAL_LENGTH_MEAN=str(sepalLength_data.mean)
SEPAL_LENGTH_MEDIAN=str(sepalLength_data.median)
SEPAL_WIDTH_MIN=str(sepalWidth_data.min)
SEPAL_WIDTH_MAX=str(sepalWidth_data.max)
SEPAL_WIDTH_MEAN=str(sepalWidth_data.mean)
SEPAL_WIDTH_MEDIAN=str(sepalWidth_data.median)

SETOSA_PETAL_LENGTH_MIN=str(setosa_PetalLen_data.min)
SETOSA_PETAL_LENGTH_MAX=str(setosa_PetalLen_data.max)
SETOSA_PETAL_LENGTH_MEAN=str(setosa_PetalLen_data.mean)
SETOSA_PETAL_LENGTH_MEDIAN=str(setosa_PetalLen_data.median)
SETOSA_PETAL_WIDTH_MIN=str(setosa_PetalWidth_data.min)
SETOSA_PETAL_WIDTH_MAX=str(setosa_PetalWidth_data.max)
SETOSA_PETAL_WIDTH_MEAN=str(setosa_PetalWidth_data.mean)
SETOSA_PETAL_WIDTH_MEDIAN=str(setosa_PetalWidth_data.median)

SETOSA_SEPAL_LENGTH_MIN=str(setosa_sepalLen_data.min)
SETOSA_SEPAL_LENGTH_MAX=str(setosa_sepalLen_data.max)
SETOSA_SEPAL_LENGTH_MEAN=str(setosa_sepalLen_data.mean)
SETOSA_SEPAL_LENGTH_MEDIAN=str(setosa_sepalLen_data.median)
SETOSA_SEPAL_WIDTH_MIN=str(setosa_sepalWidth_data.min)
SETOSA_SEPAL_WIDTH_MAX=str(setosa_sepalWidth_data.max)
SETOSA_SEPAL_WIDTH_MEAN=str(setosa_sepalWidth_data.mean)
SETOSA_SEPAL_WIDTH_MEDIAN=str(setosa_sepalWidth_data.median)

VERSICOLOR_PETAL_LENGTH_MIN=str(versicolor_PetalLen_data.min)
VERSICOLOR_PETAL_LENGTH_MAX=str(versicolor_PetalLen_data.max)
VERSICOLOR_PETAL_LENGTH_MEAN=str(versicolor_PetalLen_data.mean)
VERSICOLOR_PETAL_LENGTH_MEDIAN=str(versicolor_PetalLen_data.median)
VERSICOLOR_PETAL_WIDTH_MIN=str(versicolor_PetalWidth_data.min)
VERSICOLOR_PETAL_WIDTH_MAX=str(versicolor_PetalWidth_data.max)
VERSICOLOR_PETAL_WIDTH_MEAN=str(versicolor_PetalWidth_data.mean)
VERSICOLOR_PETAL_WIDTH_MEDIAN=str(versicolor_PetalWidth_data.median)

VERSICOLOR_SEPAL_LENGTH_MIN=str(versicolor_sepalLen_data.min)
VERSICOLOR_SEPAL_LENGTH_MAX=str(versicolor_sepalLen_data.max)
VERSICOLOR_SEPAL_LENGTH_MEAN=str(versicolor_sepalLen_data.mean)
VERSICOLOR_SEPAL_LENGTH_MEDIAN=str(versicolor_sepalLen_data.median)
VERSICOLOR_SEPAL_WIDTH_MIN=str(versicolor_sepalWidth_data.min)
VERSICOLOR_SEPAL_WIDTH_MAX=str(versicolor_sepalWidth_data.max)
VERSICOLOR_SEPAL_WIDTH_MEAN=str(versicolor_sepalWidth_data.mean)
VERSICOLOR_SEPAL_WIDTH_MEDIAN=str(versicolor_sepalWidth_data.median)

VIRGINICA_PETAL_LENGTH_MIN=str(virginica_PetalLen_data.min)
VIRGINICA_PETAL_LENGTH_MAX=str(virginica_PetalLen_data.max)
VIRGINICA_PETAL_LENGTH_MEAN=str(virginica_PetalLen_data.mean)
VIRGINICA_PETAL_LENGTH_MEDIAN=str(virginica_PetalLen_data.median)
VIRGINICA_PETAL_WIDTH_MIN=str(virginica_PetalWidth_data.min)
VIRGINICA_PETAL_WIDTH_MAX=str(virginica_PetalWidth_data.max)
VIRGINICA_PETAL_WIDTH_MEAN=str(virginica_PetalWidth_data.mean)
VIRGINICA_PETAL_WIDTH_MEDIAN=str(virginica_PetalWidth_data.median)

VIRGINICA_SEPAL_LENGTH_MIN=str(virginica_sepalLen_data.min)
VIRGINICA_SEPAL_LENGTH_MAX=str(virginica_sepalLen_data.max)
VIRGINICA_SEPAL_LENGTH_MEAN=str(virginica_sepalLen_data.mean)
VIRGINICA_SEPAL_LENGTH_MEDIAN=str(virginica_sepalLen_data.median)
VIRGINICA_SEPAL_WIDTH_MIN=str(virginica_sepalWidth_data.min)
VIRGINICA_SEPAL_WIDTH_MAX=str(virginica_sepalWidth_data.max)
VIRGINICA_SEPAL_WIDTH_MEAN=str(virginica_sepalWidth_data.mean)
VIRGINICA_SEPAL_WIDTH_MEDIAN=str(virginica_sepalWidth_data.median)

###########################
#Print useful info
###########################
# iterating the columns
'''
for col in df.columns:
    print(col)
# iterating the columns
for col in df_list1.columns:
    print(col)
'''
# iterating the columns
print("working_df.columns:")
for col in working_df.columns:
    print(col)
# iterating the columns
print("sepalLength_data.columns:")
sepalLength_data.describe()
for col in sepalLength_data.columns:
    print(col)
# iterating the columns
print("sepalWidth_data.columns:")
for col in sepalWidth_data.columns:
    print(col)



################################################
# SCATTER PLOT - All sepal and petal lengths 
################################################
# Seaborn plot
#lineplot 
#sns.lineplot(x="Sepal_Length", y="Sepal_Width", data=working_df)
#scatter plot
grph = sns.lmplot( x="Sepal_Length" , y="Petal_Length" , data=working_df, hue='Class', legend=True)
plt.title("Scatter plot - combined sepal and petal lengths")
plt.xlabel('Sepal Length cm', fontsize=fs)
plt.ylabel('Petal Length cm', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen

# Label each point with its value
'''
for line in range(0,working_df.shape[0]):
         plt.text(working_df["Sepal_Length"][line]+0.01, working_df["Petal_Length"][line], 
                 working_df["Class"][line], horizontalalignment='left', 
                 size='medium', color='black', weight='semibold')
'''
             
save_filename="02_scatter_all_sepal_petal_lengths.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.show()
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
plt.xlabel('Sepal Length cm', fontsize=fs)
plt.ylabel('Petal Length cm', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen

save_filename="03_scatter_setosa_sepal_petal_lengths.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#################################################
# SCATTER PLOT - Versicolor sepal and petal lengths 
#################################################
# Seaborn plot
#scatter plot
grph=sns.lmplot(x="Sepal_Length" , y="Petal_Length", data=versicolor_data, hue='Class', legend=False)
plt.title("Scatter plot - Versicolor sepal and petal Lengths")
plt.xlabel('Sepal Length cm', fontsize=fs)
plt.ylabel('Petal Length cm', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen

save_filename="04_scatter_versicolor_sepal_petal_lengths.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#################################################
# SCATTER PLOT - Virginica sepal and petal Lengths
#################################################
# Seaborn plot
#scatter plot
grph=sns.lmplot(x="Sepal_Length" , y="Petal_Length", data=virginica_data, hue='Class', legend=False)
plt.title("Scatter plot - virginica sepal and petal Lengths")
plt.xlabel('Sepal Length cm', fontsize=fs)
plt.ylabel('Petal Length cm', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen
plt.savefig("05_scatter_virginca_sepal_petal_lengths.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()



#########################################
# HISTOGRAM PLOTS  
#########################################

#ALL CLASSES - SEPAL WIDTH plot
plt.hist([setosa_sepalWidth_data,versicolor_sepalWidth_data,virginica_sepalWidth_data])
plt.title('Frequency of each Sepal width', fontsize=fs)
plt.xlabel('Sepal Width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="06_histogram_frequency_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

##########################################
# COMBINED CLASSES - SEPAL LENGTH plot
##########################################
plt.hist([setosa_sepalLen_data,versicolor_sepalLen_data,virginica_sepalLen_data])
plt.title('Frequency of each Sepal length', fontsize=fs)
plt.xlabel('Sepal Length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="07_histogram_frequency_sepal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

######################################
# COMBINED CLASSES - PETAL WIDTH plot
######################################
plt.hist([setosa_PetalWidth_data,versicolor_PetalWidth_data,virginica_PetalWidth_data])
plt.title('Frequency of each Petal width', fontsize=fs)
plt.xlabel('Petal Width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="08_histogram_frequency_petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

########################################
# COMBINED CLASSES - PETAL LENGTH plot
########################################
plt.hist([setosa_PetalLen_data,versicolor_PetalLen_data,virginica_PetalLen_data])
plt.title('Frequency of each Petal length', fontsize=fs)
plt.xlabel('Petal Length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="09_histogram_frequency_petal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################

######################################
# HISTOGRAM - SETOSA CLASS plots 
######################################

###################################
# SETOSA CLASS - SEPAL WIDTH plot
###################################
plt.hist([setosa_sepalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Sepal width', fontsize=fs)
plt.xlabel('Setosa Sepal Width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="10_histogram_frequency_setosa_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

########################################
# SETOSA CLASS - SEPAL LENGTH plot
########################################
plt.hist([setosa_sepalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Sepal length', fontsize=fs)
plt.xlabel('Setosa Sepal Length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="11_histogram_frequency_setosa_sepal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#####################################
# SETOSA CLASS - PETAL WIDTH plot
#####################################
plt.hist([setosa_PetalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Petal width', fontsize=fs)
plt.xlabel('Setosa Petal Width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="12_histogram_frequency_setosa_Petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

####################################
# SETOSA CLASS - PETAL LENGTH plot
####################################
plt.hist([setosa_PetalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/
plt.title('Frequency of each Setosa Petal length', fontsize=fs)
plt.xlabel('Setosa Petal Length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
#plt.width = 1
#plt.tight_layout()
#plt.figsize=(2,5) # ref https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html

save_filename="13_histogram_frequency_setosa_Petal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################


################################################
# SCATTER PLOT - All sepal and petal widths
################################################
# Seaborn plot
#lineplot 
#sns.lineplot(x="Sepal_Width", y="Sepal_Width", data=working_df)
#scatter plot
grph = sns.lmplot( x="Sepal_Width" , y="Petal_Width" , data=working_df, hue='Class', legend=True)
plt.title("Scatter plot - combined sepal and petal widths")
plt.xlabel('Sepal Width cm', fontsize=fs)
plt.ylabel('Petal Width cm', fontsize=fs)
#plt.legend(title='Class of iris')
#plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
grph.fig.tight_layout() # helps it fit on the screen

save_filename="14_scatter_all_sepal_petal_widths.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#############################################
# SCATTER PLOT - Setosa sepal and petal widths
#############################################
# First attempt at scatter plot
# Seaborn plot
#lineplot 
#sns.lineplot(x="Sepal_Width", y="Sepal_Width", data=working_df)
#scatter plot
grph=sns.lmplot(x="Sepal_Width" , y="Petal_Width", data=setosa_data, hue='Class', legend=False)
plt.title("Scatter plot - Setosa sepal and petal widths")
plt.xlabel('Sepal Width cm', fontsize=fs)
plt.ylabel('Petal Width cm', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen

save_filename="15_scatter_setosa_sepal_petal_widths.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#################################################
# SCATTER PLOT - Versicolor sepal and petal widths
#################################################
# Seaborn plot
#scatter plot
grph=sns.lmplot(x="Sepal_Width" , y="Petal_Width", data=versicolor_data, hue='Class', legend=False)
plt.title("Scatter plot - Versicolor sepal and petal Widths")
plt.xlabel('Sepal Width cm', fontsize=fs)
plt.ylabel('Petal Width cm', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen

save_filename="16_scatter_versicolor_sepal_petal_widths.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#################################################
# SCATTER PLOT - Virginica sepal and petal Widths 
#################################################
# Seaborn plot
#scatter plot
grph=sns.lmplot(x="Sepal_Width" , y="Petal_Width", data=virginica_data, hue='Class', legend=False)
plt.title("Scatter plot - virginica sepal and petal Widths")
plt.xlabel('Sepal Width cm', fontsize=fs)
plt.ylabel('Petal Width cm', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen

save_filename="17_scatter_virginca_sepal_petal_widths.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()



#########################################
# HISTOGRAM PLOTS  
#########################################

#################################
# ALL CLASSES - SEPAL WIDTH plot
#################################
plt.hist([setosa_sepalWidth_data,versicolor_sepalWidth_data,virginica_sepalWidth_data])
plt.title('Frequency of each Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Sepal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="18_histogram_frequency_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#########################################
# COMBINED CLASSES - SEPAL LENGTH plot
#########################################
plt.hist([setosa_sepalLen_data,versicolor_sepalLen_data,virginica_sepalLen_data])
plt.title('Frequency of each Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Sepal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="19_histogram_frequency_sepal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - PETAL WIDTH plot
plt.hist([setosa_PetalWidth_data,versicolor_PetalWidth_data,virginica_PetalWidth_data])
plt.title('Frequency of each Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Petal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="20_histogram_frequency_petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - PETAL LENGTH plot
plt.hist([setosa_PetalLen_data,versicolor_PetalLen_data,virginica_PetalLen_data])
plt.title('Frequency of each Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Petal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="21_histogram_frequency_petal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################

######################################
# HISTOGRAM - SETOSA CLASS plots 
######################################


#####################################
# SETOSA CLASS - SEPAL WIDTH plot
#####################################
plt.hist([setosa_sepalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Sepal Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="22_histogram_frequency_setosa_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

####################################
# SETOSA CLASS - SEPAL LENGTH plot
####################################
plt.hist([setosa_sepalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Sepal Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="23_histogram_frequency_setosa_sepal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

###################################
# SETOSA CLASS - PETAL WIDTH plot
###################################
plt.hist([setosa_PetalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Petal Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="24_histogram_frequency_setosa_Petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

###################################
# SETOSA CLASS - PETAL LENGTH plot
###################################
plt.hist([setosa_PetalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/
plt.title('Frequency of each Setosa Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Petal Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
#plt.width = 1
#plt.tight_layout()
#plt.figsize=(2,5) # ref https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html

save_filename="25_histogram_frequency_setosa_Petal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################




######################################
# HISTOGRAM - VERISICOLOR CLASS plots 
######################################

#######################################
# VERISICOLOR CLASS - SEPAL WIDTH plot
#######################################
plt.hist([versicolor_sepalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each versicolor Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Sepal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)

save_filename="26_histogram_frequency_versicolor_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

##########################################
# VERISICOLOR CLASS - SEPAL LENGTH plot
##########################################
plt.hist([versicolor_sepalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Versicolor Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Sepal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)

save_filename="27_histogram_frequency_versicolor_sepal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#########################################
# VERISICOLOR CLASS - PETAL WIDTH plot
#########################################
plt.hist([versicolor_PetalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Versicolor Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Petal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)

save_filename="28_histogram_frequency_versicolor_Petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#########################################
# VERISICOLOR CLASS - PETAL LENGTH plot
#########################################
plt.hist([versicolor_PetalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Versicolor Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Petal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)

save_filename="29_histogram_frequency_versicolor_Petal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################



######################################
# HISTOGRAM - VIRGINICA CLASS plots 
######################################

###################################
# VIRGINICA CLASS - SEPAL WIDTH plot
###################################
plt.hist([virginica_sepalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Sepal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)

save_filename="30_histogram_frequency_virginica_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

######################################
# VIRGINICA CLASS - SEPAL LENGTH plot
######################################
plt.hist([virginica_sepalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Sepal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)

save_filename="31_histogram_frequency_virginica_sepal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#####################################
# VIRGINICA CLASS - PETAL WIDTH plot
#####################################
plt.hist([virginica_PetalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Petal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)

save_filename="32_histogram_frequency_virginica_petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#####################################
# VIRGINICA CLASS - PETAL LENGTH plot
#####################################
plt.hist([virginica_PetalLen_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Petal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)

save_filename="33_histogram_frequency_virginica_petal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

###################################################################################################
# trying a new fancy seaborn plot
# as found on https://stackoverflow.com/questions/6282058/writing-numerical-values-on-the-plot-with-matplotlib
# and changed for my dataframe
###################################################################################################
sns.set()
#iris = sns.load_dataset('working_df')
# make the 'Class' column categorical to fix the order
#iris=df
df['Class'] = pd.Categorical(df['Class'])
fig, axs = plt.subplots(2, 2, figsize=(12, 6))
for col, ax in zip(df.columns[:4], axs.flat):
    sns.histplot(data=df, x=col, kde=True, hue='Class', common_norm=False, legend=ax==axs[0,0], ax=ax)
plt.tight_layout()
save_filename="34_seaborn_histogram_kde_curve_all_iris_class_per_feature.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()


#3.3 
#Outputs a scatter plot of each pair of variables

#3.4
#Performs any other analysis you think is appropriate
