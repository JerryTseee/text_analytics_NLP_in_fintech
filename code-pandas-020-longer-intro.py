import pandas as pd
import numpy as np

df = pd.read_csv('data-CRSP-extract.csv')
df.dtypes

# Selecting column(s).
print(df['TICKER'])        # Select one column, resulting in a Pandas Series.
print(df.TICKER)           # Same as df['TICKER'], returns a Series.
print(df[['TICKER']])      # Returns DataFrame. Inner brackets are a list.
print(df[['TICKER', 'PRC']])           # DataFrame with two columns.

# Convert date to a different data type, i.e. datetime.
df['date'] = pd.to_datetime(df['date'])

# Now you can do arithmetics with the date, e.g. add one day. This is
# not possible if the data type is `object` (e.g. a string) as it was
# before.
df['date'] + np.timedelta64(1, 'D')

# Basic information about the DataFrame.
print(type(df))
print(df.columns)                    # Take a look at the column names.
print(list(df))                      # Column names, similar to `df.columns`.
print(df.shape)                      # Dimensions. (rows, columns)
print(len(df.index))                 # Number of rows, same as `len(df)`.
print(len(df.columns))               # Number of columns.
print(df.describe())                 # Compute some summary statistics.

# Slicing, i.e. selecting rows.
print(df.head())                       # First five rows by default.
print(df.head(3))                      # First three rows.
print(df[:3])                          # First three rows.
print(df.iloc[:3])                     # First three rows.

print(df.tail())                       # Last five rows by default.
print(df.tail(3))                      # Last three rows. 
print(df[-3:])                         # Last three rows. 
print(df.iloc[-3:])                    # Last three rows. 

# Query the data, i.e. we select rows that satisfy certain conditions.
print(df[df.TICKER == 'FB'])                    # Extract Facebook.
print(df.query("TICKER == 'FB'"))               # Extract Facebook.
print(df[(df.TICKER == 'FB') & (df.PRC > 120)]) # Facebook with price>120.
print(df.query("TICKER == 'FB' & PRC > 120"))   # Facebook with price>120.
print(df[(df.TICKER == 'FB') | (df.PRC < 120)]) # Facebook or price<120 (or both).
print(df.query("TICKER == 'FB' | PRC < 120")) # Facebook or price<120 (or both).
print(df[df.TICKER.isin(['AAPL', 'FB'])])     # Apple and Facebook.
print(df.TICKER.unique())                     # All tickers.
print(df[['TICKER', 'SHROUT']].drop_duplicates()) # Two columns w/ unique entries.

# Modify the data. The code below creates a new DataFrame that is
# changed according to which DataFrame method is called,
# e.g. `rename()`, `drop()`, or `sort_values()`. By default, however,
# these methods do not change `df` itsefl. Instead, if you would like
# to modify `df` directly, you can use the `inplace=True` parameter.
df.rename(columns={'VOL': 'Volume', 'PRC': 'Price'}) # Two columns renamed.
df.drop('TICKER', axis=1)       # New DataFrame without this column.
df.sort_values(by='PRC')        # Sort increasing by PRC.
df.sort_values(by='PRC', ascending=False) # Sort decreasing by PRC.
df.sort_values(by=['SHROUT', 'PRC'], ascending=[False, True])

# The `assign()` method creates a new DataFrame containing the
# changes. For example, we create a new column. The existing `df`
# DataFrame is not modified. `assign()` can be useful if we would like
# to create a new column that subsequently should be used for grouping
# the data (see the `groupby()` example below).
df.assign(HIGH_PRC = (df.PRC > 120))    # New column created.
df.assign(abc = df.PRC + 8 * df.SHROUT) # New column.
# `assign` does not have the `inplace=True` parameter. If you would
# like to modify `df`, you could assign the values to the new column
# directly, for example:
# df['abc'] = df.PRC + 8 * df.SHROUT

# Apply a function to each column of the DataFrame. (If you would like
# to apply a function to each row of a DataFrame, use the `axis=1`
# parameter.) As the functions below expect numeric types, we only
# apply them to the price (PRC) and stock return (RET) columns for
# illustration.
# 
# In the first example, we use the `amax()` function (called as
# `np.amax()`) from NumPy, as it is faster than the built-in `max()`
# function of Python. Note that you will often see `np.max()` in code
# of other people, this is simply an alias for `np.amax()` and behaves
# exactly the same. Note that below we pass for example `np.amax` and
# not `np.amax()` to `apply()` because we want to pass the function
# itself to `apply()`, i.e. we do not want invoke the function
# directly (the function would be invoked later by `apply()`).
df[['PRC', 'RET']].apply(np.amax) # Maximum of each column.
df[['PRC', 'RET']].apply(lambda x: x.max() - x.min()) # Range.
df[['PRC', 'RET']].apply(lambda x: x + 3) # Add three to each column.

# Aggregating (summarizing) the data. Here we use the `max()` and
# `min()` methods of the Pandas Series.
df.PRC.max() # Maximum price.
df.PRC.min() # Minimum price.

# Aggregating using the `agg()` method. The difference to `apply()` is
# that `agg()` is often used to apply multiple aggregation functions
# at once. Below we use the string representations of the aggregating
# functions, e.g. `'max'` or `'min'`, which refer to the built-in
# Pandas methods.
df.agg('max')                   # `np.max()` applied to all columns.
df.agg(['max', 'min'])          # Max and min applied to all columns.
df.agg(                         # Different aggregations per column.
    {'RET': ['max', 'min'],
     'VOL': ['min', 'mean', 'sum']})

# Group by ticker and calculate the maximum and minimum stock returns
# for each group.
df.\
    groupby('TICKER').\
    agg({'RET': ['max', 'min']})
# Compute average stock return and stock price for each stock and
# month. Using the `reset_index()` at the end is optional, it puts the
# `TICKER` and `date` into a separate column instead of using them as
# the index (i.e. the row names).
df.\
    groupby(['TICKER', pd.Grouper(key='date', freq='ME')])\
    [['RET', 'PRC']].\
    agg('mean').\
    reset_index()

# Count how many observations have a high price (i.e. PRC>120).
df.\
    assign(HIGH_PRC = (df.PRC > 120)).\
    groupby('HIGH_PRC').\
    agg({'HIGH_PRC': 'count'}).\
    rename(columns={'HIGH_PRC': 'Count'})

# Total trading volume for each ticker, assigned to a new
# column. `transform()` is similar to `agg()` in that it boils down
# the input to one single number. However, unlike `agg()`,
# `transform()` will repeat this number to fill the column.
df['TVOL'] = \
    df['VOL'].\
    groupby(df['TICKER']).\
    transform('sum')

# Removing columns.
del df['TVOL']                  # Delete column.
df.head()                       # Column is gone.
# df.drop('TVOL', axis=1, inplace=True) # Alternative way to delete column.
# df.drop(df.columns[[0, 1, 3]], axis=1, inplace=True) # Delete by column number.
