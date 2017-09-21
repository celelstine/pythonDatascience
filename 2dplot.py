import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import os

#  try to read the dataset from a physical file
try:
  salary = pd.read_csv("/learnDatascience/salary.csv") 
except:
  url = 'https://raw.github.com/duchesnay/pylearn-doc/master/data/salary_table.csv'
  salary = pd.read_csv(url)
  # create a file to store the online dataser
  mytmpdir = os.path.join(os.getcwd(), 'learnDatascience')
  csv_filename = os.path.join(mytmpdir, "salary.csv")
  salary.to_csv(csv_filename, index=False)
df = salary

# plot a 2d graph of salaries
#set the Figure size
plt.figure(figsize=(7,6))

# Define sumbols manually for categories 
symbols_manag = dict(Y='*', N='.')
# define color scheme for categories based on eduction
colors = colors_edu = {'Bachelor':'r', 'Master':'g', 'Ph.D':'blue'} 

# plot a marker for each data value
for values, d in salary.groupby(['education', 'management']):
  # collect the employee's education and management value
  edu, management = values
  plt.scatter(d['experience'], d['salary'], marker=symbols_manag[management],
    color=colors_edu[edu], s=120, label=management+"/"+ edu)

# set axis label
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.legend(loc=4)
plt.savefig('experience_salary.png')
plt.savefig('experience_salary.pdf')
plt.close()