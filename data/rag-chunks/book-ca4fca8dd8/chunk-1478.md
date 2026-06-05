---
chunk_id: "book-ca4fca8dd8-chunk-1478"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1478
confidence: "first-pass"
extraction_method: "structured-local"
---

892
Chapter 24
Natural Language Processing
24.4 Augmented Grammars
So far we have dealt with context-free grammars. But not every NP can appear in every
context with equal probability. The sentence “I ate a banana” is ﬁne, but “Me ate a banana”
is ungrammatical, and “I ate a bandanna” is unlikely.
The issue is that our grammar is focused on lexical categories, like Pronoun, but while “I”
and “me” are both pronouns, only “I” can be the subject of a sentence. Similarly, “banana”
and “bandanna” are both nouns, but the former is much more likely to be object of “ate”.
Linguists say that the pronoun “I” is in the subjective case (i.e., is the subject of a verb) and
“me” is in the objective case3 (i.e., is the object of a verb). They also say that “I” is in the ﬁrst
person (“you” is second person, and “she” is third person) and is singular (“we” is plural).
A category like Pronoun that has been augmented with features like “subjective case, ﬁrst
person singular” is called a subcategory.
Subcategory
In this section we show how a grammar can represent this kind of knowledge to make
ﬁner-grained distinctions about which sentences are more likely. We will also show how to
construct a representation of the semantics of a phrase, in a compositional way. All of this
will be accomplished with an augmented grammar in which the nonterminals are not just
Augmented
grammar
atomic symbols like Pronoun or NP, but are structured representations. For example, the
noun phrase “I” could be represented as NP(Sbj,1S,Speaker), which means “a noun phrase
that is in the subjective case, ﬁrst person singular, and whose meaning is the speaker of the
sentence.” In contrast, “me” would be represented as NP(Obj,1S,Speaker), marking the fact
that it is in the objective case.
Consider the sequence “Noun and Noun or Noun,” which can be parsed either as “[Noun
and Noun] or Noun,” or as “Noun and [Noun or Noun].” Our context-free grammar has no
way to express a preference for one parse over the other, because the rule for conjoined NPs,
NP →NP Conjunction NP[0.05], will give the same probability to each parse. We would
like a grammar that prefers the parses “[[spaghetti and meatballs] or lasagna]” and “[spaghetti
and [pie or cake]]” over the alternative bracketing for each of these phrases.
A lexicalized PCFG is a type of augmented grammar that allows us to assign probabili-
Lexicalized PCFG
ties based on properties of the words in a phrase other than just the syntactic categories. The
data would be very sparse indeed if the probability of, say, a 40-word sentence depended on
all 40 words—this is the same problem we noted with n-grams. To simplify, we introduce the
notion of the head of a phrase—the most important word. Thus, “banana” is the head of the
Head
NP “a banana” and “ate” is the head of the VP “ate a banana.” The notation VP(v) denotes a
phrase with category VP whose head word is v. Here is a lexicalized PCFG:
VP(v) →Verb(v) NP(n)
[P1(v,n)]
VP(v) →Verb(v)
[P2(v)]
NP(n) →Article(a) Adjs(j) Noun(n)
[P3(n,a)]
NP(n) →NP(n) Conjunction(c) NP(m) [P4(n,c,m)]
Verb(ate) →ate
[0.002]
Noun(banana) →banana
[0.0007]
3
The subjective case is also sometimes called the nominative case and the objective case is sometimes called
the accusative case. Many languages also make another distinction with a dative case for words in the indirect
object position.
