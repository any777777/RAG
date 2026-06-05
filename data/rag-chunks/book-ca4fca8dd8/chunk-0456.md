---
chunk_id: "book-ca4fca8dd8-chunk-0456"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 456
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 8.2
Syntax and Semantics of First-Order Logic
279
are persons” are the bread and butter of ﬁrst-order logic. We deal with the ﬁrst of these in
Section 8.3. The second rule, “All kings are persons,” is written in ﬁrst-order logic as
∀x King(x) ⇒Person(x).
The universal quantiﬁer ∀is usually pronounced “For all ...”. (Remember that the upside-
Universal quantiﬁer
down A stands for “all.”) Thus, the sentence says, “For all x, if x is a king, then x is a person.”
The symbol x is called a variable. By convention, variables are lowercase letters. A variable
Variable
is a term all by itself, and as such can also serve as the argument of a function—for example,
LeftLeg(x). A term with no variables is called a ground term.
Ground term
Intuitively, the sentence ∀x P, where P is any logical sentence, says that P is true for every
object x. More precisely, ∀x P is true in a given model if P is true in all possible extended
interpretations constructed from the interpretation given in the model, where each extended
Extended
interpretation
interpretation speciﬁes a domain element to which x refers.
This sounds complicated, but it is really just a careful way of stating the intuitive mean-
ing of universal quantiﬁcation. Consider the model shown in Figure 8.2 and the intended
interpretation that goes with it. We can extend the interpretation in ﬁve ways:
x →Richard the Lionheart,
x →King John,
x →Richard’s left leg,
x →John’s left leg,
x →the crown.
The universally quantiﬁed sentence ∀x King(x) ⇒Person(x) is true in the original model if
the sentence King(x) ⇒Person(x) is true under each of the ﬁve extended interpretations. That
is, the universally quantiﬁed sentence is equivalent to asserting the following ﬁve sentences:
Richard the Lionheart is a king ⇒Richard the Lionheart is a person.
King John is a king ⇒King John is a person.
Richard’s left leg is a king ⇒Richard’s left leg is a person.
John’s left leg is a king ⇒John’s left leg is a person.
The crown is a king ⇒the crown is a person.
Let us look carefully at this set of assertions. Since, in our model, King John is the only
king, the second sentence asserts that he is a person, as we would hope. But what about
the other four sentences, which appear to make claims about legs and crowns? Is that part
of the meaning of “All kings are persons”? In fact, the other four assertions are true in the
model, but make no claim whatsoever about the personhood qualiﬁcations of legs, crowns,
or indeed Richard. This is because none of these objects is a king. Looking at the truth table
for ⇒(Figure 7.8 on page 237), we see that the implication is true whenever its premise is
false—regardless of the truth of the conclusion. Thus, by asserting the universally quantiﬁed
sentence, which is equivalent to asserting a whole list of individual implications, we end up
asserting the conclusion of the rule just for those objects for which the premise is true and
saying nothing at all about those objects for which the premise is false. Thus, the truth-table
deﬁnition of ⇒turns out to be perfect for writing general rules with universal quantiﬁers.
A common mistake, made frequently even by diligent readers who have read this para-
graph several times, is to use conjunction instead of implication. The sentence
∀x King(x)∧Person(x)
