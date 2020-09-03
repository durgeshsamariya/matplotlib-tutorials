"""Line plot script
"""

# author: Durgesh Samariya
# github: themlphdstudent
# Licence: BSD 3-Clause

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = np.linspace(0, 20, 1000)
y = np.cos(X)

plt.plot(X,y, color='b', linestyle='--')
plt.xlabel('X')
plt.ylabel('cos(X)')
plt.savefig('../figures/Line_Plot.png', dpi=300)
plt.show()