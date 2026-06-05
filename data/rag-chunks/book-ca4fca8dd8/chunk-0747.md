---
chunk_id: "book-ca4fca8dd8-chunk-0747"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 747
confidence: "first-pass"
extraction_method: "structured-local"
---

452
Chapter 13
Probabilistic Reasoning
¬
¬
W
X
Y
Z
C3
C1
S
C2
Figure 13.14 Bayes net encoding of the 3-CNF sentence
(W ∨X ∨Y)∧(¬W ∨Y ∨Z)∧(X ∨Y ∨¬Z).
problem is #P-complete (“number-P complete”), this means that Bayes net inference is #P-
hard—that is, strictly harder than NP-complete problems.
There is a close connection between the complexity of Bayes net inference and the com-
plexity of constraint satisfaction problems (CSPs). As we discussed in Chapter 5, the difﬁ-
culty of solving a discrete CSP is related to how “treelike” its constraint graph is. Measures
such as tree width, which bound the complexity of solving a CSP, can also be applied directly
to Bayes nets. Moreover, the variable elimination algorithm can be generalized to solve CSPs
as well as Bayes nets.
As well as reducing satisﬁability problems to Bayes net inference, we can reduce Bayes
net inference to satisﬁability, which allows us to take advantage of the powerful machinery
developed for SAT-solving (see Chapter 7). In this case, the reduction is to a particular
form of SAT solving called weighted model counting (WMC). Regular model counting
Weighted model
counting
counts the number of satisfying assignments for a SAT expression; WMC sums the total
weight of those satisfying assignments—where, in this application, the weight is essentially
the product of the conditional probabilities for each variable assignment given its parents.
(See Exercise 13.WMCX for details.) Partly because SAT-solving technology has been so
well optimized for large-scale applications, Bayes net inference via WMC is competitive
with and sometimes superior to other exact algorithms on networks with large tree width.
13.3.4 Clustering algorithms
The variable elimination algorithm is simple and efﬁcient for answering individual queries. If
we want to compute posterior probabilities for all the variables in a network, however, it can
be less efﬁcient. For example, in a polytree network, one would need to issue O(n) queries
costing O(n) each, for a total of O(n2) time. Using clustering algorithms (also known as
Clustering
join tree algorithms), the time can be reduced to O(n). For this reason, these algorithms are
Join tree
widely used in commercial Bayes net tools.
The basic idea of clustering is to join individual nodes of the network to form cluster
nodes in such a way that the resulting network is a polytree. For example, the multiply
connected network shown in Figure 13.15(a) can be converted into a polytree by combining
the Sprinkler and Rain node into a cluster node called Sprinkler+Rain, as shown in Fig-
