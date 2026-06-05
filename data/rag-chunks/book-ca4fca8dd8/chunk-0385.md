---
chunk_id: "book-ca4fca8dd8-chunk-0385"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 385
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.4
Propositional Logic: A Very Simple Logic
235
KB is true in the real world? (After all, KB is just “syntax” inside the agent’s head.) This is a
philosophical question about which many, many books have been written. (See Chapter 28.)
A simple answer is that the agent’s sensors create the connection. For example, our wumpus-
world agent has a smell sensor. The agent program creates a suitable sentence whenever there
is a smell. Then, whenever that sentence is in the knowledge base, it is true in the real world.
Thus, the meaning and truth of percept sentences are deﬁned by the processes of sensing and
sentence construction that produce them. What about the rest of the agent’s knowledge, such
as its belief that wumpuses cause smells in adjacent squares? This is not a direct represen-
tation of a single percept, but a general rule—derived, perhaps, from perceptual experience
but not identical to a statement of that experience. General rules like this are produced by
a sentence construction process called learning, which is the subject of Part V. Learning is
fallible. It could be the case that wumpuses cause smells except on February 29 in leap years,
which is when they take their baths. Thus, KB may not be true in the real world, but with
good learning procedures, there is reason for optimism.
7.4 Propositional Logic: A Very Simple Logic
We now present propositional logic. We describe its syntax (the structure of sentences) and
Propositional logic
its semantics (the way in which the truth of sentences is determined). From these, we derive
a simple, syntactic algorithm for logical inference that implements the semantic notion of
entailment. Everything takes place, of course, in the wumpus world.
7.4.1 Syntax
The syntax of propositional logic deﬁnes the allowable sentences. The atomic sentences
Atomic sentences
consist of a single proposition symbol. Each such symbol stands for a proposition that can
Proposition symbol
be true or false. We use symbols that start with an uppercase letter and may contain other
letters or subscripts, for example: P, Q, R, W1,3 and FacingEast. The names are arbitrary
but are often chosen to have some mnemonic value—we use W1,3 to stand for the proposition
that the wumpus is in [1,3]. (Remember that symbols such as W1,3 are atomic, i.e., W, 1,
and 3 are not meaningful parts of the symbol.) There are two proposition symbols with
ﬁxed meanings: True is the always-true proposition and False is the always-false proposition.
Complex sentences are constructed from simpler sentences, using parentheses and operators
Complex sentences
called logical connectives. There are ﬁve connectives in common use:
Logical connectives
¬ (not). A sentence such as ¬W1,3 is called the negation of W1,3. A literal is either an
Negation
Literal
atomic sentence (a positive literal) or a negated atomic sentence (a negative literal).
∧(and). A sentence whose main connective is ∧, such as W1,3 ∧P3,1, is called a conjunc-
tion; its parts are the conjuncts. (The ∧looks like an “A” for “And.”)
Conjunction
∨(or). A sentence whose main connective is ∨, such as (W1,3 ∧P3,1)∨W2,2, is a disjunc-
tion; its parts are disjuncts—in this example, (W1,3 ∧P3,1) and W2,2.
Disjunction
⇒(implies). A sentence such as (W1,3 ∧P3,1) ⇒¬W2,2 is called an implication (or con-
Implication
ditional). Its premise or antecedent is (W1,3 ∧P3,1), and its conclusion or consequent
Premise
Conclusion
is ¬W2,2. Implications are also known as rules or if–then statements. The implication
Rules
symbol is sometimes written in other books as ⊃or →.
⇔(if and only if). The sentence W1,3 ⇔¬W2,2 is a biconditional.
Biconditional
