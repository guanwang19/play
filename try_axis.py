import pandas as pd
import numpy as np
# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
print(df)
# Sum along rows (axis=0)
sum_along_rows = df.sum(axis=0)
print("Sum along rows:\n", sum_along_rows)

# Sum along columns (axis=1)
sum_along_columns = df.sum(axis=1)
print("\nSum along columns:\n", sum_along_columns)

# Mean along rows (axis=0)
mean_along_rows = df.mean(axis=0)
print("\nMean along rows:\n", mean_along_rows)

# Mean along columns (axis=1)
mean_along_columns = df.mean(axis=1)
print("\nMean along columns:\n", mean_along_columns)

df = pd.DataFrame(np.arange(12).reshape(3, 4),
                  columns=['A', 'B', 'C', 'D'])
print(df)
print(df.drop(['B', 'C'], axis=1))
print(df.drop(columns=['B', 'C']))
print(df.drop([0, 1]))
print(df)
# print(df.drop(['B', 'C'])) #"['B', 'C'] not found in axis"