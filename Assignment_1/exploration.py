from csv_reader import read_data
import numpy as np
import matplotlib.pyplot as plt

# read data
df = read_data('ODI-2021.csv')

# histogram of the answer of 'have you taken a course on information retrieval?'
histo = df['Have you taken a course on information retrieval?']

histo.hist(bins=3)
plt.ylabel('Frequency')
plt.xlabel('No, yes, unknown')
plt.title('Prior course information retrieval')

# turn on the line below to show the plot
# plt.show()
