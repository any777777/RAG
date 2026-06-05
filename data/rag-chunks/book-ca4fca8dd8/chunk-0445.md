---
chunk_id: "book-ca4fca8dd8-chunk-0445"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 445
confidence: "first-pass"
extraction_method: "structured-local"
---

272
Chapter 8
First-Order Logic
8.1.2 Combining the best of formal and natural languages
We can adopt the foundation of propositional logic—a declarative, compositional semantics
that is context-independent and unambiguous—and build a more expressive logic on that
foundation, borrowing representational ideas from natural language while avoiding its draw-
backs. When we look at the syntax of natural language, the most obvious elements are nouns
and noun phrases that refer to objects (squares, pits, wumpuses) and verbs and verb phrases
Object
along with adjectives and adverbs that refer to relations among objects (is breezy, is ad-
Relation
jacent to, shoots). Some of these relations are functions—relations in which there is only
Function
one “value” for a given “input.” It is easy to start listing examples of objects, relations, and
functions:
• Objects: people, houses, numbers, theories, Ronald McDonald, colors, baseball games,
wars, centuries ...
• Relations: these can be unary relations or properties such as red, round, bogus, prime,
Property
multistoried ..., or more general n-ary relations such as brother of, bigger than, inside,
part of, has color, occurred after, owns, comes between, ...
• Functions: father of, best friend, third inning of, one more than, beginning of ...
Indeed, almost any assertion can be thought of as referring to objects and properties or rela-
tions. Some examples follow:
• “One plus two equals three.”
Objects: one, two, three, one plus two; Relation: equals; Function: plus. (“One plus
two” is a name for the object that is obtained by applying the function “plus” to the
objects “one” and “two.” “Three” is another name for this object.)
• “Squares neighboring the wumpus are smelly.”
Objects: wumpus, squares; Property: smelly; Relation: neighboring.
• “Evil King John ruled England in 1200.”
Objects: John, England, 1200; Relation: ruled during; Properties: evil, king.
The language of ﬁrst-order logic, whose syntax and semantics we deﬁne in the next section,
is built around objects and relations. It has been important to mathematics, philosophy, and
artiﬁcial intelligence precisely because those ﬁelds—and indeed, much of everyday human
existence—can be usefully thought of as dealing with objects and the relations among them.
First-order logic can also express facts about some or all of the objects in the universe. This
enables one to represent general laws or rules, such as the statement “Squares neighboring
the wumpus are smelly.”
The primary difference between propositional and ﬁrst-order logic lies in the ontological
commitment made by each language—that is, what it assumes about the nature of reality.
Ontological
commitment
Mathematically, this commitment is expressed through the nature of the formal models with
respect to which the truth of sentences is deﬁned. For example, propositional logic assumes
that there are facts that either hold or do not hold in the world. Each fact can be in one of two
states—true or false—and each model assigns true or false to each proposition symbol (see
Section 7.4.2). First-order logic assumes more; namely, that the world consists of objects with
certain relations among them that do or do not hold. (See Figure 8.1.) The formal models are
correspondingly more complicated than those for propositional logic.
