---
chunk_id: "book-ca4fca8dd8-chunk-0210"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 210
confidence: "first-pass"
extraction_method: "structured-local"
---

126
Chapter 3
Solving Problems by Searching
noted that several well-known problems contained exponentially many nodes on optimal-cost
solution paths, implying exponential time complexity for A∗.
There are many variations on the A∗algorithm. Pohl (1970) introduced weighted A∗
search, and later a dynamic version (1973), where the weight changes over the depth of the
tree. Ebendt and Drechsler (2009) synthesize the results and examine some applications.
Hatem and Ruml (2014) show a simpliﬁed and improved version of weighted A∗that is easier
to implement. Wilt and Ruml (2014) introduce speedy search as an alternative to greedy
search that focuses on minimizing search time, and Wilt and Ruml (2016) show that the
best heuristics for satisﬁcing search are different from the ones for optimal search. Burns
et al. (2012) give some implementation tricks for writing fast search code, and Felner (2018)
considers how the implementation changes when using an early goal test.
Pohl (1971) introduced bidirectional search. Holte et al. (2016) describe the version of
bidirectional search that is guaranteed to meet in the middle, making it more widely applica-
ble. Eckerle et al. (2017) describe the set of surely expanded pairs of nodes, and show that
no bidirectional search can be optimally efﬁcient. The NBS algorithm (Chen et al., 2017)
makes explicit use of a queue of pairs of nodes.
A combination of bidirectional A∗and known landmarks was used to efﬁciently ﬁnd
driving routes for Microsoft’s online map service (Goldberg et al., 2006). After caching a
set of paths between landmarks, the algorithm can ﬁnd an optimal-cost path between any
pair of points in a 24-million-point graph of the United States, searching less than 0.1%
of the graph. Korf (1987) shows how to use subgoals, macro-operators, and abstraction to
achieve remarkable speedups over previous techniques. Delling et al. (2009) describe how
to use bidirectional search, landmarks, hierarchical structure, and other tricks to ﬁnd driving
routes. Anderson et al. (2008) describe a related technique, called coarse-to-ﬁne search,
Coarse-to-ﬁne search
which can be thought of as deﬁning landmarks at various hierarchical levels of abstraction.
Korf (1987) describes conditions under which coarse-to-ﬁne search provides an exponential
speedup. Knoblock (1991) provides experimental results and analysis to quantify the advan-
tages of hierarchical search.
A∗and other state-space search algorithms are closely related to the branch-and-bound
Branch-and-bound
techniques that are widely used in operations research (Lawler and Wood, 1966; Rayward-
Smith et al., 1996). Kumar and Kanal (1988) attempt a “grand uniﬁcation” of heuristic
search, dynamic programming, and branch-and-bound techniques under the name of CDP—
the “composite decision process.”
Because most computers in the 1960s had only a few thousand words of main memory,
memory-bounded heuristic search was an early research topic. The Graph Traverser (Doran
and Michie, 1966), one of the earliest search programs, commits to an action after search-
ing best-ﬁrst up to the memory limit. IDA∗(Korf, 1985b) was the ﬁrst widely used length-
optimal, memory-bounded heuristic search algorithm, and a large number of variants have
been developed. An analysis of the efﬁciency of IDA∗and of its difﬁculties with real-valued
heuristics appears in Patrick et al. (1992).
The original version of RBFS (Korf, 1993) is actually somewhat more complicated than
the algorithm shown in Figure 3.22, which is actually closer to an independently developed
algorithm called iterative expansion or IE (Russell, 1992). RBFS uses a lower bound as
Iterative expansion
well as the upper bound; the two algorithms behave identically with admissible heuristics,
but RBFS expands nodes in best-ﬁrst order even with an inadmissible heuristic. The idea of
