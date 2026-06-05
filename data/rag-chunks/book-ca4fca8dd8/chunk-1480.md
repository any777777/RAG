---
chunk_id: "book-ca4fca8dd8-chunk-1480"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1480
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.4
Augmented Grammars
893
S(v) →NP(Sbj,pn,n) VP(pn,v) | ...
NP(c,pn,n) →Pronoun(c,pn,n) | Noun(c,pn,n) | ...
VP(pn,v) →Verb(pn,v) NP(Obj,pn,n) | ...
PP(head) →Prep(head) NP(Obj,pn,h)
Pronoun(Sbj,1S,I) →I
Pronoun(Sbj,1P,we) →we
Pronoun(Obj,1S,me) →me
Pronoun(Obj,3P,them) →them
Verb(3S,see) →see
Figure 24.9 Part of an augmented grammar that handles case agreement, subject–verb agree-
ment, and head words. Capitalized names are constants: Sbj, and Obj for subjective and ob-
jective case; 1S for ﬁrst person singular; 1P and 3P for ﬁrst and third person plural. As usual,
lowercase names are variables. For simplicity, the probabilities have been omitted.
Here P1(v,n) means the probability of a VP headed by v joining with an NP headed by n to
form a VP. We can specify that “ate a banana” is more probable than “ate a bandanna” by
ensuring that P1(ate,banana) > P1(ate,bandanna). Note that since we are considering only
phrase heads, the distinction between “ate a banana” and “ate a rancid banana” will not be
caught by P1. Conceptually, P1 is a huge table of probabilities: if there are 5,000 verbs and
10,000 nouns in the vocabulary, then P1 requires 50 million entries, but most of them will not
be stored explicitly; rather they will be derived from smoothing and backoff. For example,
we can back off from P1(v,n) to a model that depends only on v. Such a model would require
10,000 times fewer parameters, but can still capture important regularities, such as the fact
that a transitive verb like “ate” is more likely to be followed by an NP (regardless of the head)
than an intransitive verb like “sleep.”
We saw in Section 24.2 that the simple grammar for E0 overgenerates, producing non-
sentences such as “I saw she” or “I sees her.” To avoid this problem, our grammar would have
to know that “her,” not “she,” is a valid object of “saw” (or of any other verb) and that “see,”
not “sees,” is the form of the verb that accompanies the subject “I.”
We could encode these facts completely in the probability entries, for example making
P1(v,she) be a very small number, for all verbs v. But it is more concise and modular to
augment the category NP with additional variables: NP(c,pn,n) is used to represent a noun
phrase with case c (subjective or objective), person and number pn (e.g., third person singu-
lar), and head noun n. Figure 24.9 shows an augmented lexicalized grammar that handles
these additional variables. Let’s consider one grammar rule in detail:
S(v) →NP(Sbj,pn,n) VP(pn,v) [P5(n,v)].
This rule says that when an NP is followed by a VP they can form an S, but only if the NP
has the subjective (Sbj) case and the person and number (pn) of the NP and VP are identical.
(We say that they are in agreement.) If that holds, then we have an S whose head is the verb
from the VP. Here is an example lexical rule,
Pronoun(Sbj,1S,I) →I [0.005]
which says that “I” is a Pronoun in the subjective case, ﬁrst-person singular, with head “I.”
