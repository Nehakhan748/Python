import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 4, 5, 8, 10])   # numbers from 0 to 10
y1 = x                    # y = x
y2 = x**2                 # y = x^2

plt.figure(figsize=(8,5))
# Plotting Both Lines
plt.plot(x, y1, label="y = x", color="g", linestyle=":")
plt.plot(x, y2, label="y = x^2", color="hotpink", linestyle="--")

# Labels and title
plt.xlabel("X Values", fontsize=12)
plt.ylabel("Y Values", fontsize=12)
plt.title("Multiple Lines on One Graph", fontsize=14)

# Show legend
plt.legend()
plt.savefig("multiple_lines.png")     #Save Plot
plt.show()