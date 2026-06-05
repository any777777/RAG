---
chunk_id: "book-ca4fca8dd8-chunk-0704"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 704
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 422

422
Chapter 12
Quantifying Uncertainty
OK
 1,1
 2,1
 3,1
 4,1
 1,2
 2,2
 3,2
 4,2
 1,3
 2,3
 3,3
 4,3
 1,4
 2,4
OK
OK
 3,4
 4,4
B
B
1,1
 2,1
 3,1
 4,1
1,2
2,2
 3,2
 4,2
 2,3
 3,3
 4,3
 2,4
 3,4
 4,4
KNOWN
FRONTIER
1,3
1,4
QUERY
OTHER
(a)
(b)
Figure 12.5 (a) After ﬁnding a breeze in both [1,2] and [2,1], the agent is stuck—there is
no safe place to explore. (b) Division of the squares into Known, Frontier, and Other, for a
query about [1,3].
The naive Bayes model assumes that words occur independently in documents, with fre-
quencies determined by the document category. This independence assumption is clearly
violated in practice. For example, the phrase “ﬁrst quarter” occurs more frequently in busi-
ness (or sports) articles than would be suggested by multiplying the probabilities of “ﬁrst” and
“quarter.” The violation of independence usually means that the ﬁnal posterior probabilities
will be much closer to 1 or 0 than they should be; in other words, the model is overconﬁ-
dent in its predictions. On the other hand, even with these errors, the ranking of the possible
categories is often quite accurate.
Naive Bayes models are widely used for language determination, document retrieval,
spam ﬁltering, and other classiﬁcation tasks. For tasks such as medical diagnosis, where the
actual values of the posterior probabilities really matter—for example, in deciding whether to
perform an appendectomy—one would usually prefer to use the more sophisticated models
described in the next chapter.
12.7 The Wumpus World Revisited
We can combine the ideas in this chapter to solve probabilistic reasoning problems in the
wumpus world. (See Chapter 7 for a complete description of the wumpus world.) Uncertainty
arises in the wumpus world because the agent’s sensors give only partial information about
the world. For example, Figure 12.5 shows a situation in which each of the three unvisited
but reachable squares—[1,3], [2,2], and [3,1]—might contain a pit. Pure logical inference
can conclude nothing about which square is most likely to be safe, so a logical agent might
have to choose randomly. We will see that a probabilistic agent can do much better than the
logical agent.
Our aim is to calculate the probability that each of the three squares contains a pit. (For
this example we ignore the wumpus and the gold.) The relevant properties of the wumpus

## Page 423
