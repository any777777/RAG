---
chunk_id: "book-ca4fca8dd8-chunk-0667"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 667
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
401
space while keeping the belief-state representation simple by deﬁning derived literals that
cover conditional effects. Bryce and Kambhampati (2007) discuss how a planning graph can
be generalized to generate good heuristics for conformant and contingent planning.
The contingent-planning approach described in the chapter is based on Hoffmann and
Brafman (2005), and was inﬂuenced by the efﬁcient search algorithms for cyclic AND–OR
graphs developed by Jimenez and Torras (2000) and Hansen and Zilberstein (2001). The
problem of contingent planning received more attention after the publication of Drew Mc-
Dermott’s (1978a) inﬂuential article, Planning and Acting. Bertoli et al. (2001b) describe
MBP (Model-Based Planner), which uses binary decision diagrams to do conformant and
contingent planning. Some authors use “conditional planning” and “contingent planning” as
synonyms; others make the distinction that “conditional” refers to actions with nondetermin-
istic effects, and “contingent” means using sensing to overcome partial observability.
In retrospect, it is now possible to see how the major classical planning algorithms led to
extended versions for uncertain domains. Fast-forward heuristic search through state space
led to forward search in belief space (Bonet and Geffner, 2000; Hoffmann and Brafman,
2005); SATPLAN led to stochastic SATPLAN (Majercik and Littman, 2003) and to planning
with quantiﬁed Boolean logic (Rintanen, 2007); partial order planning led to UWL (Etzioni
et al., 1992) and CNLP (Peot and Smith, 1992); Graphplan led to Sensory Graphplan or SGP
(Weld et al., 1998).
The ﬁrst online planner with execution monitoring was PLANEX (Fikes et al., 1972),
which worked with the STRIPS planner to control the robot Shakey. SIPE (System for In-
teractive Planning and Execution monitoring) (Wilkins, 1988) was the ﬁrst planner to deal
systematically with the problem of replanning. It has been used in demonstration projects in
several domains, including planning operations on the ﬂight deck of an aircraft carrier, job-
shop scheduling for an Australian beer factory, and planning the construction of multistory
buildings (Kartam and Levitt, 1990).
In the mid-1980s, pessimism about the slow run times of planning systems led to the pro-
posal of reﬂex agents called reactive planning systems (Brooks, 1986; Agre and Chapman,
Reactive planning
1987). “Universal plans” (Schoppers, 1989) were developed as a lookup-table method for
reactive planning, but turned out to be a rediscovery of the idea of policies that had long been
used in Markov decision processes (see Chapter 16). Koenig (2001) surveys online planning
techniques, under the name Agent-Centered Search.
Planning with time constraints was ﬁrst dealt with by DEVISER (Vere, 1983). The rep-
resentation of time in plans was addressed by Allen (1984) and by Dean et al. (1990) in the
FORBIN system. NONLIN+ (Tate and Whiter, 1984) and SIPE (Wilkins, 1990) could rea-
son about the allocation of limited resources to various plan steps. O-PLAN (Bell and Tate,
1985) has been applied to resource problems such as software procurement planning at Price
Waterhouse and back-axle assembly planning at Jaguar Cars.
The two planners SAPA (Do and Kambhampati, 2001) and T4 (Haslum and Geffner,
2001) both used forward state-space search with sophisticated heuristics to handle actions
with durations and resources. An alternative is to use very expressive action languages, but
guide them by human-written, domain-speciﬁc heuristics, as is done by ASPEN (Fukunaga
et al., 1997), HSTS (Jonsson et al., 2000), and IxTeT (Ghallab and Laruelle, 1994).
A number of hybrid planning-and-scheduling systems have been deployed: ISIS (Fox
et al., 1982; Fox, 1990) has been used for job-shop scheduling at Westinghouse, GARI (De-
