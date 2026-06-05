---
chunk_id: "book-ca4fca8dd8-chunk-0969"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 969
confidence: "first-pass"
extraction_method: "structured-local"
---

586
Chapter 16
Making Complex Decisions
Bibliographical and Historical Notes
Richard Bellman developed the ideas underlying the modern approach to sequential deci-
sion problems while working at the RAND Corporation beginning in 1949. According to his
autobiography (Bellman, 1984), he coined the term “dynamic programming” to hide from
a research-phobic Secretary of Defense, Charles Wilson, the fact that his group was doing
mathematics. (This cannot be strictly true, because his ﬁrst paper using the term (Bellman,
1952) appeared before Wilson became Secretary of Defense in 1953.) Bellman’s book, Dy-
namic Programming (1957), gave the new ﬁeld a solid foundation and introduced the value
iteration algorithm.
Shapley (1953b) actually described the value iteration algorithm independently of Bell-
man, but his results were not widely appreciated in the operations research community, per-
haps because they were presented in the more general context of Markov games. Although
the original formulations included discounting, its analysis in terms of stationary preferences
was suggested by Koopmans (1972). The shaping theorem is due to Ng et al. (1999).
Ron Howard’s Ph.D. thesis (1960) introduced policy iteration and the idea of average
reward for solving inﬁnite-horizon problems.
Several additional results were introduced
by Bellman and Dreyfus (1962). The use of contraction mappings in analyzing dynamic
programming algorithms is due to Denardo (1967). Modiﬁed policy iteration is due to van
Nunen (1976) and Puterman and Shin (1978). Asynchronous policy iteration was analyzed
by Williams and Baird (1993), who also proved the policy loss bound in Equation (16.13).
The general family of prioritized sweeping algorithms aims to speed up convergence to op-
timal policies by heuristically ordering the value and policy update calculations (Moore and
Atkeson, 1993; Andre et al., 1998; Wingate and Seppi, 2005).
The formulation of MDP-solving as a linear program is due to de Ghellinck (1960),
Manne (1960), and D’´Epenoux (1963). Although linear programming has traditionally been
considered inferior to dynamic programming as an exact solution method for MDPs, de Farias
and Roy (2003) show that it is possible to use linear programming and a linear representation
of the utility function to obtain provably good approximate solutions to very large MDPs.
Papadimitriou and Tsitsiklis (1987) and Littman et al. (1995) provide general results on the
computational complexity of MDPs. Yinyu Ye (2011) analyzes the relationship between
policy iteration and the simplex method for linear programming and proves that for ﬁxed γ,
the runtime of policy iteration is polynomial in the number of states and actions.
Seminal work by Sutton (1988) and Watkins (1989) on reinforcement learning methods
for solving MDPs played a signiﬁcant role in introducing MDPs into the AI community. (Ear-
lier work by Werbos (1977) contained many similar ideas, but was not taken up to the same
extent.) AI researchers have pushed MDPs in the direction of more expressive representa-
tions that can accommodate much larger problems than the traditional atomic representations
based on transition matrices.
The basic ideas for an agent architecture using dynamic decision networks were proposed
by Dean and Kanazawa (1989a). Tatman and Shachter (1990) showed how to apply dynamic
programming algorithms to DDN models. Several authors made the connection between
MDPs and AI planning problems, developing probabilistic forms of the compact STRIPS
representation for transition models (Wellman, 1990b; Koenig, 1991). The book Planning
and Control by Dean and Wellman (1991) explores the connection in great depth.
