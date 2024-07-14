import matplotlib.pyplot as plt
country = ['A','B','C','D','E']
gdp=[45000,42000,55000,52000,65000]
plt.bar(country, gdp, color ='red')
plt.title('Country Vs GDP Per Capita')
plt.xlabel('Country')
plt.ylabel('GDP Per Capita')
plt.plot(country, gdp)
plt.show()