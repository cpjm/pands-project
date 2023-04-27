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

df = pd.read_csv('data/iris.data')
print(df.to_string()) 