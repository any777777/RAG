---
chunk_id: "book-ca4fca8dd8-chunk-0462"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 462
confidence: "first-pass"
extraction_method: "structured-local"
---

282
Chapter 8
First-Order Logic
Thus, we do not really need both ∀and ∃, just as we do not really need both ∧and ∨. Still,
readability is more important than parsimony, so we will keep both of the quantiﬁers.
8.2.7 Equality
First-order logic includes one more way to make atomic sentences, other than using a predi-
cate and terms as described earlier. We can use the equality symbol to signify that two terms
Equality symbol
refer to the same object. For example,
Father(John)=Henry
says that the object referred to by Father(John) and the object referred to by Henry are the
same. Because an interpretation ﬁxes the referent of any term, determining the truth of an
equality sentence is simply a matter of seeing that the referents of the two terms are the same
object.
The equality symbol can be used to state facts about a given function, as we just did for
the Father symbol. It can also be used with negation to insist that two terms are not the same
object. To say that Richard has at least two brothers, we would write
∃x,y Brother(x,Richard)∧Brother(y,Richard)∧¬(x=y).
The sentence
∃x,y Brother(x,Richard)∧Brother(y,Richard)
does not have the intended meaning. In particular, it is true in the model of Figure 8.2, where
Richard has only one brother. To see this, consider the extended interpretation in which both
x and y are assigned to King John. The addition of ¬(x=y) rules out such models. The
notation x ̸= y is sometimes used as an abbreviation for ¬(x=y).
8.2.8 Database semantics
Continuing the example from the previous section, suppose that we believe that Richard has
two brothers, John and Geoffrey.7 We could write
Brother(John,Richard)∧Brother(Geoffrey,Richard),
(8.3)
but that wouldn’t completely capture the state of affairs. First, this assertion is true in a model
where Richard has only one brother—we need to add John ̸= Geoffrey. Second, the sentence
doesn’t rule out models in which Richard has many more brothers besides John and Geoffrey.
Thus, the correct translation of “Richard’s brothers are John and Geoffrey” is as follows:
Brother(John,Richard)∧Brother(Geoffrey,Richard)∧John ̸= Geoffrey
∧∀x Brother(x,Richard) ⇒(x=John∨x=Geoffrey).
This logical sentence seems much more cumbersome than the corresponding English sen-
tence. But if we fail to translate the English properly, our logical reasoning system will make
mistakes. Can we devise a semantics that allows a more straightforward logical sentence?
One proposal that is very popular in database systems works as follows. First, we in-
sist that every constant symbol refer to a distinct object—the unique-names assumption.
Unique-names
assumption
Second, we assume that atomic sentences not known to be true are in fact false—the closed-
world assumption. Finally, we invoke domain closure, meaning that each model contains
Closed-world
assumption
Domain closure
no more domain elements than those named by the constant symbols.
7
Actually he had four, the others being William and Henry.
