from csv_reader import read_data
import numpy as np

# read data
df = read_data()

# print(df['Have you taken a course on information retrieval?'])
# df.hist(column='Have you taken a course on information retrieval?')
print(df.groupby(by='Have you taken a course on information retrieval?'))
# .sum().plot(kind='bar')
