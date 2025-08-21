import matplotlib.pyplot as plt
import numpy as np

hours = np.array([8, 7, 4, 2, 3])
mylabels = ["Sleeping", "School", "Hobbies", "Exercise", "Other"]
mycolors = ['grey', 'blue', 'hotpink', 'green', 'cyan']
myexplode = [0.1, 0.1, 0.2, 0.3, 0.2]

plt.figure(figsize=(8,5))
#Plotting Pie Chart
plt.pie(hours, labels = mylabels, autopct='%1.0f%%', colors = mycolors, explode = myexplode)       

#Use Legend to add Title
plt.legend(title = 'Daily Activities')         
#Save Plot
plt.savefig("pie_chart.png")     
plt.show() 