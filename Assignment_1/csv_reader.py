import csv
import pandas

def read_data(file):
    """
    Function which reads in the data set and return a pandas dataframe.

    Input:
    - csv file

    Output:
    - df: pandas dataframe
    """

    df = pandas.read_csv(file)
    return df
