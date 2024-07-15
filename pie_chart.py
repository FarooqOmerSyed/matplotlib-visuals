import matplotlib.pyplot as plt
from load import sum_by_category

plt.figure(figsize=(10, 6))
sum_by_category.plot(kind='pie', subplots=True, autopct='%1.1f%%')
plt.title('sum of sales by category')

plt.show()
