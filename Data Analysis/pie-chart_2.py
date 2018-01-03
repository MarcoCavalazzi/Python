from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

#plot here
plt.figure(figsize=(10,8))
plt.pie(num_hardest_reported, labels=unit_topics, autopct='%d%%')
plt.axis("equal") # flattens out the pie

plt.title("Hardest Topics")

plt.show()
plt.savefig("my_pie_chart.png")