---
chunk_id: "book-ca4fca8dd8-chunk-0501"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 501
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 305

Section 9.3
Forward Chaining
305
als can include variables, so Greedy(y) is interpreted as “everyone is greedy” (the universal
quantiﬁer is implicit).
Let us put deﬁnite clauses to work in representing the following problem:
The law says that it is a crime for an American to sell weapons to hostile nations. The
country Nono, an enemy of America, has some missiles, and all of its missiles were sold
to it by Colonel West, who is American.
First, we will represent these facts as ﬁrst-order deﬁnite clauses:
“... it is a crime for an American to sell weapons to hostile nations”:
American(x)∧Weapon(y)∧Sells(x,y,z)∧Hostile(z) ⇒Criminal(x).
(9.3)
“Nono ... has some missiles.” The sentence ∃x Owns(Nono,x) ∧Missile(x) is transformed
into two deﬁnite clauses by Existential Instantiation, introducing a new constant M1:
Owns(Nono,M1)
(9.4)
Missile(M1)
.
(9.5)
“All of its missiles were sold to it by Colonel West”:
Missile(x)∧Owns(Nono,x) ⇒Sells(West,x,Nono).
(9.6)
We will also need to know that missiles are weapons:
Missile(x) ⇒Weapon(x)
(9.7)
and we must know that an enemy of America counts as “hostile”:
Enemy(x,America) ⇒Hostile(x).
(9.8)
“West, who is American ...”:
American(West).
(9.9)
“The country Nono, an enemy of America ...”:
Enemy(Nono,America).
(9.10)
This knowledge base happens to be a Datalog knowledge base: Datalog is a language con-
Datalog
sisting of ﬁrst-order deﬁnite clauses with no function symbols. Datalog gets its name because
it can represent the type of statements typically made in relational databases. The absence of
function symbols makes inference much easier.
9.3.2 A simple forward-chaining algorithm
Figure 9.3 shows a simple forward chaining inference algorithm. Starting from the known
facts, it triggers all the rules whose premises are satisﬁed, adding their conclusions to the
known facts. The process repeats until the query is answered (assuming that just one answer
is required) or no new facts are added. Notice that a fact is not “new” if it is just a renaming
Renaming
of a known fact—a sentence is a renaming of another if they are identical except for the names
of the variables. For example, Likes(x,IceCream) and Likes(y,IceCream) are renamings of
each other. They both mean the same thing: “Everyone likes ice cream.”
We use our crime problem to illustrate FOL-FC-ASK. The implication sentences avail-
able for chaining are (9.3), (9.6), (9.7), and (9.8). Two iterations are required:

## Page 306
