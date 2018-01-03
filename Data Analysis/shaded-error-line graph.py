from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

#your work here
plt.plot(months, revenue)
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)

y_lower = []
for i in revenue:
  y_lower.append(0.9*i)
y_upper = []
for i in revenue:
  y_upper.append(i*1.1)

plt.fill_between(months, y_lower, y_upper, alpha=0.2) # This is the shaded error
  
plt.show()