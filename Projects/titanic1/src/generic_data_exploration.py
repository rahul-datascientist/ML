"""
@author: Saurabh  Wasule
@Purpose - Re-usable code in Python 3 for general data exploration and pre-processing in modeling process
"""

## Importing required libraries
import pandas as pd ## For DataFrame operation
import numpy as np ## Numerical python for matrix operations
import pandas_profiling ## For easy profiling of pandas DataFrame
import missingno as msno ## Missing value co-occurance analysis

####### Data Exploration ############

def print_dim(df):
    '''
    Function to print the dimensions of a given python dataframe
    Required Input -
        - df = Pandas DataFrame
    Expected Output -
        - Data size
    '''
    print("Data size: Rows-{0} Columns-{1}".format(df.shape[0],df.shape[1]))



def print_dataunique(df):
    '''
    Function to print unique information for each column in a python dataframe
    Required Input - 
        - df = Pandas DataFrame
    Expected Output -
        - Column name
        - Data type of that column
        - Number of unique values in that column
        - 5 unique values from that column
    '''
    counter = 0
    for i in df.columns:
        x = df.loc[:,i].unique()
        print(counter,i,df[i].dtype,len(x),x[0:5])
        counter +=1
        
def do_data_profiling(df, filename):
    '''
    Function to do basic data profiling
    Required Input - 
        - df = Pandas DataFrame
        - filename = Path for output file with a .html extension
    Expected Output -
        - HTML file with data profiling summary
    '''
    profile = pandas_profiling.ProfileReport(df)
    profile.to_file(outputfile = filename)
    print("Data profiling done")

def do_simple_data_profiling(df):
    '''
    Function to do basic data profiling
    Required Input - 
        - df = Pandas DataFrame
    Expected Output -
        -
    '''
    df.describe()
    print("Missing Value")
    print(df.apply(lambda x:sum(x.isnull())))

def missing_value_analysis(df):
    '''
    Function to do basic missing value analysis
    Required Input - 
        - df = Pandas DataFrame
    Expected Output -
        - Chart of Missing value co-occurance
        - Chart of Missing value heatmap
    '''
    msno.matrix(df)
    msno.heatmap(df)
