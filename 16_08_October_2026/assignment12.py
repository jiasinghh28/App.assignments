import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('customer_churn.csv')
print("first 5 records of the dataset:\n", df.head())
print("shape of the dataset:", df.shape)
print("columns of the dataset : ", df.columns)
print("data information : ", df.info())
print("Missing values : ")
print(df.isnull().sum())
print("duplicates records : ")
print(df.duplicated().sum())
df = df.drop_duplicates()
numeric_columns = df.select_dtypes(include=np.number).columns
for column in numeric_columns :
    df[column] = df[column].fillna(df[column].mean())
categorical_columns = df.select_dtypes(include='object').columns
for column in categorical_columns :
    df[column] = df[column].fillna(df[column].mode()[0])
print("Missing values after handling : ")
print(df.isnull().sum())
print("summary statics : ",df.describe())
print("average monthly charges : ",np.mean(df['MonthlyCharges']))
print("average monthly Tenure : ",np.mean(df['Tenure']))
print("\ncustomer churn count : ",df['Churn'].value_counts())
churn_percentage = df["Churn"].value_counts(normalize=True) * 100
print("nChurn Percentage: ")
print(churn_percentage)
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()
plt.hist(df["MonthlyCharges"], bins=10)
plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.show()
contract_churn = pd.crosstab(df["Contract"], df["Churn"])
print("\nChurn based on Contract:")
print(contract_churn)
contract_churn.plot(kind="bar")
plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.show()
