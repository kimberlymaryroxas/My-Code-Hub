import pandas as pd
import matplotlib.pyplot as plt
import os

files = [file for file in os.listdir('C:\\ALLMONTHS\\')]

alldata = pd.DataFrame()

for file in files:
    df = pd.read_csv('C:\\Users\\krox\\Documents\\Python Scripts\\SalesAnalysis\\Sales_Data\\'+file)
    alldata = pd.concat([alldata, df])

alldata.to_csv('alldata.csv', index=False)



alldata = pd.read_csv('alldata.csv')
alldata = alldata.dropna(how='any')
alldata = alldata[alldata['Order Date'].str[0:2] != 'Or']
alldata.to_csv('alldata_cleaned.csv', index=False)
alldata['Quantity Ordered'] = pd.to_numeric(alldata['Quantity Ordered'], errors='coerce')
alldata['Price Each'] = pd.to_numeric(alldata['Price Each'], errors='coerce')
alldata['Sales'] = alldata['Quantity Ordered'] * alldata['Price Each']
alldata['Month'] = alldata['Order Date'].str[0:2].astype(int)
alldata.info()


monthxsales = alldata.groupby('Month')['Sales'].sum().reset_index()
# monthxsales['Sales'] = monthxsales['Sales'].apply(lambda x: "{:,.2f}".format(x))

plt.bar(monthxsales['Month'], monthxsales['Sales'])
plt.xticks(monthxsales['Month'])
plt.show()



def get_city(x):
    return x.split(',')[1]

alldata['City'] = alldata['Purchase Address'].apply(lambda x: get_city(x))
alldata['City']




def get_city(x):
    return x.split(',')[1]

def get_state(x):
    return x.split(',')[2].split(' ')[1]
    
alldata['City'] = alldata['Purchase Address'].apply(lambda x: get_city(x))
alldata['State'] = alldata['Purchase Address'].apply(lambda x: get_state(x))
alldata['CityState'] = alldata['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})" )

alldata.head()


# cityxsales = alldata.groupby('CityState')['Sales'].sum().reset_index()
cityxsales = alldata.groupby('CityState')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=0)
# cityxsales['Sales'] = cityxsales['Sales'].apply(lambda x: "{:,.2f}".format(x))
cityxsales



plt.bar(cityxsales['CityState'], cityxsales['Sales'])
plt.xticks(cityxsales['CityState'], rotation=90)

plt.show()



alldata['Order Date'] = pd.to_datetime(alldata['Order Date'])
alldata['Hour'] = alldata['Order Date'].dt.hour
alldata['Minute'] = alldata['Order Date'].dt.minute

hours = [hour for hour, df in alldata.groupby('Hour')]

plt.plot(hours, alldata.groupby(['Hour']).count())
plt.xticks(hours)
plt.grid()
plt.show()




tempalldata = alldata[alldata['Order ID'].duplicated(keep=False)]

tempalldata['Grouped'] = tempalldata.groupby('Order ID')['Product'].transform(lambda x: ', '.join(x))
tempalldata = tempalldata[['Order ID', 'Grouped']].drop_duplicates()
tempalldata.head()



from itertools import combinations
from collections import Counter

count = Counter()

for row in tempalldata['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))

# print(count)

for key, value in count.most_common(10):
    print(key, value)
	
	
	
productxqty = alldata.groupby('Product')['Quantity Ordered'].sum().reset_index().sort_values(by='Quantity Ordered', ascending=0)
plt.bar(productxqty['Product'], productxqty['Quantity Ordered'])
plt.xticks(productxqty['Product'], rotation=90)

prices = alldata.groupby('Product')['Price Each'].mean()




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