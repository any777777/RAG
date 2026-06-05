---
chunk_id: "book-ca4fca8dd8-chunk-0971"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 971
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
587
Later work on factored MDPs (Boutilier et al., 2000; Koller and Parr, 2000; Guestrin
Factored MDP
et al., 2003b) uses structured representations of the value function as well as the transition
model, with provable improvements in complexity. Relational MDPs (Boutilier et al., 2001;
Relational MDP
Guestrin et al., 2003a) go one step further, using structured representations to handle domains
with many related objects. Open-universe MDPs and POMDPs (Srivastava et al., 2014b) also
allow for uncertainty over the existence and identity of objects and actions.
Many authors have developed approximate online algorithms for decision making in
MDPs, often borrowing explicitly from earlier AI approaches to real-time search and game-
playing (Werbos, 1992; Dean et al., 1993; Tash and Russell, 1994). The work of Barto et al.
(1995) on RTDP (real-time dynamic programming) provided a general framework for under-
standing such algorithms and their connection to reinforcement learning and heuristic search.
The analysis of depth-bounded expectimax with sampling at chance nodes is due to Kearns
et al. (2002). The UCT algorithm described in the chapter is due to Kocsis and Szepes-
vari (2006) and borrows from earlier work on random playouts for estimating the values of
states (Abramson, 1990; Br¨ugmann, 1993; Chang et al., 2005).
Bandit problems were introduced by Thompson (1933) but came to prominence after
World War II through the work of Herbert Robbins (1952). Bradt et al. (1956) proved the
ﬁrst results concerning stopping rules for one-armed bandits, which led eventually to the
breakthrough results of John Gittins (Gittins and Jones, 1974; Gittins, 1989). Katehakis and
Veinott (1987) suggested the restart MDP as a method of computing Gittins indices. The text
by Berry and Fristedt (1985) covers many variations on the basic problem, while the pellucid
online text by Ferguson (2001) connects bandit problems with stopping problems.
Lai and Robbins (1985) initiated the study of the asymptotic regret of optimal bandit
policies. The UCB heuristic was introduced and analyzed by Auer et al. (2002). Bandit su-
perprocesses (BSPs) were ﬁrst studied by Nash (1973) but have remained largely unknown
in AI. Hadﬁeld-Menell and Russell (2015) describe an efﬁcient branch-and-bound algorithm
capable of solving relatively large BSPs. Selection problems were introduced by Bechhofer
(1954). Hay et al. (2012) developed a formal framework for metareasoning problems, show-
ing that simple instances mapped to selection rather than bandit problems. They also proved
the satisfying result that expected computation cost of the optimal computational strategy is
never higher than the expected gain in decision quality—although there are cases where the
optimal policy may, with some probability, keep computing long past the point where any
possible gain has been used up.
The observation that a partially observable MDP can be transformed into a regular MDP
over belief states is due to Astrom (1965) and Aoki (1965). The ﬁrst complete algorithm
for the exact solution of POMDPs—essentially the value iteration algorithm presented in
this chapter—was proposed by Edward Sondik (1971) in his Ph.D. thesis. (A later jour-
nal paper by Smallwood and Sondik (1973) contains some errors, but is more accessible.)
Lovejoy (1991) surveyed the ﬁrst twenty-ﬁve years of POMDP research, reaching somewhat
pessimistic conclusions about the feasibility of solving large problems.
The ﬁrst signiﬁcant contribution within AI was the Witness algorithm (Cassandra et al.,
1994; Kaelbling et al., 1998), an improved version of POMDP value iteration. Other algo-
rithms soon followed, including an approach due to Hansen (1998) that constructs a policy
incrementally in the form of a ﬁnite-state automaton whose states deﬁne the possible belief
states of the agent.
