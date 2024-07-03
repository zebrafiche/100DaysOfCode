import pandas

df = pandas.read_csv('593 salaries-by-college-major.csv')

print(df.head())

print(df.shape)

print(df.columns)

# Index(['Undergraduate Major', 'Starting Median Salary',
#        'Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary',
#        'Mid-Career 90th Percentile Salary', 'Group'],
#       dtype='object')


print(df.isna())

print(df.tail(5))

#       Undergraduate Major  ...  Group
# 46             Psychology  ...   HASS
# 47               Religion  ...   HASS
# 48              Sociology  ...   HASS
# 49                Spanish  ...   HASS
# 50  Source: PayScale Inc.  ...    NaN
#
# [5 rows x 6 columns]

