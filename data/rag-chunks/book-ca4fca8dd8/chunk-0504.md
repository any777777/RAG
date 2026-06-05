---
chunk_id: "book-ca4fca8dd8-chunk-0504"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 504
confidence: "first-pass"
extraction_method: "structured-local"
---

308
Chapter 9
Inference in First-Order Logic
Q
NT
WA
SA
V
NSW
T
Diff(wa,nt)∧Diff(wa,sa)∧
Diff(nt,q)∧Diff(nt,sa)∧
Diff(q,nsw)∧Diff(q,sa)∧
Diff(nsw,v)∧Diff(nsw,sa)∧
Diff(v,sa) ⇒Colorable()
Diff(Red,Blue)
Diff(Red,Green)
Diff(Green,Red) Diff(Green,Blue)
Diff(Blue,Red) Diff(Blue,Green)
(a)
(b)
Figure 9.5 (a) Constraint graph for coloring the map of Australia. (b) The map-coloring
CSP expressed as a single deﬁnite clause. Each map region is represented as a variable
whose value can be one of the constants Red, Green, or Blue (which are declared Diff).
base, this can be done in constant time per fact. Now consider a rule such as
Missile(x)∧Owns(Nono,x) ⇒Sells(West,x,Nono).
Again, we can ﬁnd all the objects owned by Nono in constant time per object; then, for each
object, we could check whether it is a missile. However, if the knowledge base contains
many objects owned by Nono and very few missiles, then it would be better to ﬁnd all the
missiles ﬁrst and then check whether they are owned by Nono. This is the conjunct ordering
Conjunct ordering
problem: ﬁnd an ordering to solve the conjuncts of the rule premise so that the total cost is
minimized. It turns out that ﬁnding the optimal ordering is NP-hard, but good heuristics are
available. For example, the minimum-remaining-values (MRV) heuristic used for CSPs in
Chapter 5 would suggest ordering the conjuncts to look for missiles ﬁrst if there are fewer
missiles than there are objects owned by Nono.
The connection between this pattern matching and constraint satisfaction is actually
Pattern matching
very close. We can view each conjunct as a constraint on the variables that it contains—for
example, Missile(x) is a unary constraint on x. Extending this idea, we can express every
▶
ﬁnite-domain CSP as a single deﬁnite clause together with some associated ground facts.
Consider the map-coloring problem from Figure 5.1, shown again in Figure 9.5(a). An equiv-
alent formulation as a single deﬁnite clause is given in Figure 9.5(b). Clearly, the conclusion
Colorable() can be inferred only if the CSP has a solution. Because CSPs in general include
3-SAT problems as special cases, we can conclude that matching a deﬁnite clause against a
▶
set of facts is NP-hard.
It might seem rather depressing that forward chaining has an NP-hard matching problem
in its inner loop. There are three ways to cheer ourselves up:
• We can remind ourselves that most rules in real-world knowledge bases are small and
simple (like the rules in our crime example) rather than large and complex (like the
CSP formulation in Figure 9.5). It is common in the database world to assume that
both the sizes of rules and the arities of predicates are bounded by a constant and to
worry only about data complexity—that is, the complexity of inference as a function
Data complexity
