import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('E:\MCA\expense.csv')
print(data.head())

plt.figure(figsize=(10, 5))
plt.plot(data['Month'], data['Expense'], marker='o', linestyle='-', color='b', label='Monthly Expense')

plt.xlabel('Month')
plt.ylabel('Expense ($)')
plt.title('Monthly Expenses - Line Chart')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(data['Month'], data['Expense'], color='orange', label='Monthly Expense')

plt.xlabel('Month')
plt.ylabel('Expense ($)')
plt.title('Monthly Expenses - Bar Chart')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()