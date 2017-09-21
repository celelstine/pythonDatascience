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

plt.subplot(211)
sns.boxplot(x="education", y="salary", hue="management", data=salary, palette="PRGn")
# plt.close()

plt.subplot(212)
sns.boxplot(x="management", y="salary", hue="education", data=salary, palette="PRGn")
plt.savefig('salaryplotbox.jpg')
plt.show()
