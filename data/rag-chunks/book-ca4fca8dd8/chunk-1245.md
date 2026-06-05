---
chunk_id: "book-ca4fca8dd8-chunk-1245"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1245
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 20.3
Explanation-Based Learning
751
and eventually this simpliﬁes to 2X. In the authors’ logic programming implementation, this
takes 136 proof steps, of which 99 are on dead-end branches in the proof. After such an
experience, we would like the program to solve the same problem much more quickly the
next time it arises.
The technique of memoization has long been used in computer science to speed up pro-
Memoization
grams by saving the results of computation. The basic idea of memo functions is to accumu-
late a database of input–output pairs; when the function is called, it ﬁrst checks the database
to see whether it can avoid solving the problem from scratch. Explanation-based learning
takes this a good deal further, by creating general rules that cover an entire class of cases.
In the case of differentiation, memoization would remember that the derivative of X2 with
respect to X is 2X, but would leave the agent to calculate the derivative of Z2 with respect to
Z from scratch. We would like to be able to extract the general rule that for any arithmetic
unknown u, the derivative of u2 with respect to u is 2u. (An even more general rule for un can
also be produced, but the current example sufﬁces to make the point.) In logical terms, this is
expressed by the rule
ArithmeticUnknown(u) ⇒Derivative(u2,u)=2u .
If the knowledge base contains such a rule, then any new case that is an instance of this rule
can be solved immediately.
This is, of course, merely a trivial example of a very general phenomenon. Once some-
thing is understood, it can be generalized and reused in other circumstances. It becomes an
“obvious” step and can then be used as a building block in solving problems still more com-
plex. Alfred North Whitehead (1911), co-author with Bertrand Russell of Principia Mathe-
matica, wrote “Civilization advances by extending the number of important operations that ◀
we can do without thinking about them,” perhaps himself applying EBL to his understanding
of events such as Zog’s discovery. If you have understood the basic idea of the differenti-
ation example, then your brain is already busily trying to extract the general principles of
explanation-based learning from it. Notice that you hadn’t already invented EBL before you
saw the example. Like the cavemen watching Zog, you (and we) needed an example before
we could generate the basic principles. This is because explaining why something is a good
idea is much easier than coming up with the idea in the ﬁrst place.
20.3.1 Extracting general rules from examples
The basic idea behind EBL is ﬁrst to construct an explanation of the observation using prior
knowledge, and then to establish a deﬁnition of the class of cases for which the same expla-
nation structure can be used. This deﬁnition provides the basis for a rule covering all of the
cases in the class. The “explanation” can be a logical proof, but more generally it can be any
reasoning or problem-solving process whose steps are well deﬁned. The key is to be able to
identify the necessary conditions for those same steps to apply to another case.
We will use for our reasoning system the simple backward-chaining theorem prover de-
scribed in Chapter 9. The proof tree for Derivative(X2,X)=2X is too large to use as an
example, so we will use a simpler problem to illustrate the generalization method. Suppose
our problem is to simplify 1×(0+X). The knowledge base includes the following rules:
