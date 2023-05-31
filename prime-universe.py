import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sympy import primepi, factorint

# Maximum number to represent
max_num = 5000
point_thickness = 2

# Calculate the number of primes up to and including max_num
num_primes = primepi(max_num)

# Initialize a zeros matrix to store the coordinates
coordinates = np.zeros((max_num + 1, num_primes))

# Populate the coordinates matrix with prime factors
for i in range(2, max_num + 1):
    factors = factorint(i)
    for factor, multiplicity in factors.items():
        # Find the dimension for this factor (minus 1 because our matrix is 0-indexed)
        dimension = primepi(factor) - 1
        coordinates[i, dimension] = multiplicity

# Perform t-SNE to reduce to 2 dimensions
tsne = TSNE(n_components=2)
coordinates_tsne = tsne.fit_transform(coordinates)

# Plot the points
plt.figure(figsize=(17, 13))
plt.scatter(coordinates_tsne[:, 0], coordinates_tsne[:, 1], s=point_thickness)
plt.title('Prime Universe of First ' + str(max_num) + ' Natural Numbers (t-SNE to 2D)')
plt.show()

