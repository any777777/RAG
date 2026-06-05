---
chunk_id: "book-ca4fca8dd8-chunk-1460"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1460
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 880

880
Chapter 24
Natural Language Processing
Tag
Word
Description
Tag
Word
Description
CC
and
Coordinating conjunction
PRP$
your
Possessive pronoun
CD
three
Cardinal number
RB
quickly
Adverb
DT
the
Determiner
RBR
quicker
Adverb, comparative
EX
there
Existential there
RBS
quickest
Adverb, superlative
FW
per se
Foreign word
RP
off
Particle
IN
of
Preposition
SYM
+
Symbol
JJ
purple
Adjective
TO
to
to
JJR
better
Adjective, comparative
UH
eureka
Interjection
JJS
best
Adjective, superlative
VB
talk
Verb, base form
LS
1
List item marker
VBD
talked
Verb, past tense
MD
should
Modal
VBG
talking
Verb, gerund
NN
kitten
Noun, singular or mass
VBN
talked
Verb, past participle
NNS
kittens
Noun, plural
VBP
talk
Verb, non-3rd-sing
NNP
Ali
Proper noun, singular
VBZ
talks
Verb, 3rd-sing
NNPS
Fords
Proper noun, plural
WDT
which
Wh-determiner
PDT
all
Predeterminer
WP
who
Wh-pronoun
POS
’s
Possessive ending
WP$
whose
Possessive wh-pronoun
PRP
you
Personal pronoun
WRB
where
Wh-adverb
$
$
Dollar sign
#
#
Pound sign
“
‘
Left quote
”
’
Right quote
(
[
Left parenthesis
)
]
Right parenthesis
,
,
Comma
.
!
Sentence end
:
;
Mid-sentence punctuation
Figure 24.1 Part-of-speech tags (with an example word for each tag) for the Penn Treebank
corpus (Marcus et al., 1993). Here “3rd-sing” is an abbreviation for “third person singular
present tense.”
24.1.6 Part-of-speech (POS) tagging
One basic way to categorize words is by their part of speech (POS), also called lexical
Part of speech
(POS)
category or tag: noun, verb, adjective, and so on. Parts of speech allow language models
to capture generalizations such as “adjectives generally come before nouns in English.” (In
other languages, such as French, it is the other way around (generally)).
Everyone agrees that “noun” and “verb” are parts of speech, but when we get into the
details there is no one deﬁnitive list. Figure 24.1 shows the 45 tags used in the Penn Tree-
bank, a corpus of over three million words of text annotated with part-of-speech tags. As we
Penn Treebank
will see later, the Penn Treebank also annotates many sentences with syntactic parse trees,
from which the corpus gets its name. Here is an excerpt saying that “from” is tagged as a
preposition (IN), “the” as a determiner (DT), and so on:
From the start , it
took
a
person with great qualities to
succeed
IN
DT NN
, PRP VBD DT NN
IN
JJ
NNS
TO VB
The task of assigning a part of speech to each word in a sentence is called part-of-speech

## Page 881
