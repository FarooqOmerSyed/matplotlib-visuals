# import pandas
import pandas as pd

# initiate the data into data variable with pandas method read_csv()
data = pd.read_csv('sample_orders.csv')
# print the data
print(data)
# Initally maybe the Date in data may come as string, change to correct date format
data['Date'] = pd.to_datetime(data['Date'])
# this time it correctly displays the date in data
print(data)

# get the sum of the day
sum_by_day = data.groupby('Date')['Order Value'].sum()
print(sum_by_day)

# electronics data-only filter
electronics_data = data[data['Order Category'] == 'Electronics']
print(electronics_data)

# electronics sum by day
electronics_daily = electronics_data.groupby('Date')['Order Value'].sum()
print(electronics_daily)

# pet data-only filter
pet_data = data[data['Order Category'] == 'Pet Supplies']
print(pet_data)

# pets data sum by day
pets_daily = pet_data.groupby('Date')['Order Value'].sum()
print(pets_daily)

# clothing data-only filter
clothing_data = data[data['Order Category'] == 'Clothing']
print(clothing_data)

# clothing data sum by day
clothing_daily = clothing_data.groupby('Date')['Order Value'].sum()
print(clothing_daily)

# sum_by_category
sum_by_category = data.groupby('Order Category')['Order Value'].sum()
print(sum_by_category)

# average discounts per day
avg_discount = data.groupby('Date')['Discount %'].mean()
print(avg_discount)
