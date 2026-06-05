---
chunk_id: "book-ca4fca8dd8-chunk-0496"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 496
confidence: "first-pass"
extraction_method: "structured-local"
---

302
Chapter 9
Inference in First-Order Logic
The last uniﬁcation fails because x cannot take on the values John and Elizabeth at the same
time. Now, remember that Knows(x,Elizabeth) means “Everyone knows Elizabeth,” so we
should be able to infer that John knows Elizabeth. The problem arises only because the two
sentences happen to use the same variable name, x. The problem can be avoided by stan-
dardizing apart one of the two sentences being uniﬁed, which means renaming its variables
Standardizing apart
to avoid name clashes. For example, we can rename x in Knows(x,Elizabeth) to x17 (a new
variable name) without changing its meaning. Now the uniﬁcation will work:
UNIFY(Knows(John,x), Knows(x17,Elizabeth)) = {x/Elizabeth,x17/John}.
Exercise 9.STAN delves further into the need for standardizing apart.
There is one more complication: we said that UNIFY should return a substitution that
makes the two arguments look the same. But there could be more than one such uniﬁer.
For example, UNIFY(Knows(John,x),Knows(y,z)) could return {y/John,x/z} or could re-
turn {y/John,x/John,z/John}. The ﬁrst uniﬁer gives Knows(John,z) as the result of uniﬁca-
tion, whereas the second gives Knows(John,John). The second result could be obtained from
the ﬁrst by an additional substitution {z/John}; we say that the ﬁrst uniﬁer is more general
than the second, because it places fewer restrictions on the values of the variables.
Every uniﬁable pair of expressions has a single most general uniﬁer (MGU) that is
Most general uniﬁer
(MGU)
unique up to renaming and substitution of variables. For example, {x/John} and {y/John}
are considered equivalent, as are {x/John,y/John} and {x/John,y/x}.
An algorithm for computing most general uniﬁers is shown in Figure 9.1. The process
is simple: recursively explore the two expressions simultaneously “side by side,” building
up a uniﬁer along the way, but failing if two corresponding points in the structures do not
match. There is one expensive step: when matching a variable against a complex term,
one must check whether the variable itself occurs inside the term; if it does, the match fails
because no consistent uniﬁer can be constructed. For example, S(x) can’t unify with S(S(x)).
This so-called occur check makes the complexity of the entire algorithm quadratic in the
Occur check
size of the expressions being uniﬁed. Some systems, including many logic programming
systems, simply omit the occur check and put the onus on the user to avoid making unsound
inferences as a result. Other systems use more complex uniﬁcation algorithms with linear-
time complexity.
9.2.2 Storage and retrieval
Underlying the TELL, ASK, and ASKVARS functions used to inform and interrogate a knowl-
edge base are the more primitive STORE and FETCH functions. STORE(s) stores a sentence s
into the knowledge base and FETCH(q) returns all uniﬁers such that the query q uniﬁes with
some sentence in the knowledge base. The problem we used to illustrate uniﬁcation—ﬁnding
all facts that unify with Knows(John,x)—is an instance of FETCHing.
The simplest way to implement STORE and FETCH is to keep all the facts in one long
list and unify each query against every element of the list. Such a process is inefﬁcient, but it
works. The remainder of this section outlines ways to make retrieval more efﬁcient.
We can make FETCH more efﬁcient by ensuring that uniﬁcations are attempted only with
sentences that have some chance of unifying. For example, there is no point in trying to unify
Knows(John,x) with Brother(Richard,John). We can avoid such uniﬁcations by indexing
Indexing
the facts in the knowledge base. A simple scheme called predicate indexing puts all the
Predicate indexing
