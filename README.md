Server-end Geo-Cluster
================================

*View [the actual webpage of the program](http://131.204.27.140:8001/static/frontend.html).*

Since most existing geo-cluster tools are applied on front-end, I designed a package to analyse the structure of geo-distribution in the server-end. I designed the app to implement Model-based Clustering  [1] (Mclust) for clustering geo-distribution. The check-in information is modeled as a mixture of a series of 2-dimensional gaussian distributions. After you give the maximum number of cluster you want, Mclust iteratively decides whether K, the number of clusters is steady.

[1]: C. Fraley and A. E. Raftery. Model-based clustering, discriminant analysis, and density estimation. Journal of the American Statistical Association, 97(458):611–631, 2002.


Where is available Dataset
-------------------------

There are several good geo-social dataset in [SNAP](http://snap.stanford.edu/data/loc-gowalla.html), used by me.


Other packages you need
------------------------

* R(3.0.0 or above)
* mclust in R
* python (2.7 or above)
* Rpy2 in Python

Usage
------------------
1.  Input a ID number, then you will obtain its Geo-distribution

2.  you give the maximum number of cluster you want, the server end will analyse the structure of the clusters, and give you clusters.

