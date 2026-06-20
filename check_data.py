import pandas as pd

df0 = pd.read_csv("shipping_data_0.csv")
df1 = pd.read_csv("shipping_data_1.csv")
df2 = pd.read_csv("shipping_data_2.csv")

print("\n=== FILE 0 ===")
print(df0.head())
print(df0.columns)

print("\n=== FILE 1 ===")
print(df1.head())
print(df1.columns)

print("\n=== FILE 2 ===")
print(df2.head())
print(df2.columns)