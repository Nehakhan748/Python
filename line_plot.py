import matplotlib.pyplot as plt
import numpy as np

x = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

plt.figure(figsize=(8,5))
# Line plot with custom color & style
plt.plot(x, y, color="green", linestyle="--", marker="o") 

# Labels and title
plt.xlabel("X Values", fontsize=12, color="darkblue")
plt.ylabel("Y Values", fontsize=12, color="darkblue")
plt.title("Simple Line Plot", fontsize=14, color="purple")

plt.grid(c="black", ls=":", lw='2')   

plt.savefig("line_plot.png")     #Save Plot
plt.show()