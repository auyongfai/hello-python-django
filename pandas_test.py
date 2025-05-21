# pandas_test.py
# Author: Au Yong Fai
# Description: Practice script showing usage of dictionary and pandas DataFrame

import pandas as pd

# ==========================
# Version 1: Basic Dictionary to DataFrame
# ==========================
print("\n--- Version 1: Basic Dictionary to DataFrame ---")
data_v1 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'City': ['New York', 'London', 'Tokyo']
}

df_v1 = pd.DataFrame(data_v1)
print(df_v1)

# ==========================
# Version 2: Accessing Columns and Rows
# ==========================
print("\n--- Version 2: Accessing Columns and Rows ---")
print("Names column:")
print(df_v1['Name'])

print("Second row:")
print(df_v1.iloc[1])  # Bob's row

# ==========================
# Version 3: Adding a New Column
# ==========================
print("\n--- Version 3: Adding a New Column ---")
df_v3 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22]
})

df_v3['Is_Adult'] = df_v3['Age'] >= 18
print(df_v3)

# ==========================
# Version 4: Dictionary of Dictionaries
# ==========================
print("\n--- Version 4: Dictionary of Dictionaries ---")
data_v4 = {
    'Alice': {'Age': 24, 'City': 'New York'},
    'Bob': {'Age': 30, 'City': 'London'},
    'Charlie': {'Age': 22, 'City': 'Tokyo'}
}

df_v4 = pd.DataFrame.from_dict(data_v4, orient='index')
print(df_v4)

# ==========================
# Version 5: Filtering Data
# ==========================
print("\n--- Version 5: Filtering Data ---")
data_v5 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 17]
}

df_v5 = pd.DataFrame(data_v5)

adults = df_v5[df_v5['Age'] >= 21]
print("People aged 21 and above:")
print(adults)