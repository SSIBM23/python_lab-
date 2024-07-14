import matplotlib.pyplot as plt
marks=[65,50,34,90,26,97,56,67,45,95]
grade=[0,35,70,100]
plt.xticks([0,35,70,100])
plt.hist(marks,grade,facecolor="g")
plt.xlabel("Percentage")
plt.ylabel("No.of Students")
#Pie chart
from matplotlib import pyplot as plt
import numpy as np
cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)
plt.show()
