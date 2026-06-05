---
chunk_id: "book-ca4fca8dd8-chunk-1249"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1249
confidence: "first-pass"
extraction_method: "structured-local"
---

754
Chapter 20
Knowledge in Learning
A common approach to ensuring that derived rules are efﬁcient is to insist on the opera-
tionality of each subgoal in the rule. A subgoal is operational if it is “easy” to solve. For
Operationality
example, the subgoal Primitive(z) is easy to solve, requiring at most two steps, whereas the
subgoal Simplify(y + z,w) could lead to an arbitrary amount of inference, depending on the
values of y and z. If a test for operationality is carried out at each step in the construction
of the generalized proof, then we can prune the rest of a branch as soon as an operational
subgoal is found, keeping just the operational subgoal as a conjunct of the new rule.
Unfortunately, there is usually a tradeoff between operationality and generality. More
speciﬁc subgoals are generally easier to solve but cover fewer cases. Also, operationality
is a matter of degree: one or two steps is deﬁnitely operational, but what about 10 or 100?
Finally, the cost of solving a given subgoal depends on what other rules are available in the
knowledge base. It can go up or down as more rules are added. Thus, EBL systems really
face a very complex optimization problem in trying to maximize the efﬁciency of a given
initial knowledge base. It is sometimes possible to derive a mathematical model of the effect
on overall efﬁciency of adding a given rule and to use this model to select the best rule to
add. The analysis can become very complicated, however, especially when recursive rules
are involved. One promising approach is to address the problem of efﬁciency empirically,
simply by adding several rules and seeing which ones are useful and actually speed things up.
Empirical analysis of efﬁciency is actually at the heart of EBL. What we have been call-
ing loosely the “efﬁciency of a given knowledge base” is actually the average-case com-
plexity on a distribution of problems. By generalizing from past example problems, EBL
▶
makes the knowledge base more efﬁcient for the kind of problems that it is reasonable to
expect. This works as long as the distribution of past examples is roughly the same as for
future examples—the same assumption used for PAC-learning in Section 19.5. If the EBL
system is carefully engineered, it is possible to obtain signiﬁcant speedups. For example, a
very large Prolog-based natural language system designed for speech-to-speech translation
between Swedish and English was able to achieve real-time performance only by the appli-
cation of EBL to the parsing process (Samuelsson and Rayner, 1991).
20.4 Learning Using Relevance Information
Our traveler in Brazil seems to be able to make a conﬁdent generalization concerning the lan-
guage spoken by other Brazilians. The inference is sanctioned by her background knowledge,
namely, that people in a given country (usually) speak the same language. We can express
this in ﬁrst-order logic as follows:2
Nationality(x,n)∧Nationality(y,n)∧Language(x,l) ⇒Language(y,l) .
(20.6)
(Literal translation: “If x and y have the same nationality n and x speaks language l, then y
also speaks it.”) It is not difﬁcult to show that, from this sentence and the observation that
Nationality(Fernando,Brazil)∧Language(Fernando,Portuguese) ,
the following conclusion is entailed (see Exercise 20.1):
Nationality(x,Brazil) ⇒Language(x,Portuguese) .
2
We assume for the sake of simplicity that a person speaks only one language. Clearly, the rule would have to
be amended for countries such as Switzerland and India.
