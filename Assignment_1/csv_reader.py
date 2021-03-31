import csv
import pandas

def read_data():
    """
    Function which reads in the data set and return a pandas dataframe.

    Input:
    -

    Output:
    - df: pandas dataframe
    """
    
    df = pandas.read_csv('ODI-2021.csv')
    return df
