---
chunk_id: "book-ca4fca8dd8-chunk-0458"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 458
confidence: "first-pass"
extraction_method: "structured-local"
---

280
Chapter 8
First-Order Logic
would be equivalent to asserting
Richard the Lionheart is a king∧Richard the Lionheart is a person,
King John is a king∧King John is a person,
Richard’s left leg is a king∧Richard’s left leg is a person,
and so on. Obviously, this does not capture what we want.
Existential quantiﬁcation (∃)
Universal quantiﬁcation makes statements about every object. Similarly, we can make a
statement about some object without naming it, by using an existential quantiﬁer. To say,
Existential quantiﬁer
for example, that King John has a crown on his head, we write
∃x Crown(x)∧OnHead(x,John).
∃x is pronounced “There exists an x such that ...” or “For some x...”.
Intuitively, the sentence ∃x P says that P is true for at least one object x. More precisely,
∃x P is true in a given model if P is true in at least one extended interpretation that assigns x
to a domain element. That is, at least one of the following is true:
Richard the Lionheart is a crown∧Richard the Lionheart is on John’s head;
King John is a crown∧King John is on John’s head;
Richard’s left leg is a crown∧Richard’s left leg is on John’s head;
John’s left leg is a crown∧John’s left leg is on John’s head;
The crown is a crown∧the crown is on John’s head.
The ﬁfth assertion is true in the model, so the original existentially quantiﬁed sentence is
true in the model. Notice that, by our deﬁnition, the sentence would also be true in a model
in which King John was wearing two crowns. This is entirely consistent with the original
sentence “King John has a crown on his head.” 6
Just as ⇒appears to be the natural connective to use with ∀, ∧is the natural connective
to use with ∃. Using ∧as the main connective with ∀led to an overly strong statement in
the example in the previous section; using ⇒with ∃usually leads to a very weak statement,
indeed. Consider the following sentence:
∃x Crown(x) ⇒OnHead(x,John).
On the surface, this might look like a reasonable rendition of our sentence. Applying the
semantics, we see that the sentence says that at least one of the following assertions is true:
Richard the Lionheart is a crown ⇒Richard the Lionheart is on John’s head;
King John is a crown ⇒King John is on John’s head;
Richard’s left leg is a crown ⇒Richard’s left leg is on John’s head;
and so on. An implication is true if both premise and conclusion are true, or if its premise
is false; so if Richard the Lionheart is not a crown, then the ﬁrst assertion is true and the
existential is satisﬁed. So, an existentially quantiﬁed implication sentence is true whenever
any object fails to satisfy the premise; hence such sentences really do not say much at all.
6
There is a variant of the existential quantiﬁer, usually written ∃1 or ∃!, that means “There exists exactly one.”
The same meaning can be expressed using equality statements.
