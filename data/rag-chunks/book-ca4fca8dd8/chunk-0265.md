---
chunk_id: "book-ca4fca8dd8-chunk-0265"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 265
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 163

Bibliographical and Historical Notes
163
a small competitive ratio is achievable with square obstacles, but with general rectangular
obstacles no bounded ratio can be achieved. (See Figure 4.20.)
In a dynamic environment, the state of the world can spontaneously change without any
action by the agent. For example, the agent can plan an optimal driving route from A to B,
but an accident or unusually bad rush hour trafﬁc can spoil the plan. Incremental search algo-
rithms such as Lifelong Planning A∗(Koenig et al., 2004) and D∗Lite (Koenig and Likhachev,
2002) deal with this situation.
The LRTA∗algorithm was developed by Korf (1990) as part of an investigation into real-
time search for environments in which the agent must act after searching for only a ﬁxed
amount of time (a common situation in two-player games). LRTA∗is in fact a special case of
reinforcement learning algorithms for stochastic environments (Barto et al., 1995). Its policy
of optimism under uncertainty—always head for the closest unvisited state—can result in
an exploration pattern that is less efﬁcient in the uninformed case than simple depth-ﬁrst
search (Koenig, 2000). Dasgupta et al. (1994) show that online iterative deepening search is
optimally efﬁcient for ﬁnding a goal in a uniform tree with no heuristic information.
Several informed variants on the LRTA∗theme have been developed with different meth-
ods for searching and updating within the known portion of the graph (Pemberton and Korf,
1992). As yet, there is no good theoretical understanding of how to ﬁnd goals with opti-
mal efﬁciency when using heuristic information. Sturtevant and Bulitko (2016) provide an
analysis of some pitfalls that occur in practice.

## Page 164
