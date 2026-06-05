---
chunk_id: "book-ca4fca8dd8-chunk-0470"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 470
confidence: "first-pass"
extraction_method: "structured-local"
---

286
Chapter 8
First-Order Logic
answered. If all goes well, the answers to these questions will then be theorems that follow
from the axioms.
Often, one ﬁnds that the expected answers are not forthcoming—for example, from
Spouse(Jim,Laura) one expects (under the laws of many countries) to be able to infer that
¬Spouse(George,Laura); but this does not follow from the axioms given earlier—even after
we add Jim ̸= George as suggested in Section 8.2.8. This is a sign that an axiom is missing.
Exercise 8.HILL asks the reader to supply it.
8.3.3 Numbers, sets, and lists
Numbers are perhaps the most vivid example of how a large theory can be built up from
a tiny kernel of axioms. We describe here the theory of natural numbers or nonnegative
Natural numbers
integers. We need a predicate NatNum that will be true of natural numbers; we need one
constant symbol, 0; and we need one function symbol, S (successor). The Peano axioms
Peano axioms
deﬁne natural numbers and addition.8 Natural numbers are deﬁned recursively:
NatNum(0).
∀n NatNum(n) ⇒NatNum(S(n)).
That is, 0 is a natural number, and for every object n, if n is a natural number, then S(n) is a
natural number. So the natural numbers are 0, S(0), S(S(0)), and so on. We also need axioms
to constrain the successor function:
∀n 0 ̸= S(n).
∀m,n m ̸= n ⇒S(m) ̸= S(n).
Now we can deﬁne addition in terms of the successor function:
∀m NatNum(m) ⇒+(0,m) = m.
∀m,n NatNum(m)∧NatNum(n) ⇒+(S(m),n) = S(+(m,n)).
The ﬁrst of these axioms says that adding 0 to any natural number m gives m itself. Notice
the use of the binary function symbol “+” in the term +(m,0); in ordinary mathematics, the
term would be written m+0 using inﬁx notation. (The notation we have used for ﬁrst-order
Inﬁx
logic is called preﬁx.) To make our sentences about numbers easier to read, we allow the use
Preﬁx
of inﬁx notation. We can also write S(n) as n+1, so the second axiom becomes
∀m,n NatNum(m)∧NatNum(n) ⇒(m+1)+n = (m+n)+1.
This axiom reduces addition to repeated application of the successor function.
The use of inﬁx notation is an example of syntactic sugar, that is, an extension to or
Syntactic sugar
abbreviation of the standard syntax that does not change the semantics. Any sentence that
uses sugar can be “desugared” to produce an equivalent sentence in ordinary ﬁrst-order logic.
Another example is using square brackets rather than parentheses to make it easier to see what
left bracket matches with what right bracket. Yet another example is collapsing quantiﬁers:
replacing ∀x ∀y P(x,y) with ∀x,y P(x,y).
Once we have addition, it is straightforward to deﬁne multiplication as repeated addition,
exponentiation as repeated multiplication, integer division and remainders, prime numbers,
and so on. Thus, the whole of number theory (including cryptography) can be built up from
one constant, one function, one predicate and four axioms.
8
The Peano axioms also include the principle of induction, which is a sentence of second-order logic rather
than of ﬁrst-order logic. The importance of this distinction is explained in Chapter 9.
