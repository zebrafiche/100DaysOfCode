import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./602 QueryResults.csv')
# print(data)

# column names: ['DATE', 'TAG', 'POSTS']
data.columns = ['DATE', 'TAG', 'POSTS']
print(data)

print(data.head(n=5))
print(data.tail(n=5))

print(data.shape)

print(data.count('index'))

print(data.count())

print(data.groupby('TAG').sum())

print(data.groupby('TAG').sum()['POSTS'])

print(data.groupby('TAG').sum()['POSTS'].idxmax())

print(data.groupby('TAG').sum()['POSTS'].loc['javascript'])

print(data.groupby('TAG').count())

print(data.groupby('TAG').count()['DATE'])

print(data.groupby('TAG').count()['DATE'].idxmin())

print(data['DATE'][1])

print(type(data['DATE'][1]))

data['DATE'] = pd.to_datetime(data['DATE'])

print(data.head(n=3))

reshaped_df = data.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df)

print(reshaped_df.shape)

print(reshaped_df.head(n=5))

print(reshaped_df.tail(n=5))

print(reshaped_df.columns.values)

print(reshaped_df.count(axis='index'))

print(reshaped_df.fillna(0))

reshaped_df.fillna(0, inplace=True)

plt.plot(reshaped_df['java'])
plt.show()

