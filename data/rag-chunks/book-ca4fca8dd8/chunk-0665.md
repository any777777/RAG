---
chunk_id: "book-ca4fca8dd8-chunk-0665"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 665
confidence: "first-pass"
extraction_method: "structured-local"
---

400
Chapter 11
Automated Planning
approaches do better in domains where feasible solutions can be found without backtracking.
Graphplan and SATPLAN have trouble in domains with many objects because that means
they must create many actions. In some cases the problem can be delayed or avoided by gen-
erating the propositionalized actions dynamically, only as needed, rather than instantiating
them all before the search begins.
The ﬁrst mechanism for hierarchical planning was a facility in the STRIPS program for
learning macrops—“macro-operators” consisting of a sequence of primitive steps (Fikes
Macrops
et al., 1972). The ABSTRIPS system (Sacerdoti, 1974) introduced the idea of an abstraction
hierarchy, whereby planning at higher levels was permitted to ignore lower-level precon-
Abstraction
hierarchy
ditions of actions in order to derive the general structure of a working plan. Austin Tate’s
Ph.D. thesis (1975b) and work by Earl Sacerdoti (1977) developed the basic ideas of HTN
planning. Erol, Hendler, and Nau (1994, 1996) present a complete hierarchical decomposi-
tion planner as well as a range of complexity results for pure HTN planners. Our presentation
of HLAs and angelic semantics is due to Marthi et al. (2007, 2008).
One of the goals of hierarchical planning has been the reuse of previous planning ex-
perience in the form of generalized plans. The technique of explanation-based learning
has been used as a means of generalizing previously computed plans in systems such as
SOAR (Laird et al., 1986) and PRODIGY (Carbonell et al., 1989). An alternative approach is
to store previously computed plans in their original form and then reuse them to solve new,
similar problems by analogy to the original problem. This is the approach taken by the ﬁeld
called case-based planning (Carbonell, 1983; Alterman, 1988). Kambhampati (1994) argues
Case-based planning
that case-based planning should be analyzed as a form of reﬁnement planning and provides a
formal foundation for case-based partial-order planning.
Early planners lacked conditionals and loops, but some could use coercion to form con-
formant plans. Sacerdoti’s NOAH solved the “keys and boxes” problem (in which the planner
knows little about the initial state) using coercion. Mason (1993) argued that sensing often
can and should be dispensed with in robotic planning, and described a sensorless plan that
can move a tool into a speciﬁc position on a table by a sequence of tilting actions, regardless
of the initial position.
Goldman and Boddy (1996) introduced the term conformant planning, noting that sen-
sorless plans are often effective even if the agent has sensors. The ﬁrst moderately efﬁcient
conformant planner was Smith and Weld’s (1998) Conformant Graphplan (CGP). Ferraris
and Giunchiglia (2000) and Rintanen (1999) independently developed SATPLAN-based con-
formant planners. Bonet and Geffner (2000) describe a conformant planner based on heuristic
search in the space of belief states, drawing on ideas ﬁrst developed in the 1960s for partially
observable Markov decision processes, or POMDPs (see Chapter 16).
Currently, there are three main approaches to conformant planning. The ﬁrst two use
heuristic search in belief-state space: HSCP (Bertoli et al., 2001a) uses binary decision di-
agrams (BDDs) to represent belief states, whereas Hoffmann and Brafman (2006) adopt the
lazy approach of computing precondition and goal tests on demand using a SAT solver.
The third approach, championed primarily by Jussi Rintanen (2007), formulates the entire
sensorless planning problem as a quantiﬁed Boolean formula (QBF) and solves it using a
general-purpose QBF solver. Current conformant planners are ﬁve orders of magnitude faster
than CGP. The winner of the 2006 conformant-planning track at the International Planning
Competition was T0 (Palacios and Geffner, 2007), which uses heuristic search in belief-state
