---
chunk_id: "book-ca4fca8dd8-chunk-0417"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 417
confidence: "first-pass"
extraction_method: "structured-local"
---

256
Chapter 7
Logical Agents
We began collecting axioms in Section 7.4.3. The agent knows that the starting square
contains no pit (¬P1,1) and no wumpus (¬W1,1). Furthermore, for each square, it knows that
the square is breezy if and only if a neighboring square has a pit; and a square is smelly if and
only if a neighboring square has a wumpus. Thus, we include a large collection of sentences
of the following form:
B1,1 ⇔(P1,2 ∨P2,1)
S1,1 ⇔(W1,2 ∨W2,1)
···
The agent also knows that there is exactly one wumpus. This is expressed in two parts. First,
we have to say that there is at least one wumpus:
W1,1 ∨W1,2 ∨···∨W4,3 ∨W4,4 .
Then we have to say that there is at most one wumpus. For each pair of locations, we add a
sentence saying that at least one of them must be wumpus-free:
¬W1,1 ∨¬W1,2
¬W1,1 ∨¬W1,3
···
¬W4,3 ∨¬W4,4 .
So far, so good. Now let’s consider the agent’s percepts. We are using S1,1 to mean there is
a stench in [1,1]; can we use a single proposition, Stench to mean that the agent perceives
a stench? Unfortunately we can’t: if there was no stench at the previous time step, then
¬Stench would already be asserted, and the new assertion would simply result in a contra-
diction. The problem is solved when we realize that a percept asserts something only about
the current time. Thus, if the time step (as supplied to MAKE-PERCEPT-SENTENCE in Fig-
ure 7.1) is 4, then we add Stench4 to the knowledge base, rather than Stench—neatly avoiding
any contradiction with ¬Stench3. The same goes for the breeze, bump, glitter, and scream
percepts.
The idea of associating propositions with time steps extends to any aspect of the world
that changes over time. For example, the initial knowledge base includes L0
1,1—the agent is in
square [1,1] at time 0—as well as FacingEast0, HaveArrow0, and WumpusAlive0. We use the
noun ﬂuent (from the Latin ﬂuens, ﬂowing) to refer to an aspect of the world that changes.
Fluent
“Fluent” is a synonym for “state variable,” in the sense described in the discussion of factored
representations in Section 2.4.7 on page 76. Symbols associated with permanent aspects of
the world do not need a time superscript and are sometimes called atemporal variables.
Atemporal variable
We can connect stench and breeze percepts directly to the properties of the squares where
they are experienced as follows.11 For any time step t and any square [x,y], we assert
Lt
x,y ⇒(Breezet ⇔Bx,y)
Lt
x,y ⇒(Stencht ⇔Sx,y).
Now, of course, we need axioms that allow the agent to keep track of ﬂuents such as Lt
x,y.
These ﬂuents change as the result of actions taken by the agent, so, in the terminology of
Chapter 3, we need to write down the transition model of the wumpus world as a set of
logical sentences.
11 Section 7.4.3 conveniently glossed over this requirement.
