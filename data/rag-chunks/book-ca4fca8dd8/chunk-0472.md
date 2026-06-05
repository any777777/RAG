---
chunk_id: "book-ca4fca8dd8-chunk-0472"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 472
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 8.3
Using First-Order Logic
287
The domain of sets is also fundamental to mathematics as well as to commonsense rea-
Set
soning. (In fact, it is possible to deﬁne number theory in terms of set theory.) We want to
be able to represent individual sets, including the empty set. We need a way to build up sets
from elements or from operations on other sets. We will want to know whether an element is
a member of a set and we will want to distinguish sets from objects that are not sets.
We will use the normal vocabulary of set theory as syntactic sugar. The empty set is a
constant written as {}. There is one unary predicate, Set, which is true of sets. The binary
predicates are x∈s (x is a member of set s) and s1 ⊆s2 (set s1 is a subset of s2, possibly equal
to s2). The binary functions are s1 ∩s2 (intersection), s1 ∪s2 (union), and Add(x,s) (the set
resulting from adding element x to set s). One possible set of axioms is as follows:
1. The only sets are the empty set and those made by adding something to a set:
∀s Set(s) ⇔(s={})∨(∃x,s2 Set(s2)∧s=Add(x,s2)).
2. The empty set has no elements added into it. In other words, there is no way to decom-
pose {} into a smaller set and an element:
¬∃x,s Add(x,s)={}.
3. Adding an element already in the set has no effect:
∀x,s x∈s ⇔s=Add(x,s).
4. The only members of a set are the elements that were added into it. We express this
recursively, saying that x is a member of s if and only if s is equal to some element y
added to some set s2, where either y is the same as x or x is a member of s2:
∀x,s x∈s ⇔∃y,s2 (s=Add(y,s2)∧(x=y∨x∈s2)).
5. A set is a subset of another set if and only if all of the ﬁrst set’s members are members
of the second set:
∀s1,s2 s1 ⊆s2 ⇔(∀x x∈s1 ⇒x∈s2).
6. Two sets are equal if and only if each is a subset of the other:
∀s1,s2 (s1 =s2) ⇔(s1 ⊆s2 ∧s2 ⊆s1).
7. An object is in the intersection of two sets if and only if it is a member of both sets:
∀x,s1,s2 x∈(s1 ∩s2) ⇔(x∈s1 ∧x∈s2).
8. An object is in the union of two sets if and only if it is a member of either set:
∀x,s1,s2 x∈(s1 ∪s2) ⇔(x∈s1 ∨x∈s2).
Lists are similar to sets. The differences are that lists are ordered and the same element can
List
appear more than once in a list. We can use the vocabulary of Lisp for lists: Nil is the constant
list with no elements; Cons, Append, First, and Rest are functions; and Find is the predicate
that does for lists what Member does for sets. List is a predicate that is true only of lists. As
with sets, it is common to use syntactic sugar in logical sentences involving lists. The empty
list is []. The term Cons(x,Nil) (i.e., the list containing the element x followed by nothing)
is written as [x]. A list of several elements, such as [A,B,C], corresponds to the nested term
Cons(A,Cons(B,Cons(C,Nil))). Exercise 8.LIST asks you to write out the axioms for lists.
