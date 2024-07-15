import matplotlib.pyplot as plt
from load import sum_by_day

# target = 900
plt.figure(figsize=(20, 6))
plt.plot(sum_by_day.index, sum_by_day.values, marker='o', linestyle='--')
plt.title('total sales day')
plt.xlabel('day')
plt.ylabel('sales')
plt.grid(True)

# plt.axhline(y=target, linestyle='--', color='red')
plt.show()
