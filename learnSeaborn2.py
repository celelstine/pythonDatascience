import numpy as np
import pandas as pd 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
import seaborn as sns



#  try to read the dataset from a physical file
try:
  # read the dataset and use the first column as the index column
  salary = pd.read_csv("./learnDatascience/Pokemon.csv", index_col=0) 
except:
  print("the file does not exist at --> ./learnDatascience/Pokemon.csv")

df=salary
# plot a scatter plot, setting the axis and the data source, 
# fit_reg is false to hide the defualt seaborn diagonal line
# we set hue to a column to create a colour scheme for category
# sns.lmplot(x='Attack', y='Defense', data=df, fit_reg=False, hue='Stage')
# plt.savefig("seaborn_scatterplot.png")
# set the limit of value to show on the axis
# plt.ylim(0,  None)
# plt.xlim(0, None)

# plot a box plot of every numeric column
# To show only reasonable data, we refine the dataset by droping irrelevant columns
# stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
# sns.boxplot(data=stats_df)
# plt.savefig('seaborn_boxplot.png')

# use seaborn theme and violin plot
# this plot show the growth rate of an attribute
sns.set_style('whitegrid')
# create a smaple colour palette to use
type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]
# Violin plot
# sns.violinplot(x='Type 1', y='Attack', data=df, palette=type_colors)
# plt.savefig('seaborn_violinplot.png')

#Swarmplot is used to visualize each point and also show related point
# sns.swarmplot(x='Type 1', y='Attack', data=df, palette=type_colors) 
# plt.savefig('seaborn_swarmplot.png')

# we can combine swarmplot and violin plot in a diagram
# first we set he size of our plot , (height,width)
# plt.figure(figsize=(12,10))
# # then we plot the violin without the bar
# sns.violinplot(x='Type 1', y='Attack', data=df, palette=type_colors, inner=None)

# # we now plot the swarm plot, we make the spot black to make then visible and we lighten their transparency
# sns.swarmplot(x='Type 1', y='Attack', data=df, color='k', alpha=0.7)
# plt.title('swarm-violin plot for Attack against Type')
# plt.savefig('seaborn and swarm&violinplot.png')

# melt the exisitng dataframe, it is same as dropping columns but now we want to store the hide columns into a single column
# we drop the total column
# plt.figure(figsize=(14,13))
# df_withoutTotal = df.drop(['Total'], axis=1)
# meltd_df = pd.melt(df_withoutTotal,
#                   id_vars=['Name', 'Type 1', 'Type 2'],
#                   var_name='other guys')
# #  wonder why it necessary to melt a dataset, then checkout this swarmplot
# sns.swarmplot(x='other guys',
#               y='value', 
#               data=meltd_df, 
#               hue ='Type 1', 
#               split=True, # draw a horizontal line to seperate related spot
#               palette=type_colors )

# # Adjust the y-axis to begin from 0 instead of -50
# plt.ylim(0, 260)
# # Place legend to the right beside the graph
# plt.legend(bbox_to_anchor=(1, 1), loc=2)
# plt.title('The effect of other quantiy against thier type')
# plt.savefig('seaborn_sweetswarmplot.png')

# Calculate correlations
# stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
# # create a table of correlation of each column agianst the other
# corr = stats_df.corr()
# # plot a Heatmap, which use colors to show relationship
# sns.heatmap(corr)
# plt.title('The effect of other quantiy against thier type')
# plt.savefig('seaborn_heatmapCorrelation.png')

# Distribution Plot (a.k.a. Histogram)
# sns.distplot(df.Attack)
# plt.title('History of Attack')
# plt.savefig('seaborn_histogram.png')

# Count Plot (a.k.a. Bar Plot)
sns.countplot(x='Type 1', data=df, palette=type_colors)
 
# Rotate x-labels
# plt.xticks(rotation=-45)
# plt.title('History of Attack')
# plt.savefig('seaborn_barchat.png')

# Factor Plot: create seperare plot for each value in the col parameter
# g = sns.factorplot(x='Type 1', 
#                    y='Attack', 
#                    data=df, 
#                    hue='Stage',  # Color by stage
#                    col='Stage',  # Separate by stage
#                    kind='swarm') # Swarmplot
 
# # Rotate x-axis labels
# g.set_xticklabels(rotation=-45)
# plt.title('Attack for each Type')
# plt.savefig('seaborn_factorplot.png')

# Density Plot: display the distribution between two variables
# sns.kdeplot(df.Attack, df.Defense)
# plt.title('Distribution density between Attack and Type1')
# plt.savefig('seaborn_kdeplot.png')

# Joint Distribution Plot: combine information from scatter plots and histograms to give you detailed information for bi-variate distributions
sns.jointplot(x='Attack', y='Defense', data=df)
plt.title('bi-variate Distribution density between Attack and Type1')
plt.savefig('seaborn_jointplot.png')
plt.show()