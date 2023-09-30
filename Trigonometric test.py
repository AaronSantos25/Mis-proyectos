import matplotlib.pyplot as plt
import numpy as np
# Here we are going to choose the x and y values for the graph. It can be combined with sine, cosine and tangent.
x = np.arange(3,10,0.1)
y = x*np.tan(x)
# Let's make the commands combine to create the x and y graph.
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric test')
plt.show()
