---
chunk_id: "book-ca4fca8dd8-chunk-0379"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 379
confidence: "first-pass"
extraction_method: "structured-local"
---

232
Chapter 7
Logical Agents
7.3 Logic
This section summarizes the fundamental concepts of logical representation and reasoning.
These beautiful ideas are independent of any of logic’s particular forms. We therefore post-
pone the technical details of those forms until the next section, using instead the familiar
example of ordinary arithmetic.
In Section 7.1, we said that knowledge bases consist of sentences. These sentences are
expressed according to the syntax of the representation language, which speciﬁes all the
Syntax
sentences that are well formed. The notion of syntax is clear enough in ordinary arithmetic:
“x+y = 4” is a well-formed sentence, whereas “x4y+ =” is not.
A logic must also deﬁne the semantics, or meaning, of sentences. The semantics deﬁnes
Semantics
the truth of each sentence with respect to each possible world. For example, the semantics
Truth
Possible world
for arithmetic speciﬁes that the sentence “x+y=4” is true in a world where x is 2 and y is 2,
but false in a world where x is 1 and y is 1. In standard logics, every sentence must be either
true or false in each possible world—there is no “in between.”2
When we need to be precise, we use the term model in place of “possible world.”
Model
Whereas possible worlds might be thought of as (potentially) real environments that the agent
might or might not be in, models are mathematical abstractions, each of which has a ﬁxed
truth value (true or false) for every relevant sentence. Informally, we may think of a possible
world as, for example, having x men and y women sitting at a table playing bridge, and the
sentence x + y=4 is true when there are four people in total. Formally, the possible models
are just all possible assignments of nonnegative integers to the variables x and y. Each such
assignment determines the truth of any sentence of arithmetic whose variables are x and y. If
a sentence α is true in model m, we say that m satisﬁes α or sometimes m is a model of α.
Satisfaction
We use the notation M(α) to mean the set of all models of α.
Now that we have a notion of truth, we are ready to talk about logical reasoning. This in-
volves the relation of logical entailment between sentences—the idea that a sentence follows
Entailment
logically from another sentence. In mathematical notation, we write
α |= β
to mean that the sentence α entails the sentence β. The formal deﬁnition of entailment is this:
α |= β if and only if, in every model in which α is true, β is also true. Using the notation just
introduced, we can write
α |= β if and only if M(α) ⊆M(β).
(Note the direction of the ⊆here: if α |= β, then α is a stronger assertion than β: it rules out
more possible worlds.) The relation of entailment is familiar from arithmetic; we are happy
with the idea that the sentence x = 0 entails the sentence xy = 0. Obviously, in any model
where x is zero, it is the case that xy is zero (regardless of the value of y).
We can apply the same kind of analysis to the wumpus-world reasoning example given
in the preceding section. Consider the situation in Figure 7.3(b): the agent has detected
nothing in [1,1] and a breeze in [2,1]. These percepts, combined with the agent’s knowledge
of the rules of the wumpus world, constitute the KB. The agent is interested in whether the
adjacent squares [1,2], [2,2], and [3,1] contain pits. Each of the three squares might or might
2
Fuzzy logic, discussed in Chapter 13, allows for degrees of truth.
