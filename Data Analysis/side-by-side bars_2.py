from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
school_a_x = [0.8, 2.8, 4.8, 6.8, 8.8]
school_b_x = [1.6, 3.6, 5.6, 7.6, 9.6]
# Make your chart here
plt.figure(num=None, figsize=(10, 8))
ax = plt.subplot()

n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(middle_school_a)  # Number of sets of bars
w = 0.8 # Width of each bar
school1_x = [t*element + w*n for element
             in range(d)]
plt.bar(school1_x, middle_school_a)

n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = len(middle_school_a)  # Number of sets of bars
w = 0.8 # Width of each bar
school2_x = [t*element + w*n for element
             in range(d)]
plt.bar(school2_x, middle_school_b)

middle_x = []
for i in range(len(middle_school_a)):
    middle_x.append((school1_x[i] + school2_x[i])/2) # the values in the middle of school_a_x and school_b_x

ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

plt.legend(["Middle School A", "Middle School B"])

plt.title("Test Averages on Different Units")
plt.xlabel("Unit")
plt.ylabel("Test Average")

plt.show()

plt.savefig("my_side_by_side.png")