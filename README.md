# Collect Coins in a Tree

This repository provides a Python implementation of the algorithm to find the
minimum number of edges required to traverse in order to collect all coins in a
tree. From a vertex, you can collect all coins within distance two.

The algorithm follows these steps:

1. Build the adjacency list for the tree.
2. Remove all leaf nodes that do not contain coins.
3. Remove leaves again twice, accounting for the ability to collect coins that
   are within a distance of two edges from any visited vertex.
4. Count the remaining edges. Each remaining edge must be traversed twice
   (forward and backward), so the result is `2 * remaining_edges`.

The provided script `collect_coins_in_tree.py` includes an example that matches
the problem statement.
