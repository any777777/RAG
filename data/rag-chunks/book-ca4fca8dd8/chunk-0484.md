---
chunk_id: "book-ca4fca8dd8-chunk-0484"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 484
confidence: "first-pass"
extraction_method: "structured-local"
---

294
Chapter 8
First-Order Logic
11. Gates, terminals, and signals are all distinct.
∀g,t,s Gate(g)∧Terminal(t)∧Signal(s) ⇒
g ̸= t ∧g ̸= s∧t ̸= s .
12. Gates are circuits.
∀g Gate(g) ⇒Circuit(g)
Encode the speciﬁc problem instance
The circuit shown in Figure 8.6 is encoded as circuit C1 with the following description. First
we categorize the circuit and its component gates:
Circuit(C1)∧Arity(C1,3,2)
Gate(X1)∧Type(X1)=XOR
Gate(X2)∧Type(X2)=XOR
Gate(A1)∧Type(A1)=AND
Gate(A2)∧Type(A2)=AND
Gate(O1)∧Type(O1)=OR.
Then we show the connections between them:
Connected(Out(1,X1),In(1,X2))
Connected(In(1,C1),In(1,X1))
Connected(Out(1,X1),In(2,A2))
Connected(In(1,C1),In(1,A1))
Connected(Out(1,A2),In(1,O1))
Connected(In(2,C1),In(2,X1))
Connected(Out(1,A1),In(2,O1))
Connected(In(2,C1),In(2,A1))
Connected(Out(1,X2),Out(1,C1)) Connected(In(3,C1),In(2,X2))
Connected(Out(1,O1),Out(2,C1)) Connected(In(3,C1),In(1,A2)).
Pose queries to the inference procedure
What combinations of inputs would cause the ﬁrst output of C1 (the sum bit) to be 0 and the
second output of C1 (the carry bit) to be 1?
∃i1,i2,i3 Signal(In(1,C1))=i1 ∧Signal(In(2,C1))=i2 ∧Signal(In(3,C1))=i3
∧Signal(Out(1,C1))=0∧Signal(Out(2,C1))=1.
The answers are substitutions for the variables i1, i2, and i3 such that the resulting sentence is
entailed by the knowledge base. ASKVARS will give us three such substitutions:
{i1/1, i2/1, i3/0}
{i1/1, i2/0, i3/1}
{i1/0, i2/1, i3/1}.
What are the possible sets of values of all the terminals for the adder circuit?
∃i1,i2,i3,o1,o2 Signal(In(1,C1))=i1 ∧Signal(In(2,C1))=i2
∧Signal(In(3,C1))=i3 ∧Signal(Out(1,C1))=o1 ∧Signal(Out(2,C1))=o2 .
This ﬁnal query will return a complete input–output table for the device, which can be used
to check that it does in fact add its inputs correctly. This is a simple example of circuit
veriﬁcation. We can also use the deﬁnition of the circuit to build larger digital systems, for
Circuit veriﬁcation
which the same kind of veriﬁcation procedure can be carried out. (See Exercise 8.ADDR.)
Many domains are amenable to the same kind of structured knowledge-base development, in
which more complex concepts are deﬁned on top of simpler concepts.

## Page 295
