---
chunk_id: "book-ca4fca8dd8-chunk-1176"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1176
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.7
Nonparametric Models
707
the ith dimension; thus half the examples will be in the left branch of the tree and half in the
right. We then recursively make a tree for the left and right sets of examples, stopping when
there are fewer than two examples left. To choose a dimension to split on at each node of the
tree, one can simply select dimension i mod n at level i of the tree. (Note that we may need
to split on any given dimension several times as we proceed down the tree.) Another strategy
is to split on the dimension that has the widest spread of values.
Exact lookup from a k-d tree is just like lookup from a binary tree (with the slight com-
plication that you need to pay attention to which dimension you are testing at each node). But
nearest-neighbor lookup is more complicated. As we go down the branches, splitting the ex-
amples in half, in some cases we can ignore half of the examples. But not always. Sometimes
the point we are querying for falls very close to the dividing boundary. The query point itself
might be on the left hand side of the boundary, but one or more of the k nearest neighbors
might actually be on the right-hand side.
We have to test for this possibility by computing the distance of the query point to the
dividing boundary, and then searching both sides if we can’t ﬁnd k examples on the left that
are closer than this distance. Because of this problem, k-d trees are appropriate only when
there are many more examples than dimensions, preferably at least 2n examples. Thus, k-d
trees are a good choice for up to about 10 dimensions when there are thousands of examples
or up to 20 dimensions with millions of examples.
19.7.3 Locality-sensitive hashing
Hash tables have the potential to provide even faster lookup than binary trees. But how can
we ﬁnd nearest neighbors using a hash table, when hash codes rely on an exact match? Hash
codes randomly distribute values among the bins, but we want to have near points grouped
together in the same bin; we want a locality-sensitive hash (LSH).
Locality-sensitive
hash
We can’t use hashes to solve NN(k,xq) exactly, but with a clever use of randomized
algorithms, we can ﬁnd an approximate solution. First we deﬁne the approximate near-
neighbors problem: given a data set of example points and a query point xq, ﬁnd, with high
Approximate
near-neighbors
probability, an example point (or points) that is near xq. To be more precise, we require that
if there is a point xj that is within a radius r of xq, then with high probability the algorithm
will ﬁnd a point xj′ that is within distance cr of xq. If there is no point within radius r
then the algorithm is allowed to report failure. The values of c and “high probability” are
hyperparameters of the algorithm.
To solve approximate near neighbors, we will need a hash function g(x) that has the
property that, for any two points xj and xj′, the probability that they have the same hash code
is small if their distance is more than cr, and is high if their distance is less than r. For
simplicity we will treat each point as a bit string. (Any features that are not Boolean can be
encoded into a set of Boolean features.)
We rely on the intuition that if two points are close together in an n-dimensional space,
then they will necessarily be close when projected down onto a one-dimensional space (a
line). In fact, we can discretize the line into bins—hash buckets—so that, with high prob-
ability, near points project down to the same bin. Points that are far away from each other
will tend to project down into different bins, but there will always be a few projections that
coincidentally project far-apart points into the same bin. Thus, the bin for point xq contains
many (but not all) points that are near xq, and it might contain some points that are far away.
