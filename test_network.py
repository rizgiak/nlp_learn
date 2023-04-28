import numpy as np
import networkx as nx
from mayavi import mlab

# Create some random data
x, y, z = np.random.normal(0, 1, (3, 10))

# Create a graph with 10 nodes and 15 edges
G = nx.fast_gnp_random_graph(10, 0.3)
pos = nx.spring_layout(G, dim=3)  # Compute node positions using a 3D layout algorithm

# Plot the nodes as points in 3D space
mlab.points3d(x, y, z, scale_factor=0.5)

# Plot the edges as lines connecting the nodes
for u, v in G.edges():
    x1, y1, z1 = pos[u]
    x2, y2, z2 = pos[v]
    mlab.plot3d([x1, x2], [y1, y2], [z1, z2], tube_radius=0.1)

# Add some labels to the plot
for i in range(len(x)):
    mlab.text3d(x[i], y[i], z[i], f"Node {i}", scale=0.5)

mlab.show()  # Display the plot
