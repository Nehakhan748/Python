import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 1, 5, 7])

plt.figure(figsize=(8,5))
plt.scatter(x, y, color= 'hotpink', marker= '*')         #Plotting Scatter

# Labels and title
plt.xlabel("X-axis", fontsize=12, color="darkblue")
plt.ylabel("Y-axis", fontsize=12, color="darkblue")
plt.title("Scatter Plot of Given Points", color="purple")

plt.savefig("scatter_plot.png")     #Save Plot
plt.show()