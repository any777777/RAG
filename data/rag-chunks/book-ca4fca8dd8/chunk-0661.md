---
chunk_id: "book-ca4fca8dd8-chunk-0661"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 661
confidence: "first-pass"
extraction_method: "structured-local"
---

398
Chapter 11
Automated Planning
say, each individual coin and bill in the world. Time is one of the most important
resources. It can be handled by specialized scheduling algorithms, or scheduling can be
integrated with planning.
• This chapter extends classical planning to cover nondeterministic environments (where
outcomes of actions are uncertain), but it is not the last word on planning. Chapter 16
describes techniques for stochastic environments (in which outcomes of actions have
probabilities associated with them): Markov decision processes, partially observable
Markov decision processes, and game theory. In Chapter 23 we show that reinforcement
learning allows an agent to learn how to behave from past successes and failures.
Bibliographical and Historical Notes
AI planning arose from investigations into state-space search, theorem proving, and control
theory. STRIPS (Fikes and Nilsson, 1971, 1993), the ﬁrst major planning system, was de-
signed as the planner for the Shakey robot at SRI. The ﬁrst version of the program ran on a
computer with only 192 KB of memory. Its overall control structure was modeled on GPS,
the General Problem Solver (Newell and Simon, 1961), a state-space search system that used
means–ends analysis.
The STRIPS representation language evolved into the Action Description Language, or
ADL (Pednault, 1986), and then the Problem Domain Description Language, or PDDL
(Ghallab et al., 1998), which has been used for the International Planning Competition since
1998. The most recent version is PDDL 3.1 (Kovacs, 2011).
Planners in the early 1970s decomposed problems by computing a subplan for each sub-
goal and then stringing the subplans together in some order. This approach, called linear
planning by Sacerdoti (1975), was soon discovered to be incomplete. It cannot solve some
Linear planning
very simple problems, such as the Sussman anomaly (see Exercise 11.SUSS), found by Allen
Brown during experimentation with the HACKER system (Sussman, 1975). A complete plan-
ner must allow for interleaving of actions from different subplans within a single sequence.
Warren’s (1974) WARPLAN system achieved that, and demonstrated how the logic program-
ming language Prolog can produce concise programs; WARPLAN is only 100 lines of code.
Partial-order planning dominated the next 20 years of research, with theoretical work
describing the detection of conﬂicts (Tate, 1975a) and the protection of achieved condi-
tions (Sussman, 1975), and implementations including NOAH (Sacerdoti, 1977) and NONLIN
(Tate, 1977). That led to formal models (Chapman, 1987; McAllester and Rosenblitt, 1991)
that allowed for theoretical analysis of various algorithms and planning problems, and to a
widely distributed system, UCPOP (Penberthy and Weld, 1992).
Drew McDermott suspected that the emphasis on partial-order planning was crowding out
other techniques that should perhaps be reconsidered now that computers had 100 times the
memory of Shakey’s day. His UNPOP (McDermott, 1996) was a state-space planning pro-
gram employing the ignore-delete-list heuristic. HSP, the Heuristic Search Planner (Bonet
and Geffner, 1999; Haslum, 2006) made state-space search practical for large planning prob-
lems. The FF or Fast Forward planner (Hoffmann, 2001; Hoffmann and Nebel, 2001; Hoff-
mann, 2005) and the FASTDOWNWARD variant (Helmert, 2006) won international planning
competitions in the 2000s.
