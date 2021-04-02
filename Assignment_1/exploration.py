from csv_reader import read_data
import numpy as np

# read data
df = read_data('ODI-2021.csv')


histo = df['Have you taken a course on information retrieval?'].hist()
fig = histo.get_figure()
fig.savefig('documents/histtest.pdf')
# df.hist(column='Have you taken a course on information retrieval?')
# print(df.groupby(by='Have you taken a course on information retrieval?'))
# .sum().plot(kind='bar')
