import matplotlib.pyplot as plt
from load import sum_by_category

target = 900
plt.figure(figsize=(10, 6))
sum_by_category.plot(kind='bar')
plt.axhline(y=target, linestyle='dashed', color='red')
plt.legend(loc='upper right')
plt.xlabel('categories')
plt.ylabel('sales')
plt.title('Sales by category')
plt.show()
