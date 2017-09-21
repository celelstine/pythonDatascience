import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import os
import seaborn as sns

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

# Set up the matplotlib figure: 3 x 1 axis
f, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True)
i=0
for edu, d in salary.groupby(['education']):
  print(edu , '-', d.salary)
  sns.distplot(d.salary[d.management == "Y"], color="b", bins=10, label="Manager",ax=axes[i])
  sns.distplot(d.salary[d.management == "N"], color="r", bins=10, label="Employee",ax=axes[i])
  axes[i].set_title(edu)
  axes[i].set_ylabel('Density')
  i += 1
plt.legend()
plt.show()
