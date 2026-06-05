---
chunk_id: "book-ca4fca8dd8-chunk-0669"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 669
confidence: "first-pass"
extraction_method: "structured-local"
---

402
Chapter 11
Automated Planning
scotte and Latombe, 1985) planned the machining and construction of mechanical parts,
FORBIN was used for factory control, and NONLIN+ was used for naval logistics planning.
We chose to present planning and scheduling as two separate problems; Cushing et al. (2007)
show that this can lead to incompleteness on certain problems.
There is a long history of scheduling in aerospace. T-SCHED (Drabble, 1990) was used
to schedule mission-command sequences for the UOSAT-II satellite. OPTIMUM-AIV (Aarup
et al., 1994) and PLAN-ERS1 (Fuchs et al., 1990), both based on O-PLAN, were used for
spacecraft assembly and observation planning, respectively, at the European Space Agency.
SPIKE (Johnston and Adorf, 1992) was used for observation planning at NASA for the Hub-
ble Space Telescope, while the Space Shuttle Ground Processing Scheduling System (Deale
et al., 1994) does job-shop scheduling of up to 16,000 worker-shifts. Remote Agent (Muscet-
tola et al., 1998) became the ﬁrst autonomous planner–scheduler to control a spacecraft, when
it ﬂew onboard the Deep Space One probe in 1999. Space applications have driven the de-
velopment of algorithms for resource allocation; see Laborie (2003) and Muscettola (2002).
The literature on scheduling is presented in a classic survey article (Lawler et al., 1993), a
book (Pinedo, 2008), and an edited handbook (Blazewicz et al., 2007).
The computational complexity of planning has been analyzed by several authors (By-
lander, 1994; Ghallab et al., 2004; Rintanen, 2016). There are two main tasks: PlanSAT
is the question of whether there exists any plan that solves a planning problem. Bounded
PlanSAT asks whether there is a solution of length k or less; this can be used to ﬁnd an op-
timal plan. Both are decidable for classical planning (because the number of states is ﬁnite).
But if we add function symbols to the language, then the number of states becomes inﬁnite,
and PlanSAT becomes only semidecidable. For propositionalized problems both are in the
complexity class PSPACE, a class that is larger (and hence more difﬁcult) than NP and refers
to problems that can be solved by a deterministic Turing machine with a polynomial amount
of space. These theoretical results are discouraging, but in practice, the problems we want
to solve tend to be not so bad. The true advantage of the classical planning formalism is
that it has facilitated the development of very accurate domain-independent heuristics; other
approaches have not been as fruitful.
Readings in Planning (Allen et al., 1990) is a comprehensive anthology of early work
in the ﬁeld. Weld (1994, 1999) provides two excellent surveys of planning algorithms of the
1990s. It is interesting to see the change in the ﬁve years between the two surveys: the ﬁrst
concentrates on partial-order planning, and the second introduces Graphplan and SATPLAN.
Automated Planning and Acting (Ghallab et al., 2016) is an excellent textbook on all aspects
of the ﬁeld. LaValle’s text Planning Algorithms (2006) covers both classical and stochastic
planning, with extensive coverage of robot motion planning.
Planning research has been central to AI since its inception, and papers on planning are
a staple of mainstream AI journals and conferences. There are also specialized conferences
such as the International Conference on Automated Planning and Scheduling and the Inter-
national Workshop on Planning and Scheduling for Space.
