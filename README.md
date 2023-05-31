# prime-universe
A novel way of visualizing the structure of prime numbers where every prime number represents a unique "dimension" in this universe

Below is a novel way of visualizing the structure of prime numbers in a way that has never been done before. (If you'd like to check out the Python program, feel free to check it out on GitHub — https://github.com/zoglmannk/prime-universe . Warning, the Big O Notation of this program is non-linear. It is progressively computationally expensive to explore larger numbers of natural numbers. It took 20 minutes to calculate and plot the Prime Universe of the first 75,000 natural numbers in t-SNE to 2D).

# Approach
### 1) The Prime Universe is about the concept of prime factorization.

Every prime number represents a unique "dimension" in this universe. For instance, 2 is the first dimension, 3 is the second, 5 is the third, and so forth. 

A composite number is a point in this multi-dimensional space, with its coordinates determined by the exponents in its prime factorization.

For example, the number 18 = 2^1 * 3^2 would correspond to a point at the coordinates (1, 2, 0, 0, 0, ...). If this isn't clicking, see the additional examples below.

* The number 8 = 2^3 would be represented as the coordinates (3, 0, 0, 0, 0, ...), meaning it is 3 units along the 2-dimension and zero along all other dimensions.
* The number 27 = 3^3 would be represented as (0, 3, 0, 0, 0, ...), meaning it is 3 units along the 3-dimension and zero along all other dimensions.
* The number 100 = 2^2 * 5^2 would be represented as (2, 0, 2, 0, 0, ...), 2 units along the 2-dimension and 2 units along the 5-dimension, and zero along all other dimensions.
* The number 252 = 2^2 * 3^2 * 7 would be represented as (2, 2, 0, 1, 0, ...), 2 units along the 2-dimension, 2 units along the 3-dimension, 1 unit along the 7-dimension, and zero along all other dimensions.
* The number 2310 = 2 * 3 * 5 * 7 * 11 would be represented as (1, 1, 1, 1, 1, 0, ...), 1 unit along each of the first five dimensions (2, 3, 5, 7, and 11) and zero along all other dimensions.

### 2) Use t-distributed Stochastic Neighbor Embedding (t-SNE) to translate the high-dimensional space into two dimensions and plot it as a graph.

### 3) Interpret the graph for structures and patterns.

Interpreting t-SNE images can be tricky due to the algorithm's focus on maintaining local structures, often at the expense of the global structure. Consider the following guidelines.

**Clusters:** Look for clusters of points in the visualization. A cluster of points indicates that those data points are similar in some way, according to the features used to generate the t-SNE plot.

**Distances between clusters:** While the absolute distances between clusters are not to be taken at face value, relative distances can sometimes be meaningful. For example, if one cluster is visually farther away from the others, you might infer that it represents data points that are notably different from the others.

**Do not over-interpret:** One of the most important things to remember is that t-SNE is not a magic solution that will always produce meaningful visualizations. It is a tool that can help to reveal structure in your data, but it is not perfect and it does not replace the need for careful data analysis.

**Noise and outliers:** Points that are not part of any discernable cluster can be interpreted as noise or outliers in the data.

**Parameter Sensitivity:** t-SNE has a key parameter, perplexity, which can significantly affect the output. Perplexity loosely determines how to balance attention between local and global aspects of your data. Changing the perplexity can sometimes reveal different structures in the data, so it can be helpful to create a few plots with different perplexity values to see how stable the clusters are.

Also, note that graphs with different numbers of natural numbers will be oriented slightly differently relative to each other.
