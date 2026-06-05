---
chunk_id: "book-ca4fca8dd8-chunk-0403"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 403
confidence: "first-pass"
extraction_method: "structured-local"
---

248
Chapter 7
Logical Agents
most one is positive. So all deﬁnite clauses are Horn clauses, as are clauses with no positive
literals; these are called goal clauses. Horn clauses are closed under resolution: if you resolve
Goal clauses
two Horn clauses, you get back a Horn clause. One more class is the k-CNF sentence, which
is a CNF sentence where each clause has at most k literals.
Knowledge bases containing only deﬁnite clauses are interesting for three reasons:
1. Every deﬁnite clause can be written as an implication whose premise is a conjunction of
positive literals and whose conclusion is a single positive literal. (See Exercise 7.DISJ.)
For example, the deﬁnite clause (¬L1,1 ∨¬Breeze∨B1,1) can be written as the implica-
tion (L1,1∧Breeze) ⇒B1,1. In the implication form, the sentence is easier to understand:
it says that if the agent is in [1,1] and there is a breeze percept, then [1,1] is breezy. In
Horn form, the premise is called the body and the conclusion is called the head. A
Body
Head
sentence consisting of a single positive literal, such as L1,1, is called a fact. It too can
Fact
be written in implication form as True ⇒L1,1, but it is simpler to write just L1,1.
2. Inference with Horn clauses can be done through the forward-chaining and backward-
Forward-chaining
chaining algorithms, which we explain next. Both of these algorithms are natural,
Backward-chaining
in that the inference steps are obvious and easy for humans to follow. This type of
inference is the basis for logic programming, which is discussed in Chapter 9.
3. Deciding entailment with Horn clauses can be done in time that is linear in the size of
the knowledge base—a pleasant surprise.
7.5.4 Forward and backward chaining
The forward-chaining algorithm PL-FC-ENTAILS?(KB, q) determines if a single proposition
symbol q—the query—is entailed by a knowledge base of deﬁnite clauses. It begins from
known facts (positive literals) in the knowledge base. If all the premises of an implication are
known, then its conclusion is added to the set of known facts. For example, if L1,1 and Breeze
are known and (L1,1 ∧Breeze) ⇒B1,1 is in the knowledge base, then B1,1 can be added. This
process continues until the query q is added or until no further inferences can be made. The
algorithm is shown in Figure 7.15; the main point to remember is that it runs in linear time.
The best way to understand the algorithm is through an example and a picture. Fig-
ure 7.16(a) shows a simple knowledge base of Horn clauses with A and B as known facts.
Figure 7.16(b) shows the same knowledge base drawn as an AND–OR graph (see Chapter 4).
In AND–OR graphs, multiple edges joined by an arc indicate a conjunction—every edge must
be proved—while multiple edges without an arc indicate a disjunction—any edge can be
proved. It is easy to see how forward chaining works in the graph. The known leaves (here,
A and B) are set, and inference propagates up the graph as far as possible. Wherever a con-
junction appears, the propagation waits until all the conjuncts are known before proceeding.
The reader is encouraged to work through the example in detail.
It is easy to see that forward chaining is sound: every inference is essentially an appli-
cation of Modus Ponens. Forward chaining is also complete: every entailed atomic sentence
will be derived. The easiest way to see this is to consider the ﬁnal state of the inferred table
(after the algorithm reaches a ﬁxed point where no new inferences are possible). The table
contains true for each symbol inferred during the process, and false for all other symbols. We
can view the table as a logical model; moreover, every deﬁnite clause in the original KB is
▶
true in this model.
