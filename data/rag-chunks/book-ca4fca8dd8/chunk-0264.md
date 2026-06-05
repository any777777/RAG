---
chunk_id: "book-ca4fca8dd8-chunk-0264"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 264
confidence: "first-pass"
extraction_method: "structured-local"
---

162
Chapter 4
Search in Complex Environments
putation Conference (GECCO). Good overview texts on genetic algorithms include those by
Mitchell (1996), Fogel (2000), Langdon and Poli (2002), and Poli et al. (2008).
The unpredictability and partial observability of real environments were recognized early
on in robotics projects that used planning techniques, including Shakey (Fikes et al., 1972)
and FREDDY (Michie, 1972). The problems received more attention after the publication of
McDermott’s (1978a) inﬂuential article Planning and Acting.
The ﬁrst work to make explicit use of AND–OR trees seems to have been Slagle’s SAINT
program for symbolic integration, mentioned in Chapter 1. Amarel (1967) applied the idea
to propositional theorem proving, a topic discussed in Chapter 7, and introduced a search
algorithm similar to AND-OR-GRAPH-SEARCH. The algorithm was further developed by
Nilsson (1971), who also described AO∗—which, as its name suggests, ﬁnds optimal solu-
tions. AO∗was further improved by Martelli and Montanari (1973).
AO∗is a top-down algorithm; a bottom-up generalization of A∗is A∗LD, for A∗Light-
est Derivation (Felzenszwalb and McAllester, 2007). Interest in AND–OR search underwent
a revival in the early 2000s, with new algorithms for ﬁnding cyclic solutions (Jimenez and
Torras, 2000; Hansen and Zilberstein, 2001) and new techniques inspired by dynamic pro-
gramming (Bonet and Geffner, 2005).
The idea of transforming partially observable problems into belief-state problems origi-
nated with Astrom (1965) for the much more complex case of probabilistic uncertainty (see
Chapter 16). Erdmann and Mason (1988) studied the problem of robotic manipulation with-
out sensors, using a continuous form of belief-state search. They showed that it was possible
to orient a part on a table from an arbitrary initial position by a well-designed sequence of tilt-
ing actions. More practical methods, based on a series of precisely oriented diagonal barriers
across a conveyor belt, use the same algorithmic insights (Wiegley et al., 1996).
The belief-state approach was reinvented in the context of sensorless and partially ob-
servable search problems by Genesereth and Nourbakhsh (1993). Additional work was done
on sensorless problems in the logic-based planning community (Goldman and Boddy, 1996;
Smith and Weld, 1998). This work has emphasized concise representations for belief states,
as explained in Chapter 11. Bonet and Geffner (2000) introduced the ﬁrst effective heuristics
for belief-state search; these were reﬁned by Bryce et al. (2006). The incremental approach
to belief-state search, in which solutions are constructed incrementally for subsets of states
within each belief state, was studied in the planning literature by Kurien et al. (2002); several
new incremental algorithms were introduced for nondeterministic, partially observable prob-
lems by Russell and Wolfe (2005). Additional references for planning in stochastic, partially
observable environments appear in Chapter 16.
Algorithms for exploring unknown state spaces have been of interest for many centuries.
Depth-ﬁrst search in a reversible maze can be implemented by keeping one’s left hand on
the wall; loops can be avoided by marking each junction. The more general problem of
exploring Eulerian graphs (i.e., graphs in which each node has equal numbers of incoming
Eulerian graph
and outgoing edges) was solved by an algorithm due to Hierholzer (1873).
The ﬁrst thorough algorithmic study of the exploration problem for arbitrary graphs was
carried out by Deng and Papadimitriou (1990), who developed a completely general algo-
rithm but showed that no bounded competitive ratio is possible for exploring a general graph.
Papadimitriou and Yannakakis (1991) examined the question of ﬁnding paths to a goal in
geometric path-planning environments (where all actions are reversible). They showed that
