from . import Expense
import collections
import matplotlib.pyplot as plt

Expenses = Expense.Expenses()
Expenses.read_expenses('data/spending_data.csv')
spending_categories = []
for Expense in Expenses.list:
        spending_categories.append(Expense.category)

spending_counter = collections.Counter(spending_categories)

top5 = spending_counter.most_common(5)

result = top5

categories, count = zip(*top5)

fig, ax = plt.subplots()

ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

plt.show()
