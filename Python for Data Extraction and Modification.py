import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#CREATING MANUAL TABLE
row_values = np.array([
[849, 'Asphalt', True, 600],
[850, 'Phoenix', True, 600],
[851, 'Caltex', False, 779]
])
column_names = ['Number','Engine','Shiny','Strength']
table1 = pd.DataFrame(data = row_values, columns column_names)

#READ CSV FILE
dataframe = pd.read_csv('dataframe.csv')
#SAVE CSV FILE
dataframe.to_csv('modified_dataframe.csv')

#MERGE CSV FILES
import os
files = [file for file in os.listdir('C:\\Users\\krox\\Documents\\Python Scripts\\SalesAnalysis\\Sales_Data\\')]
allmonthsdata = pd.DataFrame()
for file in files:
    df = pd.read_csv('C:\\Users\\krox\\Documents\\Python Scripts\\SalesAnalysis\\Sales_Data\\'+file)
    allmonthsdata = pd.concat([allmonthsdata, df])


#CHECK COLUMNS
df.shape()
df.dtype()
df.info()

#SIMPLE NEW COLUMN
dataframe['Count'] = 1

#NEW COLUMN (CALCULATED)
dataframe['new_column1'] =  dataframe['Def'] + dataframe['Atk']
dataframe['new_column2'] = dataframe.iloc[:,4:10].sum(axis=1)

#NEW COLUMN (CONDITIONAL)
def Strength_modifier(HP):
    if HP >= 100:
        return "Strong"
    elif HP <= 50:
        return "Weak"
    else:
        return "Average"

dataframe['Strength_column'] = dataframe['HP'].apply(Strength_modifier)


#DELETE COLUMN
dataframe = dataframe.drop(columns = 'new_column2')
or
dataframe.drop(columns = 'new_column2', inplace=True)
del dataframe['new_column2']

#REARRANGED COLUMNS
dataframe_columns = list(dataframe.columns)
dataframe = dataframe[dataframe_columns[0:4] + [dataframe_columns[-1]] + dataframe_columns[5:12]]
dataframe.reset_index(drop=True, inplace=True)

parents_theme_distinctss.columns = ['theme', 'count']

#FILTERING
selected_dataframe = dataframe.loc[(dataframe['Speed'] >= 100) & (dataframe['Type 1'] == 'Fire')].sort_values(['Speed', HP], ascending = [1,0])

dataframe.loc[newpokemon['Speed'] >= 100, ['Name', 'Generation']] = ['Fast', 100]

#SELECT DATA THAT CONTAINS
dataframe2 = dataframe.loc[dataframe['Strength'].str.strip().str.contains('Average|Strong', regex = True, case = False)]
dataframe3 = dataframe.loc[dataframe['Name'].str.strip().str.contains('^pi[a-z]*', regex = True, case = False)]  #walang ^ if meron sa middle

#SELECTED TABLE - GROUPBY (STATISTICS)
dataframe.groupby(['Type 1', 'Type 2']).count()['count']
hello = df_parent_name_licensed.groupby(['year'])['set_num'].count().reset_index(name='count')
dataframe.groupby('Type 1').sum().reset_index()
dataframe['Attack'].sum()
dataframe.groupby(['Type 1']).mean().sort_values('Defense', ascending = False)
dataframe['car_type'].value_contains()
alldata.groupby('Month')['Sales'].sum().sort_values(ascending=0)
grouped_counts = tempalldata['Grouped'].value_counts().sort_values(ascending=False)

grouped_data = df_parent_name_licensed.groupby(['year', 'parent_theme'])['set_num'].count().reset_index(name='count')
grouped_data.sort_values(['year', 'count'], ascending=[1, 0])
max_counts = grouped_data.groupby('year')['count'].idxmax()
result = grouped_data.loc[max_counts, ['year', 'parent_theme', 'count']]
print(result)



#COUNT FREQUENCY
alldata['Hour'].value_counts().sort_index()

#then put in a list
hours = [hour for hour, df in alldata.groupby('Hour')]

#then put in a line plot
hours = [hour for hour, df in alldata.groupby('Hour')]
plt.plot(hours, alldata.groupby(['Hour']).count())


#REPLACING VALUE
'Flamer' = dataframe.loc[dataframe['Type 1'] == 'Fire', 'Type 1']


#DELETING ROWS
dataframe = dataframe.drop(0)


#NEW ROWS
row_a = [849, 'new row', True, 600]
row_b = [850, 'new row', True, 600]
new_rows = [row_a, row_b]
for rows in new_rows:
    dataframe.loc[len(dataframe)] = rows
    
#checking null values
df.isnull().sum()
#removing null values
df = df.dropna(how = 'any')

#Convert x column to numpy array
X = df.loc[:, ['x']].values
y = df.loc[:, 'y'].values

#extracting from another column
alldata['Month'] = alldata['Order Date'].str[0:2]

#extracting from another column via comma
def get_city(x):
    return x.split(',')[1]
alldata['City'] = alldata['Purchase Address'].apply(lambda x: get_city(x))

#changing data type
alldata['Month'] = alldata['Month'].astype('int32')

monthxsales = alldata.groupby('Month')['Sales'].sum().sort_values(ascending=False).reset_index()
monthxsales.columns = ['Month', 'Sales']

#comma separator on numbers
monthxsales['Sales'] = monthxsales['Sales'].apply(lambda x: "{:,.2f}".format(x))

#Convert to date/hour/minute
alldata['Order Date'] = pd.to_datetime(alldata['Order Date'])
alldata['Hour'] = alldata['Order Date'].dt.hour
alldata['Minute'] = alldata['Order Date'].dt.minute


#get duplicate cells only
tempalldata = alldata[alldata['Order ID'].duplicated(keep=False)].copy()

#Merge cells
tempalldata['Grouped'] = tempalldata.groupby('Order ID')['Product'].transform(lambda x: ', '.join(x))

#delete duplicate and keep copy
tempalldata = alldata[alldata['Order ID'].duplicated(keep=False)].copy()

#2 plots in one graph
productxqty = alldata.groupby('Product')['Quantity Ordered'].sum().reset_index().sort_values(by='Quantity Ordered', ascending=False)
prices = alldata.groupby('Product')['Price Each'].mean()

fig, ax1 = plt.subplots()

ax1.bar(productxqty['Product'], productxqty['Quantity Ordered'], color='g')
ax1.set_xticklabels(productxqty['Product'], rotation=90)
ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='skyblue')

ax2 = ax1.twinx()

ax2.plot(productxqty['Product'], prices, color='b', marker='.')
ax2.set_ylabel('Price ($)', color='red')

plt.show()

#MERGING CSV via column:
csv1_csv2_column = csv1.merge(csv2, left_on = 'csv1_column', right_on = 'csv2_column')

#RENAME A COLUMN
df = df.rename(columns={'old_name': 'new_name'})
need may equals

#DISTINCT
parents_theme_distinct = df_parent_name_licensed['parent_theme'].unique()
#same lang
total_parents_theme = len(df_parent_name_licensed['parent_theme'])
parents_theme_distinct = df_parent_name_licensed['parent_theme'].count()

parents_theme_distinct_count = df_parent_name_licensed['parent_theme'].value_counts()
parents_theme_distinct_count = parents_theme_distinct_count.reset_index()
parents_theme_distinct_count.columns = ['theme', 'count']
parents_theme_distinct_count['percentage'] = (parents_theme_distinct_count['count'] / parents_theme_distinct) * 100
print(parents_theme_distinct_count)

#LOOKUP
month_map = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
lrr['Month'] = lrr['Month Mark'].map(month_map)

#DISPLAY ALL
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#PIVOT
lrr2023_disposition_pivot = lrr2023_grouped.pivot_table(index=['DeviceName', 'Generic'], columns='Disposition', values='Count', fill_value=0)
lrr2023_disposition_pivot['Grand Total'] = lrr2023_disposition_pivot.sum(axis=1)
lrr2023_disposition_pivot = lrr2023_disposition_pivot.sort_values(by='Grand Total', ascending=0)

#EXPLODE CELLS
lrr2023_50276 = lrr2023[lrr2023['Generic'] == '50276'].groupby(['Generic', 'Remarks']).count()['Count'].reset_index()
lrr2023_50276_expanded = lrr2023_50276.assign(Remarks=lrr2023_50276['Remarks'].str.split(', ')).explode('Remarks')
lrr2023_50276_final = lrr2023_50276_expanded.groupby(['Generic', 'Remarks']).sum().reset_index().sort_values(by='Count', ascending=False)

#TO DATAFRAME
top50276LRR = pd.DataFrame(top50276LRR)


    

    






















