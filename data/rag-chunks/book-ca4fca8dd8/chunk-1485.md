---
chunk_id: "book-ca4fca8dd8-chunk-1485"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1485
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.5
Complications of Real Natural Language
897
One standard approach to quantiﬁcation is for the grammar to deﬁne not an actual logical
semantic sentence, but rather a quasi-logical form that is then turned into a logical sentence
Quasi-logical form
by algorithms outside of the parsing process. Those algorithms can have preference rules for
choosing one quantiﬁer scope over another—preferences that need not be reﬂected directly
in the grammar.
Pragmatics: We have shown how an agent can perceive a string of words and use a
Pragmatics
grammar to derive a set of possible semantic interpretations. Now we address the problem
of completing the interpretation by adding context-dependent information about the current
situation. The most obvious need for pragmatic information is in resolving the meaning of
indexicals, which are phrases that refer directly to the current situation. For example, in the
Indexical
sentence “I am in Boston today,” both “I” and “today” are indexicals. The word “I” would
be represented by Speaker, a ﬂuent that refers to different objects at different times, and it
would be up to the hearer to resolve the referent of the ﬂuent—that is not considered part of
the grammar but rather an issue of pragmatics.
Another part of pragmatics is interpreting the speaker’s intent. The speaker’s utterance
is considered a speech act, and it is up to the hearer to decipher what type of action it is—a
Speech act
question, a statement, a promise, a warning, a command, and so on. A command such as
“go to 2 2” implicitly refers to the hearer. So far, our grammar for S covers only declarative
sentences. We can extend it to cover commands—a command is a verb phrase where the
subject is implicitly the hearer of the command:
S(Command(pred(Hearer))) →VP(pred).
Long-distance dependencies: In Figure 24.8 we saw that “she didn’t hear or even see
Long-distance
dependencies
him” was parsed with two gaps where an NP is missing, but refers to the NP “him.” We can
use the symbol
to represent the gaps: “she didn’t [hear
or even see ] him.” In general,
the distance between the gap and the NP it refers to can be arbitrarily long: in “Who did the
agent tell you to give the gold to ?” the gap refers to “Who,” which is 11 words away.
A complex system of augmented rules can be used to make sure that the missing NPs
match up properly. The rules are complex; for example, you can’t have a gap in one branch
of an NP conjunction: “What did she play [NP Dungeons and ]?” is ungrammatical. But
you can have the same gap in both branches of a VP conjunction, as in the sentence “What
did you [VP [VP smell ] and [VP shoot an arrow at ]]?”
Time and tense: Suppose we want to represent the difference between “Ali loves Bo”
Time and tense
and “Ali loved Bo.” English uses verb tenses (past, present, and future) to indicate the relative
time of an event. One good choice to represent the time of events is the event calculus notation
of Section 10.3. In event calculus we have
Ali loves Bo: E1 ∈Loves(Ali,Bo)∧During(Now,Extent(E1))
Ali loved Bo: E2 ∈Loves(Ali,Bo)∧After(Now,Extent(E2)).
This suggests that our two lexical rules for the words “loves” and “loved” should be these:
Verb(λy λx e∈Loves(x,y)∧During(Now,e)) →loves
Verb(λy λx e∈Loves(x,y)∧After(Now,e)) →loved.
Other than this change, everything else about the grammar remains the same, which is en-
couraging news; it suggests we are on the right track if we can so easily add a complication
like the tense of verbs (although we have just scratched the surface of a complete grammar
for time and tense).
