---
chunk_id: "book-ca4fca8dd8-chunk-0474"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 474
confidence: "first-pass"
extraction_method: "structured-local"
---

288
Chapter 8
First-Order Logic
8.3.4 The wumpus world
Some propositional logic axioms for the wumpus world were given in Chapter 7. The ﬁrst-
order axioms in this section are much more concise, capturing in a natural way exactly what
we want to say.
Recall that the wumpus agent receives a percept vector with ﬁve elements. The corre-
sponding ﬁrst-order sentence stored in the knowledge base must include both the percept and
the time at which it occurred; otherwise, the agent will get confused about when it saw what.
We use integers for time steps. A typical percept sentence would be
Percept([Stench,Breeze,Glitter,None,None],5).
Here, Percept is a binary predicate, and Stench and so on are constants placed in a list. The
actions in the wumpus world can be represented by logical terms:
Turn(Right), Turn(Left), Forward, Shoot, Grab, Climb.
To determine which is best, the agent program executes the query
ASKVARS(KB,BestAction(a,5)),
which returns a binding list such as {a/Grab}. The agent program can then return Grab as
the action to take. The raw percept data implies certain facts about the current state. For
example:
∀t,s,g,w,c Percept([s,Breeze,g,w,c],t) ⇒Breeze(t)
∀t,s,g,w,c Percept([s,None,g,w,c],t) ⇒¬Breeze(t)
∀t,s,b,w,c Percept([s,b,Glitter,w,c],t) ⇒Glitter(t)
∀t,s,b,w,c Percept([s,b,None,w,c],t) ⇒¬Glitter(t)
and so on. These rules exhibit a trivial form of the reasoning process called perception,
which we study in depth in Chapter 27. Notice the quantiﬁcation over time t. In propositional
logic, we would need copies of each sentence for each time step.
Simple “reﬂex” behavior can also be implemented by quantiﬁed implication sentences.
For example, we have
∀t Glitter(t) ⇒BestAction(Grab,t).
Given the percept and rules from the preceding paragraphs, this would yield the desired con-
clusion BestAction(Grab,5)—that is, Grab is the right thing to do.
We have represented the agent’s inputs and outputs; now it is time to represent the en-
vironment itself. Let us begin with objects. Obvious candidates are squares, pits, and the
wumpus. We could name each square—Square1,2 and so on—but then the fact that Square1,2
and Square1,3 are adjacent would have to be an “extra” fact, and we would need one such
fact for each pair of squares. It is better to use a complex term in which the row and column
appear as integers; for example, we can simply use the list term [1,2]. Adjacency of any two
squares can be deﬁned as
∀x,y,a,b Adjacent([x,y],[a,b]) ⇔
(x = a∧(y = b−1∨y = b+1))∨(y = b∧(x = a−1∨x = a+1)).
We could name each pit, but this would be inappropriate for a different reason: there is no
