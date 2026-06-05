---
chunk_id: "book-ca4fca8dd8-chunk-0441"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 441
confidence: "first-pass"
extraction_method: "structured-local"
---

270
Chapter 8
First-Order Logic
example, the meaning of “S1,4 ∧S1,2” is related to the meanings of “S1,4” and “S1,2.” It would
be very strange if “S1,4” meant that there is a stench in square [1,4] and “S1,2” meant that
there is a stench in square [1,2], but “S1,4 ∧S1,2” meant that France and Poland drew 1–1 in
last week’s ice hockey qualifying match.
However, propositional logic, as a factored representation, lacks the expressive power to
concisely describe an environment with many objects. For example, we were forced to write
a separate rule about breezes and pits for each square, such as
B1,1 ⇔(P1,2 ∨P2,1).
In English, on the other hand, it seems easy enough to say, once and for all, “Squares adjacent
to pits are breezy.” The syntax and semantics of English make it possible to describe the
environment concisely: English, like ﬁrst-order logic, is a structured representation.
8.1.1 The language of thought
Natural languages (such as English or Spanish) are very expressive indeed. We managed
to write almost this whole book in natural language, with only occasional lapses into other
languages (mainly mathematics and diagrams). There is a long tradition in linguistics and
the philosophy of language that views natural language as a declarative knowledge represen-
tation language. If we could uncover the rules for natural language, we could use them in
representation and reasoning systems and gain the beneﬁt of the billions of pages that have
been written in natural language.
The modern view of natural language is that it serves as a medium for communication
rather than pure representation. When a speaker points and says, “Look!” the listener comes
to know that, say, Superman has ﬁnally appeared over the rooftops. Yet we would not want
to say that the sentence “Look!” represents that fact. Rather, the meaning of the sentence
depends both on the sentence itself and on the context in which the sentence was spoken.
Clearly, one could not store a sentence such as “Look!” in a knowledge base and expect to
recover its meaning without also storing a representation of the context—which raises the
question of how the context itself can be represented.
Natural languages also suffer from ambiguity, a problem for a representation language.
As Pinker (1995) puts it: “When people think about spring, surely they are not confused as
to whether they are thinking about a season or something that goes boing—and if one word
can correspond to two thoughts, thoughts can’t be words.”
The famous Sapir–Whorf hypothesis (Whorf, 1956) claims that our understanding of
the world is strongly inﬂuenced by the language we speak. It is certainly true that different
speech communities divide up the world differently. The French have two words “chaise” and
“fauteuil,” for a concept that English speakers cover with one: “chair.” But English speakers
can easily recognize the category fauteuil and give it a name—roughly “open-arm chair”—so
does language really make a difference? Whorf relied mainly on intuition and speculation,
and his ideas have been largely dismissed, but in the intervening years we actually have real
data from anthropological, psychological, and neurological studies.
For example, can you remember which of the following two phrases formed the opening
of Section 8.1?
“In this section, we discuss the nature of representation languages ...”
“This section covers the topic of knowledge representation languages ...”
