# -*- coding: utf-8 -*-
"""Intro_to_DS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t4oALcVjQE76XLZ_WuAxetl0t9LiEYXA

**Printing Hello World**
"""

print("Hello World")

Print("Hello World")

"""Python is case-sensitive"""

PRINT("Latha")

print(Latha)

"""inverted comma is missing"""

print('Latha')

print(10)

print(10.5)

type('Latha')

type(10)

type(10.5)

"""**Statistics **

1.   Numpy->Numerical Python
2.   Pandas->Dataset
3.   Matplotlib-> Data Visualization
4.   Seaborn-> Data Visualization
"""

### import libraries and packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### Load the dataset

df=pd.read_csv("/content/CardioGoodFitness-1.csv")

df.head()

df.tail()

df.head(10)

df.sample()

df.sample(10)

df.shape

df.info()

df.describe()

IQR=33-24
IQR

Q1=24
ab=Q1-1.5*IQR
ab

Q3=33
cd=Q3+1.5*IQR
cd

df.describe(include="all")

sns.boxplot(x="Age",data=df,palette="Set2")

"""There are outliers in all the columns-age,income,fitness,education,miles,usage

"""

sns.countplot(x="Product",data=df,palette="Paired")

df["Product"].value_counts()

df.hist(figsize=(10,10),color="black")
plt.show()

sns.distplot(df["Age"])

sns.countplot(x="Product",hue="Gender",data=df)

pd.crosstab(df["Product"],df["Gender"])

sns.countplot(x="Product",hue="MaritalStatus",data=df)

sns.boxplot(x="Product",y="Age",data=df)
plt.show()

sns.boxplot(x="Product",y="Income",data=df)
plt.show()

sns.boxplot(x="Product",y="Fitness",data=df)
plt.show()

sns.boxplot(x="Usage",y="Fitness",data=df)
plt.show()

sns.boxplot(x="Fitness",y="Age",data=df)
plt.show()

sns.boxplot(x="Usage",y="Age",data=df)
plt.show()

corr=df.corr()
corr

sns.heatmap(corr,annot=True)

sns.relplot(x="Age",y="Income",data=df)

sns.relplot(x="Age",y="Income",hue="Gender",data=df)

sns.catplot(x="Product",y="Age",data=df)

sns.catplot(x="Product",y="Age",hue="Gender",data=df)

sns.catplot(x="Product",y="Age",data=df,kind="violin")

sns.pairplot(df)
plt.show()

### Univariate Analysis -> single column

##### Categorical -> Countplot(sns)
##### Numerical -> Distplot(Distribution-skewness),Boxplot(outliers,five number summary),histogram ->skewness,max or min range

### Bivariate Analysis -> Two columns
##### Two categorical -> Countplot(x,hue),One categ and one numerical->boxplot, two numerical-> scatterplot,relplot,pairplot

### Multivariate-> Multiple columns
##### Two numerical and one categorical(x,y,hue),Three numerical ->relplot