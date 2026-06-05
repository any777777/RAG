---
chunk_id: "book-ca4fca8dd8-chunk-1177"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1177
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 708

708
Chapter 19
Learning from Examples
 0
 1
 2
 3
 4
 5
 6
 7
 8
 0
 2
 4
 6
 8
 10
 12
 14
 0
 1
 2
 3
 4
 5
 6
 7
 8
 0
 2
 4
 6
 8
 10
 12
 14
(a)
(b)
 0
 1
 2
 3
 4
 5
 6
 7
 8
 0
 2
 4
 6
 8
 10
 12
 14
 0
 1
 2
 3
 4
 5
 6
 7
 8
 0
 2
 4
 6
 8
 10
 12
 14
(c)
(d)
Figure 19.20 Nonparametric regression models: (a) connect the dots, (b) 3-nearest neigh-
bors average, (c) 3-nearest-neighbors linear regression, (d) locally weighted regression with
a quadratic kernel of width 10.
The trick of LSH is to create multiple random projections and combine them. A random
projection is just a random subset of the bit-string representation. We choose ℓdifferent
random projections and create ℓhash tables, g1(x),...,gℓ(x). We then enter all the examples
into each hash table. Then when given a query point xq, we fetch the set of points in bin
gi(xq) of each hash table, and union these ℓsets together into a set of candidate points, C.
Then we compute the actual distance to xq for each of the points in C and return the k closest
points. With high probability, each of the points that are near to xq will show up in at least
one of the bins, and although some far-away points will show up as well, we can ignore
those. With large real-world problems, such as ﬁnding the near neighbors in a data set of 13
million Web images using 512 dimensions (Torralba et al., 2008), locality-sensitive hashing
needs to examine only a few thousand images out of 13 million to ﬁnd nearest neighbors—a
thousand-fold speedup over exhaustive or k-d tree approaches.

## Page 709
