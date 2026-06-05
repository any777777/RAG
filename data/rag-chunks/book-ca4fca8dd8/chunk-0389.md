---
chunk_id: "book-ca4fca8dd8-chunk-0389"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 389
confidence: "first-pass"
extraction_method: "structured-local"
---

238
Chapter 7
Logical Agents
written using ⇔. For example, a square is breezy if a neighboring square has a pit, and a
square is breezy only if a neighboring square has a pit. So we need a biconditional,
B1,1 ⇔(P1,2 ∨P2,1),
where B1,1 means that there is a breeze in [1,1].
7.4.3 A simple knowledge base
Now that we have deﬁned the semantics for propositional logic, we can construct a knowledge
base for the wumpus world. We focus ﬁrst on the immutable aspects of the wumpus world,
leaving the mutable aspects for a later section. For now, we need the following symbols for
each [x,y] location:
Px,y is true if there is a pit in [x,y].
Wx,y is true if there is a wumpus in [x,y], dead or alive.
Bx,y is true if there is a breeze in [x,y].
Sx,y is true if there is a stench in [x,y].
Lx,y is true if the agent is in location [x,y].
The sentences we write will sufﬁce to derive ¬P1,2 (there is no pit in [1,2]), as was done
informally in Section 7.3. We label each sentence Ri so that we can refer to them:
• There is no pit in [1,1]:
R1 :
¬P1,1 .
• A square is breezy if and only if there is a pit in a neighboring square. This has to be
stated for each square; for now, we include just the relevant squares:
R2 :
B1,1
⇔
(P1,2 ∨P2,1).
R3 :
B2,1
⇔
(P1,1 ∨P2,2 ∨P3,1).
• The preceding sentences are true in all wumpus worlds. Now we include the breeze
percepts for the ﬁrst two squares visited in the speciﬁc world the agent is in, leading up
to the situation in Figure 7.3(b).
R4 :
¬B1,1 .
R5 :
B2,1 .
7.4.4 A simple inference procedure
Our goal now is to decide whether KB |= α for some sentence α. For example, is ¬P1,2
entailed by our KB? Our ﬁrst algorithm for inference is a model-checking approach that is a
direct implementation of the deﬁnition of entailment: enumerate the models, and check that
α is true in every model in which KB is true. Models are assignments of true or false to
every proposition symbol. Returning to our wumpus-world example, the relevant proposition
symbols are B1,1, B2,1, P1,1, P1,2, P2,1, P2,2, and P3,1. With seven symbols, there are 27 =128
possible models; in three of these, KB is true (Figure 7.9). In those three models, ¬P1,2 is
true, hence there is no pit in [1,2]. On the other hand, P2,2 is true in two of the three models
and false in one, so we cannot yet tell whether there is a pit in [2,2].
Figure 7.9 reproduces in a more precise form the reasoning illustrated in Figure 7.5. A
general algorithm for deciding entailment in propositional logic is shown in Figure 7.10. Like
the BACKTRACKING-SEARCH algorithm on page 176, TT-ENTAILS? performs a recursive
