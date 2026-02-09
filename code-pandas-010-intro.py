# This script gives a brief introduction on pandas in Python.

import pandas as pd
import numpy as np

# Very simple DataFrame with only one column.
temp1 = pd.DataFrame(
    data=[3, 5, 6, 7], # Data input is a list [3, 5, 6, 7]
    columns=['MyColumnName']) # "MyColumnName" is the title of the column

print(temp1)

# Use `columns=...` to rearrange the order of the columns.
temp2 = pd.DataFrame(
    {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
     'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze']}, 
    columns=['last_name', 'first_name'])

print(temp2)

# The columns of a DataFrame can hold data of different data
# types. Here we are using a dictionary as an input. The keys of the
# dict will become the column names of the DataFrame, while the values
# of the dict will become the column entries of the DataFrame.
df = \
    pd.DataFrame(
        { 'A': 1.,       # Will be repeated to fill the whole column.
          'B': pd.Timestamp('2019-12-20'), # Will be repeated.
          'C': pd.Series(1, index=list(range(5)), dtype='float32'),
          'D': np.array([3] * 5, dtype='int32'),
          'E': ['Jason', 'Molly', 'Tina', 'Jake', 'Jeff'],
          'F': pd.Categorical(['test', 'train', 'test', 'train', 'train'])})

print(df.dtypes)