---
chunk_id: "book-ca4fca8dd8-chunk-0439"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 439
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 8
FIRST-ORDER LOGIC
In which we notice that the world is blessed with many objects, some of which are related
to other objects, and in which we endeavor to reason about them.
Propositional logic sufﬁced to illustrate the basic concepts of logic, inference, and knowledge-
based agents. Unfortunately, propositional logic is limited in what it can say. In this chap-
ter, we examine ﬁrst-order logic,1 which can concisely represent much more. We begin in
First-order logic
Section 8.1 with a discussion of representation languages in general; Section 8.2 covers the
syntax and semantics of ﬁrst-order logic; Sections 8.3 and 8.4 illustrate the use of ﬁrst-order
logic for simple representations.
8.1 Representation Revisited
In this section, we discuss the nature of representation languages. Programming languages
(such as C++ or Java or Python) are the largest class of formal languages in common use.
Data structures within programs can be used to represent facts; for example, a program could
use a 4 × 4 array to represent the contents of the wumpus world. Thus, the programming
language statement World[2,2]←Pit is a fairly natural way to assert that there is a pit in
square [2,2]. Putting together a string of such statements is sufﬁcient for running a simulation
of the wumpus world.
What programming languages lack is a general mechanism for deriving facts from other
facts; each update to a data structure is done by a domain-speciﬁc procedure whose details
are derived by the programmer from his or her own knowledge of the domain. This proce-
dural approach can be contrasted with the declarative nature of propositional logic, in which
knowledge and inference are separate, and inference is entirely domain independent. SQL
databases take a mix of declarative and procedural knowledge.
A second drawback of data structures in programs (and of databases) is the lack of any
easy way to say, for example, “There is a pit in [2,2] or [3,1]” or “If the wumpus is in [1,1]
then he is not in [2,2].” Programs can store a single value for each variable, and some systems
allow the value to be “unknown,” but they lack the expressiveness required to directly handle
partial information.
Propositional logic is a declarative language because its semantics is based on a truth
relation between sentences and possible worlds. It also has sufﬁcient expressive power to
deal with partial information, using disjunction and negation. Propositional logic has a third
property that is desirable in representation languages, namely, compositionality. In a com-
Compositionality
positional language, the meaning of a sentence is a function of the meaning of its parts. For
1
First-order logic is also called ﬁrst-order predicate calculus; it may be abbreviated as FOL or FOPC.
