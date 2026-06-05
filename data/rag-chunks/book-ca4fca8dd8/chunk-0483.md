---
chunk_id: "book-ca4fca8dd8-chunk-0483"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 483
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 293

Section 8.4
Knowledge Engineering in First-Order Logic
293
In(1,X1) to denote the ﬁrst input terminal for circuit X1. A similar function Out(n,c) is used
for output terminals. The predicate Arity(c,i, j) says that circuit c has i input and j output
terminals. The connectivity between gates can be represented by a predicate, Connected,
which takes two terminals as arguments, as in Connected(Out(1,X1),In(1,X2)).
Finally, we need to know whether a signal is on or off. One possibility is to use a unary
predicate, On(t), which is true when the signal at a terminal is on. This makes it a little
difﬁcult, however, to pose questions such as “What are all the possible values of the signals
at the output terminals of circuit C1 ?” We therefore introduce as objects two signal values,
1 and 0, representing “on” and “off” respectively, and a function Signal(t) that denotes the
signal value for the terminal t.
Encode general knowledge of the domain
One sign that we have a good ontology is that we require only a few general rules, which can
be stated clearly and concisely. These are all the axioms we will need:
1. If two terminals are connected, then they have the same signal:
∀t1,t2 Terminal(t1)∧Terminal(t2)∧Connected(t1,t2) ⇒
Signal(t1)=Signal(t2) .
2. The signal at every terminal is either 1 or 0:
∀t Terminal(t) ⇒Signal(t)=1∨Signal(t)=0 .
3. Connected is commutative:
∀t1,t2 Connected(t1,t2) ⇔Connected(t2,t1) .
4. There are four types of gates:
∀g Gate(g)∧k = Type(g) ⇒k = AND∨k = OR∨k = XOR∨k = NOT .
5. An AND gate’s output is 0 if and only if any of its inputs is 0:
∀g Gate(g)∧Type(g)=AND ⇒
Signal(Out(1,g))=0 ⇔∃n Signal(In(n,g))=0 .
6. An OR gate’s output is 1 if and only if any of its inputs is 1:
∀g Gate(g)∧Type(g)=OR ⇒
Signal(Out(1,g))=1 ⇔∃n Signal(In(n,g))=1 .
7. An XOR gate’s output is 1 if and only if its inputs are different:
∀g Gate(g)∧Type(g)=XOR ⇒
Signal(Out(1,g))=1 ⇔Signal(In(1,g)) ̸= Signal(In(2,g)) .
8. A NOT gate’s output is different from its input:
∀g Gate(g)∧Type(g)=NOT ⇒
Signal(Out(1,g)) ̸= Signal(In(1,g)) .
9. The gates (except for NOT) have two inputs and one output.
∀g Gate(g)∧Type(g) = NOT ⇒Arity(g,1,1) .
∀g Gate(g)∧k = Type(g)∧(k = AND∨k = OR∨k = XOR) ⇒
Arity(g,2,1)
10. A circuit has terminals, up to its input and output arity, and nothing beyond its arity:
∀c,i, j Circuit(c)∧Arity(c,i, j) ⇒
∀n (n ≤i ⇒Terminal(In(n,c)))∧(n > i ⇒In(n,c) = Nothing)∧
∀n (n ≤j ⇒Terminal(Out(n,c)))∧(n > j ⇒Out(n,c) = Nothing)

## Page 294
