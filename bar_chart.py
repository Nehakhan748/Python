import matplotlib.pyplot as plt
import numpy as np

x = np.array(['Ali', 'Sara', 'John', 'Ayesha', 'Tom'])
y = np.array([80, 90, 70, 85, 60])
mycolors = ['black', 'hotpink', 'grey', '#891414', "#5723AA"]    

font1 = {'color':'darkred','size':15}
font2 = {'color':'darkred','size':15}

plt.figure(figsize=(8,5))
plt.bar(x, y, color = mycolors)     #Plotting Bar

plt.xlabel("Student Name", fontdict=font1)   #Labeling x-axis
plt.ylabel("Marks", fontdict=font2)          #Labeling y-axis
plt.title("Students Marks Record", fontdict={'color':'black','size':18})        

# Rotate x-axis labels
plt.xticks(rotation=45)
plt.savefig("bar_chart.png")     #Save Plot
plt.show()