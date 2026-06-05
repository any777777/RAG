---
chunk_id: "book-ca4fca8dd8-chunk-0558"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 558
confidence: "first-pass"
extraction_method: "structured-local"
---

338
Chapter 10
Knowledge Representation
Natural Kinds
Some categories have strict deﬁnitions: an object is a triangle if and only if it is
a polygon with three sides. On the other hand, most categories in the real world
have no clear-cut deﬁnition; these are called natural kind categories. For example,
tomatoes tend to be a dull scarlet; roughly spherical; with an indentation at the top
where the stem was; about two to four inches in diameter; with a thin but tough
skin; and with ﬂesh, seeds, and juice inside. However, there is variation: some
tomatoes are yellow or orange, unripe tomatoes are green, some are smaller or
larger than average, and cherry tomatoes are uniformly small. Rather than having
a complete deﬁnition of tomatoes, we have a set of features that serves to identify
objects that are clearly typical tomatoes, but might not deﬁnitively identify other
objects. (Could there be a tomato that is fuzzy like a peach?)
This poses a problem for a logical agent. The agent cannot be sure that an
object it has perceived is a tomato, and even if it were sure, it could not be cer-
tain which of the properties of typical tomatoes this one has. This problem is an
inevitable consequence of operating in partially observable environments.
One useful approach is to separate what is true of all instances of a category
from what is true only of typical instances. So in addition to the category Tomatoes,
we will also have the category Typical(Tomatoes). Here, the Typical function maps
a category to the subclass that contains only typical instances:
Typical(c) ⊆c.
Most knowledge about natural kinds will actually be about their typical instances:
x∈Typical(Tomatoes) ⇒Red(x)∧Round(x).
Thus, we can write down useful facts about categories without exact deﬁni-
tions. The difﬁculty of providing exact deﬁnitions for most natural categories was
explained in depth by Wittgenstein (1953). He used the example of games to show
that members of a category shared “family resemblances” rather than necessary
and sufﬁcient characteristics: what strict deﬁnition encompasses chess, tag, soli-
taire, and dodgeball?
The utility of the notion of strict deﬁnition was also challenged by
Quine (1953). He pointed out that even the deﬁnition of “bachelor” as an un-
married adult male is suspect; one might, for example, question a statement such
as “the Pope is a bachelor.” While not strictly false, this usage is certainly infe-
licitous because it induces unintended inferences on the part of the listener. The
tension could perhaps be resolved by distinguishing between logical deﬁnitions
suitable for internal knowledge representation and the more nuanced criteria for
felicitous linguistic usage. The latter may be achieved by “ﬁltering” the assertions
derived from the former. It is also possible that failures of linguistic usage serve as
feedback for modifying internal deﬁnitions, so that ﬁltering becomes unnecessary.
