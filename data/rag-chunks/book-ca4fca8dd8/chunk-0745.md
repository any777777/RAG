---
chunk_id: "book-ca4fca8dd8-chunk-0745"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 745
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.3
Exact Inference in Bayesian Networks
451
variable. After its removal, there may be some more leaf nodes, and these too may be irrele-
vant. Continuing this process, we eventually ﬁnd that every variable that is not an ancestor ◀
of a query variable or evidence variable is irrelevant to the query. A variable elimination
algorithm can therefore remove all these variables before evaluating the query.
When applied to the insurance network shown in Figure 13.9, variable elimination shows
considerable improvement over the naive enumeration algorithm. Using reverse topological
order for the variables, exact inference using elimination is about 1,000 times faster than the
enumeration algorithm.
13.3.3 The complexity of exact inference
The complexity of exact inference in Bayes nets depends strongly on the structure of the
network. The burglary network of Figure 13.2 belongs to the family of networks in which
there is at most one undirected path (i.e., ignoring the direction of the arrows) between any
two nodes in the network. These are called singly connected networks or polytrees, and
Singly connected
Polytree
they have a particularly nice property: The time and space complexity of exact inference in ◀
polytrees is linear in the size of the network. Here, the size is deﬁned as the number of CPT
entries; if the number of parents of each node is bounded by a constant, then the complexity
will also be linear in the number of nodes. These results hold for any ordering consistent with
the topological ordering of the network (Exercise 13.VEEX).
For multiply connected networks, such as the insurance network in Figure 13.9, variable
Multiply connected
elimination can have exponential time and space complexity in the worst case, even when the
number of parents per node is bounded. This is not surprising when one considers that be- ◀
cause it includes inference in propositional logic as a special case, inference in Bayes nets
is NP-hard. To prove this, we need to work out how to encode a propositional satisﬁability
problem as a Bayes net, such that running inference on this net tells us whether or not the
original propositional sentences are satisﬁable. (In the language of complexity theory, we
reduce satisﬁability problems to Bayes net inference problems.) This turns out to be quite
Reduction
straightforward. Figure 13.14 shows how to encode a particular 3-SAT problem. The propo-
sitional variables become the root variables of the network, each with prior probability 0.5.
The next layer of nodes corresponds to the clauses, with each clause variable Cj connected
to the appropriate variables as parents. The conditional distribution for a clause variable is a
deterministic disjunction, with negation as needed, so that each clause variable is true if and
only if the assignment to its parents satisﬁes that clause. Finally, S is the conjunction of the
clause variables.
To determine if the original sentence is satisﬁable, we simply evaluate P(S=true). If
the sentence is satisﬁable, then there is some possible assignment to the logical variables
that makes S true; in the Bayes net, this means that there is a possible world with nonzero
probability in which the root variables have that assignment, the clause variables have value
true, and S has value true. Therefore, P(S=true) > 0 for a satisﬁable sentence. Conversely,
P(S=true)=0 for an unsatisﬁable sentence: all worlds with S=true have probability 0.
Hence, we can use Bayes net inference to solve 3-SAT problems; from this, we conclude that
Bayes net inference is NP-hard.
We can, in fact, do more than this. Notice that the probability of each satisfying assign-
ment is 2−n for a problem with n variables. Hence, the number of satisfying assignments
is P(S=true)/(2−n). Because computing the number of satisfying assignments for a 3-SAT
