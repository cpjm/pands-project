# This program will process the iris datset.
# it will produce a number of (hopefully!) meaningful plots on the data.
#
# Opening and reading the 'iris.data' csv file.
# My code re-used code from this article:- 
# https://www.w3schools.com/python/pandas/pandas_csv.asp
#
# Author: Ciaran Moran
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#ref https://www.w3schools.com/python/pandas/pandas_csv.asp#gsc.tab=0
df = pd.read_csv('data/iris.data')
print(df.to_string()) 

#ref https://www.w3schools.com/python/pandas/ref_df_describe.asp
print(df.describe())

#Generate the 
#ref https://pandashowto.com/how-to-save-dataframe-as-text-file/
#df.to_string("myfile.txt")
df.describe().to_string("iris_summary.txt")

