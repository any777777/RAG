---
chunk_id: "book-ca4fca8dd8-chunk-1487"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1487
confidence: "first-pass"
extraction_method: "structured-local"
---

898
Chapter 24
Natural Language Processing
Ambiguity: We tend to think of ambiguity as a failure in communication; when a listener
Ambiguity
is consciously aware of an ambiguity in an utterance, it means that the utterance is unclear or
confusing. Here are some examples taken from newspaper headlines:
Squad helps dog bite victim.
Police begin campaign to run down jaywalkers.
Helicopter powered by human ﬂies.
Once-sagging cloth diaper industry saved by full dumps.
Include your children when baking cookies.
Portable toilet bombed; police have nothing to go on.
Milk drinkers are turning to powder.
Two sisters reunited after 18 years in checkout counter.
Such confusions are the exception; most of the time the language we hear seems unambigu-
ous. Thus, when researchers ﬁrst began to use computers to analyze language in the 1960s,
they were quite surprised to learn that almost every sentence is ambiguous, with multiple
possible parses (sometimes hundreds), even when the single preferred parse is the only one
that native speakers notice. For example, we understand the phrase “brown rice and black
beans” as “[brown rice] and [black beans],” and never consider the low-probability interpre-
tation “brown [rice and black beans],” where the adjective “brown” is modifying the whole
phrase, not just the “rice.” When we hear “Outside of a dog, a book is a person’s best friend,”
we interpret “outside of” as meaning “except for,” and ﬁnd it funny when the next sentence
of the Groucho Marx joke is “Inside of a dog it’s too dark to read.”
Lexical ambiguity is when a word has more than one meaning: “back” can be an adverb
Lexical ambiguity
(go back), an adjective (back door), a noun (the back of the room), a verb (back a candidate),
or a proper noun (a river in Nunavut, Canada). “Jack” can be a proper name, a noun (a playing
card, a six-pointed metal game piece, a nautical ﬂag, a ﬁsh, a bird, a cheese, a socket, etc.), or
a verb (to jack up a car, to hunt with a light, or to hit a baseball hard). Syntactic ambiguity
Syntactic ambiguity
refers to a phrase that has multiple parses: “I smelled a wumpus in 2,2” has two parses: one
where the prepositional phrase “in 2,2” modiﬁes the noun and one where it modiﬁes the verb.
The syntactic ambiguity leads to a semantic ambiguity, because one parse means that the
Semantic ambiguity
wumpus is in 2,2 and the other means that a stench is in 2,2. In this case, getting the wrong
interpretation could be a deadly mistake.
There can also be ambiguity between literal and ﬁgurative meanings. Figures of speech
are important in poetry, and are common in everyday speech as well. A metonymy is a
Metonymy
ﬁgure of speech in which one object is used to stand for another. When we hear “Chrysler
announced a new model,” we do not interpret it as saying that companies can talk; rather
we understand that a spokesperson for the company made the announcement. Metonymy is
common and is often interpreted unconsciously by human hearers.
Unfortunately, our grammar as it is written is not so facile. To handle the semantics of
metonymy properly, we need to introduce a whole new level of ambiguity. We could do
this by providing two objects for the semantic interpretation of every phrase in the sentence:
one for the object that the phrase literally refers to (Chrysler) and one for the metonymic
reference (the spokesperson). We then have to say that there is a relation between the two. In
