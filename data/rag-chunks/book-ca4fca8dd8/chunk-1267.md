---
chunk_id: "book-ca4fca8dd8-chunk-1267"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1267
confidence: "first-pass"
extraction_method: "structured-local"
---

768
Chapter 20
Knowledge in Learning
Bibliographical and Historical Notes
Although the use of prior knowledge in learning would seem to be a natural topic for philoso-
phers of science, little formal work was done until quite recently. Fact, Fiction, and Forecast,
by the philosopher Nelson Goodman (1954), refuted the earlier supposition that induction
was simply a matter of seeing enough examples of some universally quantiﬁed proposition
and then adopting it as a hypothesis. Consider, for example, the hypothesis “All emeralds are
grue,” where grue means “green if observed before time t, but blue if observed thereafter.”
At any time up to t, we might have observed millions of instances conﬁrming the rule that
emeralds are grue, and no disconﬁrming instances, and yet we are unwilling to adopt the rule.
This can be explained only by appeal to the role of relevant prior knowledge in the induction
process. Goodman proposes a variety of different kinds of prior knowledge that might be use-
ful, including a version of determinations called overhypotheses. Unfortunately, Goodman’s
ideas were never pursued in machine learning.
The current-best-hypothesis approach is an old idea in philosophy (Mill, 1843). Early
work in cognitive psychology also suggested that it is a natural form of concept learning in
humans (Bruner et al., 1957). In AI, the approach is most closely associated with the work
of Patrick Winston, whose Ph.D. thesis (Winston, 1970) addressed the problem of learning
descriptions of complex objects. The version space method (Mitchell, 1977, 1982) takes
a different approach, maintaining the set of all consistent hypotheses and eliminating those
found to be inconsistent with new examples. The approach was used in the Meta-DENDRAL
expert system for chemistry (Buchanan and Mitchell, 1978), and later in Mitchell’s (1983)
LEX system, which learns to solve calculus problems. A third inﬂuential thread was formed
by the work of Michalski and colleagues on the AQ series of algorithms, which learned sets
of logical rules (Michalski, 1969; Michalski et al., 1986).
EBL had its roots in the techniques used by the STRIPS planner (Fikes et al., 1972).
When a plan was constructed, a generalized version of it was saved in a plan library and
used in later planning as a macro-operator. Similar ideas appeared in Anderson’s ACT*
architecture, under the heading of knowledge compilation (Anderson, 1983), and in the
SOAR architecture, as chunking (Laird et al., 1986). Schema acquisition (DeJong, 1981),
analytical generalization (Mitchell, 1982), and constraint-based generalization (Minton,
1984) were immediate precursors of the rapid growth of interest in EBL stimulated by the
papers of Mitchell et al. (1986) and DeJong and Mooney (1986). Hirsh (1987) introduced
the EBL algorithm described in the text, showing how it could be incorporated directly into a
logic programming system. Van Harmelen and Bundy (1988) explain EBL as a variant of the
partial evaluation method used in program analysis systems (Jones et al., 1993).
Initial enthusiasm for EBL was tempered by Minton’s ﬁnding (1988) that, without exten-
sive extra work, EBL could easily slow down a program signiﬁcantly. Formal probabilistic
analysis of the expected payoff of EBL can be found in Greiner (1989) and Subramanian and
Feldman (1990). An excellent survey of early work on EBL appears in Dietterich (1990).
Instead of using examples as foci for generalization, one can use them directly to solve
new problems, in a process known as analogical reasoning. This form of reasoning ranges
Analogical reasoning
from a form of plausible reasoning based on degree of similarity (Gentner, 1983), through
a form of deductive inference based on determinations but requiring the participation of the
example (Davies and Russell, 1987), to a form of “lazy” EBL that tailors the direction of
