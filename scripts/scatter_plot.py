"""Scatter plot script
"""

# author: Durgesh Samariya
# github: themlphdstudent
# Licence: BSD 3-Clause

#import libraries
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('../data/iris.csv')

plt.plot(iris['PetalLengthCm'], iris['PetalWidthCm'], linestyle='none', marker='+', color='b')
plt.title("Petal Length vs. Petal Width")
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.savefig('../figures/Scatter_Plot.png', dpi=300)
plt.show()