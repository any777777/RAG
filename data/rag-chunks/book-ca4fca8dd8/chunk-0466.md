---
chunk_id: "book-ca4fca8dd8-chunk-0466"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 466
confidence: "first-pass"
extraction_method: "structured-local"
---

284
Chapter 8
First-Order Logic
person, and all kings are persons:
TELL(KB, King(John)).
TELL(KB, Person(Richard)).
TELL(KB, ∀x King(x) ⇒Person(x)).
We can ask questions of the knowledge base using ASK. For example,
ASK(KB, King(John))
returns true. Questions asked with ASK are called queries or goals. Generally speaking, any
query that is logically entailed by the knowledge base should be answered afﬁrmatively. For
example, given the three assertions above, the query
ASK(KB, Person(John))
should also return true. We can ask quantiﬁed queries, such as
ASK(KB, ∃x Person(x)).
The answer is true, but this is perhaps not as helpful as we would like. It is rather like
answering “Can you tell me the time?” with “Yes.” If we want to know what value of x
makes the sentence true, we will need a different function, which we call ASKVARS,
ASKVARS(KB,Person(x))
and which yields a stream of answers. In this case there will be two answers: {x/John}
and {x/Richard}. Such an answer is called a substitution or binding list. ASKVARS is
Substitution
Binding list
usually reserved for knowledge bases consisting solely of Horn clauses, because in such
knowledge bases every way of making the query true will bind the variables to speciﬁc values.
That is not the case with ﬁrst-order logic; in a KB that has been told only that King(John)∨
King(Richard) there is no single binding to x that makes the query ∃x King(x) true, even
though the query is in fact true.
8.3.2 The kinship domain
The ﬁrst example we consider is the domain of family relationships, or kinship. This domain
includes facts such as “Elizabeth is the mother of Charles” and “Charles is the father of
William” and rules such as “One’s grandmother is the mother of one’s parent.”
Clearly, the objects in our domain are people. Unary predicates include Male and Female,
among others. Kinship relations—parenthood, brotherhood, marriage, and so on—are repre-
sented by binary predicates: Parent, Sibling, Brother, Sister, Child, Daughter, Son, Spouse,
Wife, Husband, Grandparent, Grandchild, Cousin, Aunt, and Uncle. We use functions for
Mother and Father, because every person has exactly one of each of these, biologically (al-
though we could introduce additional functions for adoptive mothers, surrogate mothers, etc.).
We can go through each function and predicate, writing down what we know in terms of
the other symbols. For example, one’s mother is one’s parent who is female:
∀m,c Mother(c)=m ⇔Female(m)∧Parent(m,c).
One’s husband is one’s male spouse:
∀w,h Husband(h,w) ⇔Male(h)∧Spouse(h,w).
Parent and child are inverse relations:
∀p,c Parent(p,c) ⇔Child(c, p).
