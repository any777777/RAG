---
chunk_id: "book-ca4fca8dd8-chunk-0386"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 386
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 236

236
Chapter 7
Logical Agents
Sentence
→
AtomicSentence | ComplexSentence
AtomicSentence
→
True | False | P | Q | R | ...
ComplexSentence
→
( Sentence )
|
¬ Sentence
|
Sentence ∧Sentence
|
Sentence ∨Sentence
|
Sentence ⇒Sentence
|
Sentence ⇔Sentence
OPERATOR PRECEDENCE
:
¬,∧,∨,⇒,⇔
Figure 7.7 A BNF (Backus–Naur Form) grammar of sentences in propositional logic, along
with operator precedences, from highest to lowest.
Figure 7.7 gives a formal grammar of propositional logic. (BNF notation is explained on
page 1081.) The BNF grammar is augmented with an operator precedence list to remove am-
biguity when multiple operators are used. The “not” operator (¬) has the highest precedence,
which means that in the sentence ¬A ∧B the ¬ binds most tightly, giving us the equivalent
of (¬A)∧B rather than ¬(A∧B). (The notation for ordinary arithmetic is the same: −2+4
is 2, not –6.) When appropriate, we also use parentheses and square brackets to clarify the
intended sentence structure and improve readability.
7.4.2 Semantics
Having speciﬁed the syntax of propositional logic, we now specify its semantics. The se-
mantics deﬁnes the rules for determining the truth of a sentence with respect to a particular
model. In propositional logic, a model simply sets the truth value—true or false—for every
Truth value
proposition symbol. For example, if the sentences in the knowledge base make use of the
proposition symbols P1,2, P2,2, and P3,1, then one possible model is
m1 = {P1,2 =false, P2,2 =false, P3,1 =true}.
With three proposition symbols, there are 23 =8 possible models—exactly those depicted
in Figure 7.5. Notice, however, that the models are purely mathematical objects with no
necessary connection to wumpus worlds. P1,2 is just a symbol; it might mean “there is a pit
in [1,2]” or “I’m in Paris today and tomorrow.”
The semantics for propositional logic must specify how to compute the truth value of any
sentence, given a model. This is done recursively. All sentences are constructed from atomic
sentences and the ﬁve connectives; therefore, we need to specify how to compute the truth
of atomic sentences and how to compute the truth of sentences formed with each of the ﬁve
connectives. Atomic sentences are easy:
• True is true in every model and False is false in every model.
• The truth value of every other proposition symbol must be speciﬁed directly in the
model. For example, in the model m1 given earlier, P1,2 is false.

## Page 237
