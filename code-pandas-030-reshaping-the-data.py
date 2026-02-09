import pandas as pd
import numpy as np
df = pd.read_csv('data-CRSP-extract.csv')
df['date'] = pd.to_datetime(df['date']) # ensure converting to datetime


pivot_df = \
    df.\
    pivot(
        index='date',
        columns='TICKER',
        values='RET').\
    reset_index()
print(pivot_df) # recreate a new table, each row is a date, each column is a stock
print(pivot_df.melt(id_vars=['date']))
 

melted_df = df.melt(id_vars=['TICKER', 'date'])
print(melted_df)

melted_df.\
    pivot(
        index=['TICKER', 'date'],
        columns='variable',
        values='value').\
    reset_index()

# For each stock, compute the means of each variable.
melted_df.\
    groupby(['TICKER', 'variable']).\
    mean()

df.groupby('TICKER').mean()
print(df.groupby('TICKER').mean())
