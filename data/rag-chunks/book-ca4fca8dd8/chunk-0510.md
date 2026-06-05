---
chunk_id: "book-ca4fca8dd8-chunk-0510"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 510
confidence: "first-pass"
extraction_method: "structured-local"
---

312
Chapter 9
Inference in First-Order Logic
Hostile(Nono)
Enemy(Nono,America)
Owns(Nono,M1)
Missile(M1)
Criminal(West)
Missile(y)
Weapon(y)
Sells(West,M1,z)
American(West)
{y/M1}
{ }
{ }
{ }
{z/Nono}
{ }
Figure 9.7 Proof tree constructed by backward chaining to prove that West is a criminal.
The tree should be read depth ﬁrst, left to right. To prove Criminal(West), we have to prove
the four conjuncts below it. Some of these are in the knowledge base, and others require
further backward chaining. Bindings for each successful uniﬁcation are shown next to the
corresponding subgoal. Note that once one subgoal in a conjunction succeeds, its substitution
is applied to subsequent subgoals. Thus, by the time FOL-BC-ASK gets to the last conjunct,
originally Hostile(z), z is already bound to Nono.
unify with the goal, standardizing the variables in the clause to be brand-new variables, and
then, if the rhs of the clause does indeed unify with the goal, proving every conjunct in the lhs,
using FOL-BC-AND. That function works by proving each of the conjuncts in turn, keeping
track of the accumulated substitution as it goes. Figure 9.7 is the proof tree for deriving
Criminal(West) from sentences (9.3) through (9.10).
Backward chaining, as we have written it, is clearly a depth-ﬁrst search algorithm. This
means that its space requirements are linear in the size of the proof. It also means that back-
ward chaining (unlike forward chaining) suffers from problems with repeated states and in-
completeness. Despite these limitations, backward chaining has proven to be popular and
effective in logic programming languages.
9.4.2 Logic programming
Logic programming is a technology that comes close to embodying the declarative ideal
described in Chapter 7: that systems should be constructed by expressing knowledge in a
formal language and that problems should be solved by running inference processes on that
knowledge. The ideal is summed up in Robert Kowalski’s equation,
Algorithm = Logic+Control.
Prolog is the most widely used logic programming language. It is used primarily as a rapid-
Prolog
prototyping language and for symbol-manipulation tasks such as writing compilers (Van Roy,
1990) and parsing natural language (Pereira and Warren, 1980). Many expert systems have
been written in Prolog for legal, medical, ﬁnancial, and other domains.
Prolog programs are sets of deﬁnite clauses written in a notation somewhat different
from standard ﬁrst-order logic. Prolog uses uppercase letters for variables and lowercase for
constants—the opposite of our convention for logic. Commas separate conjuncts in a clause,
