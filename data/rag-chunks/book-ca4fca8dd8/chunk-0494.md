---
chunk_id: "book-ca4fca8dd8-chunk-0494"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 494
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 9.2
Uniﬁcation and First-Order Inference
301
SUBST(θ, pi′)=SUBST(θ, pi), for all i,
p1′, p2′, ..., pn′, (p1 ∧p2 ∧...∧pn ⇒q)
SUBST(θ,q)
.
There are n+1 premises to this rule: the n atomic sentences pi′ and the one implication. The
conclusion is the result of applying the substitution θ to the consequent q. For our example:
p1′ is King(John)
p1 is King(x)
p2′ is Greedy(y)
p2 is Greedy(x)
θ is {x/John,y/John}
q is Evil(x)
SUBST(θ,q) is Evil(John).
It is easy to show that Generalized Modus Ponens is a sound inference rule. First, we observe
that, for any sentence p (whose variables are assumed to be universally quantiﬁed) and for
any substitution θ,
p |= SUBST(θ, p)
is true by Universal Instantiation. It is true in particular for a θ that satisﬁes the conditions of
the Generalized Modus Ponens rule. Thus, from p1′,..., pn′ we can infer
SUBST(θ, p1′)∧...∧SUBST(θ, pn′)
and from the implication p1 ∧...∧pn ⇒q we can infer
SUBST(θ, p1)∧...∧SUBST(θ, pn) ⇒SUBST(θ,q).
Now, θ in Generalized Modus Ponens is deﬁned so that SUBST(θ, pi′)=SUBST(θ, pi), for
all i; therefore the ﬁrst of these two sentences matches the premise of the second exactly.
Hence, SUBST(θ,q) follows by Modus Ponens.
Generalized Modus Ponens is a lifted version of Modus Ponens—it raises Modus Ponens
Lifting
from ground (variable-free) propositional logic to ﬁrst-order logic. We will see in the rest of
this chapter that we can develop lifted versions of the forward chaining, backward chaining,
and resolution algorithms introduced in Chapter 7. The key advantage of lifted inference
rules over propositionalization is that they make only those substitutions that are required to
allow particular inferences to proceed.
9.2.1 Uniﬁcation
Lifted inference rules require ﬁnding substitutions that make different logical expressions
look identical. This process is called uniﬁcation and is a key component of all ﬁrst-order
Uniﬁcation
inference algorithms. The UNIFY algorithm takes two sentences and returns a uniﬁer for
Uniﬁer
them (a substitution) if one exists:
UNIFY(p,q)=θ where SUBST(θ, p)=SUBST(θ,q).
Let us look at some examples of how UNIFY should behave. Suppose we have a query
AskVars(Knows(John,x)): whom does John know? Answers to this query can be found by
ﬁnding all sentences in the knowledge base that unify with Knows(John,x). Here are the
results of uniﬁcation with four different sentences that might be in the knowledge base:
UNIFY(Knows(John,x), Knows(John,Jane)) = {x/Jane}
UNIFY(Knows(John,x), Knows(y,Bill)) = {x/Bill,y/John}
UNIFY(Knows(John,x), Knows(y,Mother(y))) = {y/John,x/Mother(John)}
UNIFY(Knows(John,x), Knows(x,Elizabeth)) = failure.
