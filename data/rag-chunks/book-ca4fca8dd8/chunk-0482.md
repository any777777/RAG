---
chunk_id: "book-ca4fca8dd8-chunk-0482"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 482
confidence: "first-pass"
extraction_method: "structured-local"
---

292
Chapter 8
First-Order Logic
Assemble the relevant knowledge
What do we know about digital circuits? For our purposes, they are composed of wires and
gates. Signals ﬂow along wires to the input terminals of gates, and each gate produces a
signal on the output terminal that ﬂows along another wire. To determine what these signals
will be, we need to know how the gates transform their input signals. There are four types
of gates: AND, OR, and XOR gates have two input terminals, and NOT gates have one. All
gates have one output terminal. Circuits, like gates, have input and output terminals.
To reason about functionality and connectivity, we do not need to talk about the wires
themselves, the paths they take, or the junctions where they come together. All that matters
is the connections between terminals—we can say that one output terminal is connected to
another input terminal without having to say what actually connects them. Other factors such
as the size, shape, color, or cost of the various components are irrelevant to our analysis.
If our purpose were something other than verifying designs at the gate level, the ontology
would be different. For example, if we were interested in debugging faulty circuits, then it
would probably be a good idea to include the wires in the ontology, because a faulty wire can
corrupt the signal ﬂowing along it. For resolving timing faults, we would need to include gate
delays. If we were interested in designing a product that would be proﬁtable, then the cost of
the circuit and its speed relative to other products on the market would be important.
Decide on a vocabulary
We now know that we want to talk about circuits, terminals, signals, and gates. The next
step is to choose functions, predicates, and constants to represent them. First, we need to be
able to distinguish gates from each other and from other objects. Each gate is represented as
an object named by a constant, about which we assert that it is a gate with, say, Gate(X1).
The behavior of each gate is determined by its type: one of the constants AND,OR, XOR,
or NOT. Because a gate has exactly one type, a function is appropriate: Type(X1)=XOR.
Circuits, like gates, are identiﬁed by a predicate: Circuit(C1).
Next we consider terminals, which are identiﬁed by the predicate Terminal(x). A circuit
can have one or more input terminals and one or more output terminals. We use the function
1
2
3
1
2
X1
X2
A1
A2
O1
C1
Figure 8.6 A digital circuit C1, purporting to be a one-bit full adder. The ﬁrst two inputs are
the two bits to be added, and the third input is a carry bit. The ﬁrst output is the sum, and
the second output is a carry bit for the next adder. The circuit contains two XOR gates, two
AND gates, and one OR gate.
