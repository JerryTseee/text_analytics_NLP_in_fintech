import pandas as pd
import numpy as np

df = pd.read_csv('data-CRSP-extract.csv') # Import from CSV file.
df['date'] = pd.to_datetime(df['date'])   # Convert to date (and time).
df = df[['TICKER', 'date', 'PRC', 'VOL']] # Just need a few columns.


newdf = df.copy()
newdf['MVOL'] = \
    newdf.\
    groupby(['TICKER', pd.Grouper(key='date', freq='ME')])\
    ['VOL'].\
    transform('sum')
print(newdf)

mvol = df[['TICKER', 'date', 'VOL']]
mvol = mvol.groupby(['TICKER', pd.Grouper(key='date', freq='ME')]).sum().reset_index()
mvol.rename(columns={'VOL': 'MVOL'}, inplace=True) # Rename column.

# Take a look at the data. You can see that here we have ONE
# observation per ticker and per month.
mvol.tail()


mvol['mdate'] = mvol.date.dt.to_period('M') # Convert to monthly dates.
del mvol['date']
df['mdate'] = df.date.dt.to_period('M') # Convert to monthly dates.

# Convert year-month to string. Although not strictly necessary, it
# makes some things easier to handle, e.g. querying a DataFrame in the
# subsequent step.
df['mdate'] = df.mdate.astype(str)
mvol['mdate'] = mvol.mdate.astype(str)


df = df.query("TICKER == 'AAPL' & date >= '2014-12-20' & date <= '2015-01-15'")
mvol = mvol[(mvol.TICKER == 'AAPL') & (mvol.mdate >= '2014-11') & (mvol.mdate <= '2015-02')]

# Next we merge both DataFrames together
df_mvol = pd.merge(df, mvol, how='left', on=['TICKER', 'mdate'])


print(df)
mvol[['TICKER', 'mdate', 'MVOL']]
print(df_mvol)

del df_mvol['mdate']

# Here is our final result, with monthly trading volume added to each
print(df_mvol)
