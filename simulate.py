import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('initial_data.txt')
coordinates = data[:, :3]
speed = data[:, 3:] 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(coordinates[:,0], coordinates[:,1], coordinates[:,2], c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
