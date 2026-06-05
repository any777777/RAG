---
chunk_id: "book-ca4fca8dd8-chunk-0705"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 705
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 12.7
The Wumpus World Revisited
423
world are that (1) a pit causes breezes in all neighboring squares, and (2) each square other
than [1,1] contains a pit with probability 0.2. The ﬁrst step is to identify the set of random
variables we need:
• As in the propositional logic case, we want one Boolean variable Pi j for each square,
which is true iff square [i, j] actually contains a pit.
• We also have Boolean variables Bij that are true iff square [i, j] is breezy; we include
these variables only for the observed squares—in this case, [1,1], [1,2], and [2,1].
The next step is to specify the full joint distribution, P(P1,1,...,P4,4,B1,1,B1,2,B2,1). Applying
the product rule, we have
P(P1,1,...,P4,4,B1,1,B1,2,B2,1) =
P(B1,1,B1,2,B2,1 | P1,1,...,P4,4)P(P1,1,...,P4,4).
This decomposition makes it easy to see what the joint probability values should be. The
ﬁrst term is the conditional probability distribution of a breeze conﬁguration, given a pit
conﬁguration; its values are 1 if all the breezy squares are adjacent to the pits and 0 otherwise.
The second term is the prior probability of a pit conﬁguration. Each square contains a pit with
probability 0.2, independently of the other squares; hence,
P(P1,1,...,P4,4) =
4,4
∏
i,j=1,1
P(Pi,j).
(12.22)
For a particular conﬁguration with exactly n pits, the probability is 0.2n ×0.816−n.
In the situation in Figure 12.5(a), the evidence consists of the observed breeze (or its
absence) in each square that is visited, combined with the fact that each such square contains
no pit. We abbreviate these facts as b=¬b1,1 ∧b1,2 ∧b2,1 and known=¬p1,1 ∧¬p1,2 ∧¬p2,1.
We are interested in answering queries such as P(P1,3 |known,b): how likely is it that [1,3]
contains a pit, given the observations so far?
To answer this query, we can follow the standard approach of Equation (12.9), namely,
summing over entries from the full joint distribution. Let Unknown be the set of Pi,j vari-
ables for squares other than the known squares and the query square [1,3]. Then, by Equa-
tion (12.9), we have
P(P1,3 |known,b) = α ∑
unknown
P(P1,3,known,b,unknown).
(12.23)
The full joint probabilities have already been speciﬁed, so we are done—that is, unless we
care about computation.
There are 12 unknown squares; hence the summation contains
212 =4096 terms. In general, the summation grows exponentially with the number of squares.
Surely, one might ask, aren’t the other squares irrelevant? How could [4,4] affect whether
[1,3] has a pit? Indeed, this intuition is roughly correct, but it needs to be made more precise.
What we really mean is that if we knew the values of all the pit variables adjacent to the
squares we care about, then pits (or their absence) in other, more distant squares could have
no further effect on our belief.
Let Frontier be the pit variables (other than the query variable) that are adjacent to visited
squares, in this case just [2,2] and [3,1]. Also, let Other be the pit variables for the other
unknown squares; in this case, there are 10 other squares, as shown in Figure 12.5(b). With
these deﬁnitions, Unknown=Frontier∪Other. The key insight given above can now be stated
as follows: the observed breezes are conditionally independent of the other variables, given
