#!/usr/bin/python
from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#  create a dataset with pandas
columns = ['name', 'age', 'gender', 'job']

user1 = pd.DataFrame([['alice', 19, "F", "student"],
                      ['john', 26, "M", "student"]],
    columns=columns)
user2 = pd.DataFrame([['eric', 22, "M", "student"],
                      ['paul', 58, "F", "manager"]],
    columns=columns)
user3 = pd.DataFrame(dict(name=['peter', 'julie'],
                          age=[33, 44], gender=['M', 'F'],
                          job=['engineer', 'scientist']))
users = pd.concat([user1, user2, user3])
# print(users)

user4 = pd.DataFrame(dict(name=['alice', 'john', 'eric', 'julie'],
                          height=[165, 180, 175, 171]))
# print(user4)
# Use intersection of keys from both frames like sql inner join 
merge_inter = pd.merge(users, user4, on="name")
# print(merge_inter)

# perform SQL outer join
users = pd.merge(users, user4, on="name", how='outer')
# print(users)
# print(type(users))

# print the first 5 rows
# print(users.head())

# print the last 5 rows
# print(users.tail())

# get a full comparism list of the rows such as mean, count, std
# print(users.describe())

# get specify columns
# print(users.gender) or 
# print(users[['age', 'gender']])
# print(users.ix[0])

# "Unpivots" a DataFrame from wide format to long (stacked) format,
# staked = pd.melt(users, id_vars="name", var_name="property", value_name="value")
# print(staked)

# "pivots"" a DataFrame from long (stacked) format to wide format,
# print(staked.pivot(index='name', columns='property', values='value'))


# df = users.copy()
# print(df.describe(include='all'))
# replace the dataframe with true and false when a datavalue is null
# print(df.isnull())
# drop row that have null values
# print(df1)

import tempfile, os.path
# build a new path from the project directory
# workingDir = os.getcwd()
# mytmpdir = os.path.join(workingDir, 'learnDatascience')
# csv_filename = os.path.join(mytmpdir, "users.csv")
# create dataframe into a file
# users.to_csv(csv_filename, index=False)
# other = pd.read_csv(csv_filename)

# read data from a remote data source
url = 'https://raw.github.com/neurospin/pystatsml/master/data/salary_table.csv'
salary = pd.read_csv(url)
# create a file to store the online dataser
mytmpdir = os.path.join(os.getcwd(), 'learnDatascience')
csv_filename = os.path.join(mytmpdir, "salary.csv")
salary.to_csv(csv_filename, index=False)
print(salary)