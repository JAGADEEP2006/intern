import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("titanic.csv")  
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop('Cabin', axis=1, inplace=True)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
# Custom function to standardize the data (replace StandardScaler)
def standardize(data):
    return (data - data.mean()) / data.std()
# Scaling the Age and Fare columns – makes the models happier
df['Age'] = standardize(df['Age'])
df['Fare'] = standardize(df['Fare'])
# Outliers can be weird – let's see them using a boxplot
sns.boxplot(x=df['Age'])
plt.title("Age Boxplot – Let's Spot Those Outliers")
plt.show()
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['Age'] >= Q1 - 1.5 * IQR) & (df['Age'] <= Q3 + 1.5 * IQR)]
# Final check – is our data now clean and shiny?
print(df.head())
print("Final shape after cleaning:", df.shape)
