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
iris_data = pd.read_csv('data/iris.data',names=col_names)
#debug print(df.to_string()) 

print("___HEAD___________")
print(iris_data.head())
#input("Press Enter to continue...")
print("___TAIL___________")
print(iris_data.tail())
#input("Press Enter to continue...")
print("___DTYPES___________")
print(iris_data.dtypes)
input("Press Enter to continue...")

#3.1
# Generate useful summary info to the outout file "iris_summary.txt"
#ref https://pandashowto.com/how-to-save-dataframe-as-text-file/
#I analyse this data further and what it means in my research
#df.to_string("myfile.txt")
#ref https://www.w3schools.com/python/pandas/ref_df_describe.asp
#debug print(df.describe())
iris_data.describe().to_string("iris_summary.txt")
if display_plots_to_screen: print(iris_data.describe(''))

#3.2
#Saves a histogram of each variable to png files
#As histgrams deal with numeric columns only, we
#need to remove the non-numerical column i.e. the class flower description

    
#def render_dataset(*indf, title,ylabel, xlabel,legend_title,legend_ol,save_filename,
# save_filename_type="png",display_ploy_yn):
#df_list1=iris_data.drop('Class',axis=1) # we don't need the Class column, so we can drop it here
#df_list2=['Sepal Length', 'Sepal Width','Petal Length','Petal Width'] # These are our column names

#print("START - df.describe(ALL) 1:- ")
#df_list1.describe(include='all') 
#print("END - df.describe() 1:- ")


#Histogram of the Sepal and Petal lengths for all 3 classes or iris
plt.hist(iris_data.drop('Class',axis=1)) #here we dont need the Class column, so drop removes it
plt.title('Frequency of each Sepal and Petal lengths & widths', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Sepal Length', 'Sepal Width','Petal Length','Petal Width'], fontsize = legend_fs)

save_filename="histogram_sepal_and_petal_lengths.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()


#Class subsets
#Sepal width subset
#pd.DataFrame().assign(Courses=df['Courses'], Duration=df['Duration'])
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
sepalWidth_data = iris_data[['Sepal_Width']].copy()
print("sepalWidth_data.describe()>")
input("Press Enter to continue...")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
sepalWidth_data.describe()
input("Press Enter to continue...")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
sepalWidth_data = iris_data.Sepal_Width.copy()
print("sepalWidth_data.describe()>")
sepalWidth_data.describe()
input("Press Enter to continue...")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")




print("sepalWidth_data:- ", sepalWidth_data)
input("Press Enter to continue...")

#Sepal length subset
sepalLength_data = iris_data[['Sepal_Length']].copy()
print("sepalLength_data.describe()>")
iris_data.describe()
input("Press Enter to continue...")
print("sepalLength_data.describe()")
sepalLength_data.describe()
input("Press Enter to continue...")

#print("QUITTING!!!!!")
#quit()


#Petal width subset
petalWidth_data = iris_data.filter(['Petal_Width'], axis=1)
print("petalWidth_data.describe()>")
petalWidth_data.describe()
#Petal length subset
petalLength_data = iris_data.filter(['Petal_Length'], axis=1)
print("petalLength_data.describe()>")
petalLength_data.describe()
input("Press Enter to continue...")


#col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
#subclass specific data for the 3 Classes
setosa_data = iris_data[iris_data['Class'] == 'Iris-setosa'].copy()
versicolor_data = iris_data[iris_data['Class'] == 'Iris-versicolor'].copy()
virginica_data = iris_data[iris_data['Class'] == 'Iris-virginica'].copy()

#print("setosa_data :" , len(setosa_data.index))
#print("versicolor_data :" , len(versicolor_data.index))
#print("virginica_data :" , len(virginica_data.index))
#input("Press Enter to continue...")

#Sepal Class specific width subset
setosa_sepalWidth_data = setosa_data[['Sepal_Width']].copy()
versicolor_sepalWidth_data = versicolor_data[['Sepal_Width']].copy()
virginica_sepalWidth_data = virginica_data[['Sepal_Width']].copy()
print("setosa_sepalWidth_data :" , len(setosa_sepalWidth_data.index))
print("versicolor_sepalWidth_data :" , len(versicolor_sepalWidth_data.index))
print("virginica_sepalWidth_data :" , len(virginica_sepalWidth_data.index))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
input("Press Enter to continue...")

#Sepal Class specific length subset
setosa_sepalLength_data = setosa_data[['Sepal_Length']].copy()
versicolor_sepalLength_data = versicolor_data[['Sepal_Length']].copy()
virginica_sepalLength_data = virginica_data[['Sepal_Length']].copy()
#print("setosa_sepalLength_data :" , len(setosa_sepalLength_data.index))
#print("versicolor_sepalLength_data :" , len(versicolor_sepalLength_data.index))
#print("virginica_sepalLength_data :" , len(virginica_sepalLength_data.index))
#input("Press Enter to continue...")

#Petal Class specific width subset
setosa_PetalWidth_data = setosa_data[['Petal_Width']].copy()
versicolor_PetalWidth_data = versicolor_data[['Petal_Width']].copy()
virginica_PetalWidth_data = virginica_data[['Petal_Width']].copy()
#print("setosa_PetalWidth_data :" , len(setosa_PetalWidth_data.index))
#print("versicolor_PetalWidth_data :" , len(versicolor_PetalWidth_data.index))
#print("virginica_PetalWidth_data :" , len(virginica_PetalWidth_data.index))
#input("Press Enter to continue...")

#Petal Class specific length subset
setosa_PetalLength_data = setosa_data[['Petal_Length']].copy()
versicolor_PetalLength_data = versicolor_data[['Petal_Length']].copy()
virginica_PetalLength_data = virginica_data[['Petal_Length']].copy()

#print("setosa_PetalLength_data :" , len(setosa_PetalLength_data.index))
#print("versicolor_PetalLength_data :" , len(versicolor_PetalLength_data.index))
#print("virginica_PetalWidth_data :" , len(virginica_PetalWidth_data.index))
#input("Press Enter to continue...")
# iterating the columns
#print("virginica_PetalWidth_data.columns:")
#for col in pd.DataFrame(virginica_PetalWidth_data).columns:
#    print(col)
#input("Press Enter to continue...")

# MAX, MIN, MEAN and MEDIAN values set here 
# for each class and also sepal and petal.
#for col in pd.DataFrame(petalLength_data).columns:
#    print(col)
#input("Press Enter to continue...")
#for col in pd.DataFrame(petalWidth_data).columns:
#    print(col)
#input("Press Enter to continue...")

PETAL_LENGTH_MIN=str(petalLength_data.min())#(axis='Petal_Length')
PETAL_LENGTH_MAX=str(petalLength_data.max())#(axis='Petal_Length')
PETAL_LENGTH_MEAN=str(petalLength_data.mean())#(axis='Petal_Length')
PETAL_LENGTH_MEDIAN=str(petalLength_data.median())#(axis='Petal_Length')
PETAL_WIDTH_MIN=str(petalWidth_data.min())#(axis='Petal_Width')
PETAL_WIDTH_MAX=str(petalWidth_data.max())#(axis='Petal_Width')
PETAL_WIDTH_MEAN=str(petalWidth_data.mean())#(axis='Petal_Width')
PETAL_WIDTH_MEDIAN=str(petalWidth_data.median())#(axis='Petal_Width')

print("#################################################################################")
print("#################################################################################")
print(PETAL_LENGTH_MIN)
print(PETAL_LENGTH_MAX)#(axis='Petal_Length')
print(PETAL_LENGTH_MEAN)#(axis='Petal_Length')
print(PETAL_LENGTH_MEDIAN)#(axis='Petal_Length')
print(PETAL_WIDTH_MIN)#(axis='Petal_Width')
print(PETAL_WIDTH_MAX)#(axis='Petal_Width')
print(PETAL_WIDTH_MEAN)#(axis='Petal_Width')
print(PETAL_WIDTH_MEDIAN)#(axis='Petal_Width')
input("Press Enter to continue...")
print("#################################################################################")
print("#################################################################################")


SEPAL_LENGTH_MIN=str(sepalLength_data.min() )#(axis='Sepal_Length'))
SEPAL_LENGTH_MAX=str(sepalLength_data.max() )#(axis='Sepal_Length'))
SEPAL_LENGTH_MEAN=str(sepalLength_data.mean() )#(axis='Sepal_Length'))
SEPAL_LENGTH_MEDIAN=str(sepalLength_data.median() )#(axis='Sepal_Length'))
SEPAL_WIDTH_MIN=str(sepalWidth_data.min() )#(axis='Sepal_Width'))
SEPAL_WIDTH_MAX=str(sepalWidth_data.max() )#(axis='Sepal_Width'))
SEPAL_WIDTH_MEAN=str(sepalWidth_data.mean() )#(axis='Sepal_Width'))
SEPAL_WIDTH_MEDIAN=str(sepalWidth_data.median() )#(axis='Sepal_Width'))

SETOSA_PETAL_LENGTH_MIN=str(setosa_PetalLength_data.min() )#(axis='Petal_Length'))
SETOSA_PETAL_LENGTH_MAX=str(setosa_PetalLength_data.max() )#(axis='Petal_Length'))
SETOSA_PETAL_LENGTH_MEAN=str(setosa_PetalLength_data.mean() )#(axis='Petal_Length'))
SETOSA_PETAL_LENGTH_MEDIAN=str(setosa_PetalLength_data.median() )#(axis='Petal_Length'))
SETOSA_PETAL_WIDTH_MIN=str(setosa_PetalWidth_data.min() )#(axis='Petal_Width'))
SETOSA_PETAL_WIDTH_MAX=str(setosa_PetalWidth_data.max() )#(axis='Petal_Width'))
SETOSA_PETAL_WIDTH_MEAN=str(setosa_PetalWidth_data.mean() )#(axis='Petal_Width'))
SETOSA_PETAL_WIDTH_MEDIAN=str(setosa_PetalWidth_data.median() )#(axis='Petal_Width'))

SETOSA_SEPAL_LENGTH_MIN=str(setosa_sepalLength_data.min() )#(axis='Sepal_Length'))
SETOSA_SEPAL_LENGTH_MAX=str(setosa_sepalLength_data.max() )#(axis='Sepal_Length'))
SETOSA_SEPAL_LENGTH_MEAN=str(setosa_sepalLength_data.mean() )#(axis='Sepal_Length'))
SETOSA_SEPAL_LENGTH_MEDIAN=str(setosa_sepalLength_data.median() )#(axis='Sepal_Length'))
SETOSA_SEPAL_WIDTH_MIN=str(setosa_sepalWidth_data.min() )#(axis='Sepal_Width'))
SETOSA_SEPAL_WIDTH_MAX=str(setosa_sepalWidth_data.max() )#(axis='Sepal_Width'))
SETOSA_SEPAL_WIDTH_MEAN=str(setosa_sepalWidth_data.mean() )#(axis='Sepal_Width'))
SETOSA_SEPAL_WIDTH_MEDIAN=str(setosa_sepalWidth_data.median() )#(axis='Sepal_Width'))

VERSICOLOR_PETAL_LENGTH_MIN=str(versicolor_PetalLength_data.min() )#(axis='Petal_Length'))
VERSICOLOR_PETAL_LENGTH_MAX=str(versicolor_PetalLength_data.max() )#(axis='Petal_Length'))
VERSICOLOR_PETAL_LENGTH_MEAN=str(versicolor_PetalLength_data.mean() )#(axis='Petal_Length'))
VERSICOLOR_PETAL_LENGTH_MEDIAN=str(versicolor_PetalLength_data.median() )#(axis='Petal_Length'))
VERSICOLOR_PETAL_WIDTH_MIN=str(versicolor_PetalWidth_data.min() )#(axis='Petal_Width'))
VERSICOLOR_PETAL_WIDTH_MAX=str(versicolor_PetalWidth_data.max() )#(axis='Petal_Width'))
VERSICOLOR_PETAL_WIDTH_MEAN=str(versicolor_PetalWidth_data.mean() )#(axis='Petal_Width'))
VERSICOLOR_PETAL_WIDTH_MEDIAN=str(versicolor_PetalWidth_data.median() )#(axis='Petal_Width'))

VERSICOLOR_SEPAL_LENGTH_MIN=str(versicolor_sepalLength_data.min() )#(axis='Sepal_Length'))
VERSICOLOR_SEPAL_LENGTH_MAX=str(versicolor_sepalLength_data.max() )#(axis='Sepal_Length'))
VERSICOLOR_SEPAL_LENGTH_MEAN=str(versicolor_sepalLength_data.mean() )#(axis='Sepal_Length'))
VERSICOLOR_SEPAL_LENGTH_MEDIAN=str(versicolor_sepalLength_data.median() )#(axis='Sepal_Length'))
VERSICOLOR_SEPAL_WIDTH_MIN=str(versicolor_sepalWidth_data.min() )#(axis='Sepal_Width'))
VERSICOLOR_SEPAL_WIDTH_MAX=str(versicolor_sepalWidth_data.max() )#(axis='Sepal_Width'))
VERSICOLOR_SEPAL_WIDTH_MEAN=str(versicolor_sepalWidth_data.mean() )#(axis='Sepal_Width'))
VERSICOLOR_SEPAL_WIDTH_MEDIAN=str(versicolor_sepalWidth_data.median() )#(axis='Sepal_Width'))

VIRGINICA_PETAL_LENGTH_MIN=str(virginica_PetalLength_data.min() )#(axis='Petal_Length'))
VIRGINICA_PETAL_LENGTH_MAX=str(virginica_PetalLength_data.max() )#(axis='Petal_Length'))
VIRGINICA_PETAL_LENGTH_MEAN=str(virginica_PetalLength_data.mean() )#(axis='Petal_Length'))
VIRGINICA_PETAL_LENGTH_MEDIAN=str(virginica_PetalLength_data.median() )#(axis='Petal_Length'))
VIRGINICA_PETAL_WIDTH_MIN=str(virginica_PetalWidth_data.min() )#(axis='Petal_Length'))
VIRGINICA_PETAL_WIDTH_MAX=str(virginica_PetalWidth_data.max() )#(axis='Petal_Length'))
VIRGINICA_PETAL_WIDTH_MEAN=str(virginica_PetalWidth_data.mean() )#(axis='Petal_Length'))
VIRGINICA_PETAL_WIDTH_MEDIAN=str(virginica_PetalWidth_data.median() )#(axis='Petal_Length'))

VIRGINICA_SEPAL_LENGTH_MIN=str(virginica_sepalLength_data.min() )#(axis='Sepal_Length'))
VIRGINICA_SEPAL_LENGTH_MAX=str(virginica_sepalLength_data.max() )#(axis='Sepal_Length'))
VIRGINICA_SEPAL_LENGTH_MEAN=str(virginica_sepalLength_data.mean() )#(axis='Sepal_Length'))
VIRGINICA_SEPAL_LENGTH_MEDIAN=str(virginica_sepalLength_data.median() )#(axis='Sepal_Length'))
VIRGINICA_SEPAL_WIDTH_MIN=str(virginica_sepalWidth_data.min() )#(axis='Sepal_Length'))
VIRGINICA_SEPAL_WIDTH_MAX=str(virginica_sepalWidth_data.max() )#(axis='Sepal_Length'))
VIRGINICA_SEPAL_WIDTH_MEAN=str(virginica_sepalWidth_data.mean() )#(axis='Sepal_Length'))
VIRGINICA_SEPAL_WIDTH_MEDIAN=str(virginica_sepalWidth_data.median() )#(axis='Sepal_Length'))


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

# iterating the columns
print("iris_data.columns:")
print("sepalLength_data.columns:")
sepalLength_data.describe()
for col in sepalLength_data.columns:
    print(col)
# iterating the columns
print("sepalWidth_data.columns:")
for col in sepalWidth_data.columns:
    print(col)
'''



################################################
# SCATTER PLOT - All sepal and petal lengths 
################################################
# Seaborn plot
#lineplot 
#sns.lineplot(x="Sepal_Length", y="Sepal_Width", data=iris_data)
#scatter plot
grph = sns.lmplot(x="Sepal_Length" , y="Petal_Length" , data=iris_data, hue='Class', legend=True)
plt.title("Scatter plot - combined sepal and petal lengths")
plt.xlabel('Sepal Length cm', fontsize=fs)
plt.ylabel('Petal Length cm', fontsize=fs)
#plt.annotate("Min:"+str(iris_data.min)+"cm Max:"+str(iris_data.max)+"cm")
#plt.annotate('Note added at (0,0)', xy = (0, 0), xycoords='axes fraction')
#plt.annotate('Note added at (0,1)', xy = (0, 1), xycoords='axes fraction')
#plt.annotate('Note added at (1,0)', xy = (1, 0), xycoords='axes fraction')
#plt.annotate('Note added at (1,1)', xy = (1, 1), xycoords='axes fraction')
#plt.legend(title='Class of iris')
#plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
grph.fig.tight_layout() # helps it fit on the screen


statsText=""
statsText=\
   "Petal Stats - Min:" \
   + str(PETAL_LENGTH_MIN) + " Max:" + str(PETAL_LENGTH_MIN) + \
   " Mean:" + str(PETAL_LENGTH_MEAN) + " Max:" + str(PETAL_LENGTH_MEDIAN) + \
   " Sepal Stats - Min:" \
   + str(SEPAL_LENGTH_MIN) + " Max:" + str(SEPAL_LENGTH_MAX) + \
   " Mean:" + str(SEPAL_LENGTH_MEAN) + " Median:" + str(SEPAL_LENGTH_MEDIAN)

'''
plt.annotate(statsText,
            xy = (1.0, -0.2),
            xycoords='axes fraction',
            ha='right',
            va='bottom',
            fontsize=8)
'''

save_filename="scatter_all_sepal_petal_lengths.png"
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
#sns.lineplot(x="Sepal_Length", y="Sepal_Width", data=iris_data)
#scatter plot
grph=sns.lmplot(x="Sepal_Length" , y="Petal_Length", data=setosa_data, hue='Class', legend=False)
plt.title("Scatter plot - Setosa sepal and petal lengths")
plt.xlabel('Sepal Length cm', fontsize=fs)
plt.ylabel('Petal Length cm', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen

save_filename="scatter_setosa_sepal_petal_lengths.png"
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

save_filename="scatter_versicolor_sepal_petal_lengths.png"
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
plt.savefig("scatter_virginca_sepal_petal_lengths.png", format="png")
if display_plots_to_screen: plt.show()
plt.close()



#########################################
# HISTOGRAM PLOTS  
#########################################

#ALL CLASSES - SEPAL WIDTH plot
#plt.hist([setosa_sepalWidth_data.flatten(),versicolor_sepalWidth_data.flatten(),virginica_sepalWidth_data.flatten()])
plt.hist([sepalWidth_data])
plt.title('Frequency of each Sepal width', fontsize=fs)
plt.xlabel('Sepal Width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="histogram_frequency_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - SEPAL LENGTH plot
plt.hist([setosa_sepalLength_data,versicolor_sepalLength_data,virginica_sepalLength_data])
#plt.hist([sepalLength_data])
plt.title('Frequency of each Sepal length', fontsize=fs)
plt.xlabel('Sepal Length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="histogram_frequency_sepal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - PETAL WIDTH plot
plt.hist([setosa_PetalWidth_data,versicolor_PetalWidth_data,virginica_PetalWidth_data])
plt.title('Frequency of each Petal width', fontsize=fs)
plt.xlabel('Petal Width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="histogram_frequency_petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - PETAL LENGTH plot
plt.hist([setosa_PetalLength_data,versicolor_PetalLength_data,virginica_PetalLength_data])
plt.title('Frequency of each Petal length', fontsize=fs)
plt.xlabel('Petal Length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="histogram_frequency_petal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################

######################################
# HISTOGRAM - SETOSA CLASS plots 
######################################

#SETOSA CLASS - SEPAL WIDTH plot
plt.hist([setosa_sepalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Sepal width', fontsize=fs)
plt.xlabel('Setosa Sepal Width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="histogram_frequency_setosa_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - SEPAL LENGTH plot
plt.hist([setosa_sepalLength_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Sepal length', fontsize=fs)
plt.xlabel('Setosa Sepal Length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="histogram_frequency_setosa_sepal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - PETAL WIDTH plot
plt.hist([setosa_PetalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Petal width', fontsize=fs)
plt.xlabel('Setosa Petal Width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="histogram_frequency_setosa_Petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - PETAL LENGTH plot
plt.hist([setosa_PetalLength_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/
plt.title('Frequency of each Setosa Petal length', fontsize=fs)
plt.xlabel('Setosa Petal Length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
#plt.width = 1
#plt.tight_layout()
#plt.figsize=(2,5) # ref https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html

save_filename="histogram_frequency_setosa_Petal_length.png"
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
#sns.lineplot(x="Sepal_Width", y="Sepal_Width", data=iris_data)
#scatter plot
grph = sns.lmplot( x="Sepal_Width" , y="Petal_Width" , data=iris_data, hue='Class', legend=True)
plt.title("Scatter plot - combined sepal and petal widths")
plt.xlabel('Sepal Width cm', fontsize=fs)
plt.ylabel('Petal Width cm', fontsize=fs)
#plt.legend(title='Class of iris')
#plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)
grph.fig.tight_layout() # helps it fit on the screen

save_filename="scatter_all_sepal_petal_widths.png"
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
#sns.lineplot(x="Sepal_Width", y="Sepal_Width", data=iris_data)
#scatter plot
grph=sns.lmplot(x="Sepal_Width" , y="Petal_Width", data=setosa_data, hue='Class', legend=False)
plt.title("Scatter plot - Setosa sepal and petal widths")
plt.xlabel('Sepal Width cm', fontsize=fs)
plt.ylabel('Petal Width cm', fontsize=fs)
grph.fig.tight_layout() # helps it fit on the screen

save_filename="scatter_setosa_sepal_petal_widths.png"
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

save_filename="scatter_versicolor_sepal_petal_widths.png"
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

save_filename="scatter_virginca_sepal_petal_widths.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()



#########################################
# HISTOGRAM PLOTS  
#########################################

#ALL CLASSES - SEPAL WIDTH plot
plt.hist([setosa_sepalWidth_data,versicolor_sepalWidth_data,virginica_sepalWidth_data])
plt.title('Frequency of each Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Sepal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="histogram_frequency_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - SEPAL LENGTH plot
plt.hist([setosa_sepalLength_data.flatten(),versicolor_sepalLength_data.flatten(),virginica_sepalLength_data.flatten()])
plt.title('Frequency of each Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Sepal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="histogram_frequency_sepal_width.png"
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

save_filename="histogram_frequency_petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#COMBINED CLASSES - PETAL LENGTH plot
plt.hist([setosa_PetalLength_data,versicolor_PetalLength_data,virginica_PetalLength_data])
plt.title('Frequency of each Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Petal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Setosa', 'Versicolor','Virginica'], fontsize = legend_fs)

save_filename="histogram_frequency_petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################

######################################
# HISTOGRAM - SETOSA CLASS plots 
######################################

#SETOSA CLASS - SEPAL WIDTH plot
plt.hist([setosa_sepalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Sepal Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="histogram_frequency_setosa_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - SEPAL LENGTH plot
plt.hist([setosa_sepalLength_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Sepal Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="histogram_frequency_setosa_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - PETAL WIDTH plot
plt.hist([setosa_PetalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Setosa Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Petal Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)

save_filename="histogram_frequency_setosa_Petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#SETOSA CLASS - PETAL LENGTH plot
plt.hist([setosa_PetalLength_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/
plt.title('Frequency of each Setosa Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Setosa Petal Width', fontsize=fs)
plt.legend(title='Class of Setosa iris')
plt.legend(['Setosa'], fontsize = legend_fs)
#plt.width = 1
#plt.tight_layout()
#plt.figsize=(2,5) # ref https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html

save_filename="histogram_frequency_setosa_Petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################




######################################
# HISTOGRAM - VERISICOLOR CLASS plots 
######################################

#VERISICOLOR CLASS - SEPAL WIDTH plot
plt.hist([versicolor_sepalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each versicolor Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Sepal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)

save_filename="histogram_frequency_versicolor_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VERISICOLOR CLASS - SEPAL LENGTH plot
plt.hist([versicolor_sepalLength_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Versicolor Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Sepal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)

save_filename="histogram_frequency_versicolor_sepal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VERISICOLOR CLASS - PETAL WIDTH plot
plt.hist([versicolor_PetalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Versicolor Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Petal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)

save_filename="histogram_frequency_versicolor_Petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VERISICOLOR CLASS - PETAL LENGTH plot
plt.hist([versicolor_PetalLength_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Versicolor Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Versicolor Petal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Versicolor'], fontsize = legend_fs)

save_filename="histogram_frequency_versicolor_Petal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################



######################################
# HISTOGRAM - VIRGINICA CLASS plots 
######################################

#VIRGINICA CLASS - SEPAL WIDTH plot
plt.hist([virginica_sepalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Sepal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Sepal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)

save_filename="histogram_frequency_virginica_sepal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VIRGINICA CLASS - SEPAL LENGTH plot
plt.hist([virginica_sepalLength_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Sepal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Sepal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)

save_filename="histogram_frequency_virginica_sepal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VIRGINICA CLASS - PETAL WIDTH plot
plt.hist([virginica_PetalWidth_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Petal width', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Petal Width', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)

save_filename="histogram_frequency_virginica_petal_width.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()

#VIRGINICA CLASS - PETAL LENGTH plot
plt.hist([virginica_PetalLength_data], rwidth=0.7) #use rwidth to add space in histogram as per https://www.geeksforgeeks.org/add-space-between-histogram-bars-in-matplotlib/)
plt.title('Frequency of each Virginica Petal length', fontsize=fs)
plt.ylabel('Frequency', fontsize=fs)
plt.xlabel('Virginica Petal Length', fontsize=fs)
plt.legend(title='Class of iris')
plt.legend(['Virginica'], fontsize = legend_fs)

save_filename="histogram_frequency_virginica_petal_length.png"
if os.path.isfile(save_filename): os.remove(save_filename) 
plt.savefig(save_filename, format="png")
if display_plots_to_screen: plt.show()
plt.close()
###################################################################################################


#3.3 
#Outputs a scatter plot of each pair of variables

#3.4
#Performs any other analysis you think is appropriate

