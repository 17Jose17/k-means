# Voronoi-Based K-means Implementation

This directory contains the implementation of the k-means algorithm using Voronoi diagrams as described in the paper **"Initialization for K-means clustering using Voronoi diagram"**.

## Overview

The implementation leverages Voronoi tessellations to improve the initialization step of the k-means algorithm, aiming to achieve better clustering performance and faster convergence compared to traditional methods such as random initialization or k-means++.

### Key Features:
- Utilizes Voronoi diagrams to determine initial cluster centroids.
- Designed for clustering datasets with numerical features.
- Improves clustering quality by minimizing the sensitivity to poor initializations.

## Paper Reference

This implementation is based on the paper:  
**"Initialization for K-means clustering using Voronoi diagram"**, by [Damodar Reddy and Prasanta K. Jana]. Published in [Procedia Technology], [2012].  
Link: [https://doi.org/10.1016/j.protcy.2012.05.116](https://doi.org/10.1016/j.protcy.2012.05.116)  

The article is licensed under the **CC BY-NC-ND 3.0** license. This implementation is an independent work developed from scratch and adheres to the conditions of the license.
