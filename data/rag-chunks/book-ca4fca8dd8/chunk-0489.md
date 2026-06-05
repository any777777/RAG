---
chunk_id: "book-ca4fca8dd8-chunk-0489"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 489
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 9
INFERENCE IN FIRST-ORDER LOGIC
In which we deﬁne effective procedures for answering questions posed in ﬁrst-order logic.
In this chapter, we describe algorithms that can answer any answerable ﬁrst-order logic ques-
tion. Section 9.1 introduces inference rules for quantiﬁers and shows how to reduce ﬁrst-order
inference to propositional inference, albeit at potentially great expense. Section 9.2 describes
how uniﬁcation can be used to construct inference rules that work directly with ﬁrst-order
sentences. We then discuss three major families of ﬁrst-order inference algorithms: forward
chaining (Section 9.3), backward chaining (Section 9.4), and resolution-based theorem
proving (Section 9.5).
9.1 Propositional vs. First-Order Inference
One way to do ﬁrst-order inference is to convert the ﬁrst-order knowledge base to proposi-
tional logic and use propositional inference, which we already know how to do. A ﬁrst step
is eliminating universal quantiﬁers. For example, suppose our knowledge base contains the
standard folkloric axiom that all greedy kings are evil:
∀x King(x)∧Greedy(x) ⇒Evil(x).
From that we can infer any of the following sentences:
King(John)∧Greedy(John) ⇒Evil(John)
King(Richard)∧Greedy(Richard) ⇒Evil(Richard)
King(Father(John))∧Greedy(Father(John)) ⇒Evil(Father(John)).
...
In general, the rule of Universal Instantiation (UI for short) says that we can infer any
Universal
Instantiation
sentence obtained by substituting a ground term (a term without variables) for a universally
quantiﬁed variable.1
To write out the inference rule formally, we use the notion of substitutions introduced in
Section 8.3. Let SUBST(θ,α) denote the result of applying the substitution θ to the sentence
α. Then the rule is written
∀v α
SUBST({v/g},α)
for any variable v and ground term g. For example, the three sentences given earlier are
obtained with the substitutions {x/John}, {x/Richard}, and {x/Father(John)}.
1
Do not confuse these substitutions with the extended interpretations used to deﬁne the semantics of quantiﬁers
in Section 8.2.6. The substitution replaces a variable with a term (a piece of syntax) to produce a new sentence,
whereas an interpretation maps a variable to an object in the domain.

## Page 299
