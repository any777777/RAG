---
chunk_id: "book-ca4fca8dd8-chunk-0577"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 577
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 10.6
Reasoning with Default Information
351
weeks to solve a problem. The thrust in description logics, on the other hand, is to ensure that
subsumption-testing can be solved in time polynomial in the size of the descriptions.7
This sounds wonderful in principle, until one realizes that it can only have one of two
consequences: either hard problems cannot be stated at all, or they require exponentially
large descriptions! However, the tractability results do shed light on what sorts of constructs
cause problems and thus help the user to understand how different representations behave.
For example, description logics usually lack negation and disjunction. Each forces ﬁrst-
order logical systems to go through a potentially exponential case analysis in order to ensure
completeness. CLASSIC allows only a limited form of disjunction in the Fills and OneOf
constructs, which permit disjunction over explicitly enumerated individuals but not over de-
scriptions. With disjunctive descriptions, nested deﬁnitions can lead easily to an exponential
number of alternative routes by which one category can subsume another.
10.6 Reasoning with Default Information
In the preceding section, we saw a simple example of an assertion with default status: people
have two legs. This default can be overridden by more speciﬁc information, such as that
Long John Silver has one leg. We saw that the inheritance mechanism in semantic networks
implements the overriding of defaults in a simple and natural way. In this section, we study
defaults more generally, with a view toward understanding the semantics of defaults rather
than just providing a procedural mechanism.
10.6.1 Circumscription and default logic
We have seen two examples of reasoning processes that violate the monotonicity property of
Monotonicity
logic that was proved in Chapter 7.8 In this chapter we saw that a property inherited by all
members of a category in a semantic network could be overridden by more speciﬁc informa-
tion for a subcategory. In Section 9.4.4, we saw that under the closed-world assumption, if a
proposition α is not mentioned in KB then KB |= ¬α, but KB∧α |= α.
Simple introspection suggests that these failures of monotonicity are widespread in com-
monsense reasoning. It seems that humans often “jump to conclusions.” For example, when
one sees a car parked on the street, one is normally willing to believe that it has four wheels
even though only three are visible. Now, probability theory can certainly provide a conclusion
that the fourth wheel exists with high probability; yet, for most people, the possibility that the
car does not have four wheels will not arise unless some new evidence presents itself. Thus,
it seems that the four-wheel conclusion is reached by default, in the absence of any reason to
doubt it. If new evidence arrives—for example, if one sees the owner carrying a wheel and
notices that the car is jacked up—then the conclusion can be retracted. This kind of reasoning
is said to exhibit nonmonotonicity, because the set of beliefs does not grow monotonically
Nonmonotonicity
over time as new evidence arrives. Nonmonotonic logics have been devised with modiﬁed
Nonmonotonic logic
notions of truth and entailment in order to capture such behavior. We will look at two such
logics that have been studied extensively: circumscription and default logic.
Circumscription can be seen as a more powerful and precise version of the closed-world
Circumscription
7
CLASSIC provides efﬁcient subsumption testing in practice, but the worst-case run time is exponential.
8
Recall that monotonicity requires all entailed sentences to remain entailed after new sentences are added to the
KB. That is, if KB |= α then KB∧β |= α.
