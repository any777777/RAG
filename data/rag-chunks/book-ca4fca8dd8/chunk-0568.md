---
chunk_id: "book-ca4fca8dd8-chunk-0568"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 568
confidence: "first-pass"
extraction_method: "structured-local"
---

344
Chapter 10
Knowledge Representation
time
1801
1797
1789
Figure 10.3 A schematic view of the object President(USA) for the early years.
10.4 Mental Objects and Modal Logic
The agents we have constructed so far have beliefs and can deduce new beliefs. Yet none
of them has any knowledge about beliefs or about deduction. Knowledge about one’s own
knowledge and reasoning processes is useful for controlling inference. For example, suppose
Alice asks “what is the square root of 1764” and Bob replies “I don’t know.” If Alice insists
“think harder,” Bob should realize that with some more thought, this question can in fact
be answered. On the other hand, if the question were “Is the president sitting down right
now?” then Bob should realize that thinking harder is unlikely to help. Knowledge about the
knowledge of other agents is also important; Bob should realize that the president does know.
What we need is a model of the mental objects that are in someone’s head (or something’s
knowledge base) and of the mental processes that manipulate those mental objects. The model
does not have to be detailed. We do not have to be able to predict how many milliseconds
it will take for a particular agent to make a deduction. We will be happy just to be able to
conclude that mother knows whether or not she is sitting.
We begin with the propositional attitudes that an agent can have toward mental objects:
Propositional
attitude
attitudes such as Believes, Knows, Wants, and Informs. The difﬁculty is that these attitudes do
not behave like “normal” predicates. For example, suppose we try to assert that Lois knows
that Superman can ﬂy:
Knows(Lois,CanFly(Superman)).
One minor issue with this is that we normally think of CanFly(Superman) as a sentence,
but here it appears as a term. That issue can be patched up by reifying CanFly(Superman);
making it a ﬂuent. A more serious problem is that, if it is true that Superman is Clark Kent,
then we must conclude that Lois knows that Clark can ﬂy, which is wrong because (in most
versions of the story) Lois does not know that Clark is Superman.
(Superman = Clark)∧Knows(Lois,CanFly(Superman))
|= Knows(Lois,CanFly(Clark))
This is a consequence of the fact that equality reasoning is built into logic. Normally that is

## Page 345
