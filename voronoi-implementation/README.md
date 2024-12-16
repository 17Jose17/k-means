# Voronoi-Based K-means Implementation

This directory contains the implementation of the k-means algorithm using Voronoi diagrams as described in the paper **"Initialization for K-means clustering using Voronoi diagram"**.

## Overview

The implementation leverages Voronoi tessellations to improve the initialization step of the k-means algorithm, aiming to achieve better clustering performance and faster convergence compared to traditional methods such as random initialization or k-means++.

## Key Features:
- Utilizes Voronoi diagrams to determine initial cluster centroids.
- Designed for clustering datasets with numerical features.
- Improves clustering quality by minimizing the sensitivity to poor initializations.

## Alternative Method

While the original paper describes a specific initialization strategy using Voronoi tessellations, in this implementation, the Voronoi circles **CirS(v)** were obtained using the **Delaunay dual** instead of directly using the Voronoi diagram.

This method is not a modification of the original algorithm but rather an alternative approach aimed at obtaining better cluster initialization by leveraging the relationship between Delaunay triangulations and Voronoi tessellations.

## Paper Reference

This implementation is based on the paper:  
**"Initialization for K-means clustering using Voronoi diagram"**, by [Damodar Reddy and Prasanta K. Jana]. Published in [Procedia Technology], [2012].  
Link: https://www.sciencedirect.com/science/article/pii/S2212017312003404

The article is licensed under the **CC BY-NC-ND 3.0** license. This implementation is an independent work developed from scratch and adheres to the conditions of the license.
