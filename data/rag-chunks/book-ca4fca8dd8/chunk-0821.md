---
chunk_id: "book-ca4fca8dd8-chunk-0821"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 821
confidence: "first-pass"
extraction_method: "structured-local"
---

494
Chapter 14
Probabilistic Reasoning over Time
Equation (14.13) d times to get
bt−d+1:t =
 
t
∏
i=t−d+1
TOi
!
bt+1:t = Bt−d+1:t1,
(14.14)
where the matrix Bt−d+1:t is the product of the sequence of T and O matrices and 1 is a vector
of 1s. B can be thought of as a “transformation operator” that transforms a later backward
message into an earlier one. A similar equation holds for the new backward messages after
the next observation arrives:
bt−d+2:t+1 =
 
t+1
∏
i=t−d+2
TOi
!
bt+2:t+1 = Bt−d+2:t+11.
(14.15)
Examining the product expressions in Equations (14.14) and (14.15), we see that they have a
simple relationship: to get the second product, “divide” the ﬁrst product by the ﬁrst element
TOt−d+1, and multiply by the new last element TOt+1. In matrix language, then, there is a
simple relationship between the old and new B matrices:
Bt−d+2:t+1 = O−1
t−d+1T−1Bt−d+1:tTOt+1 .
(14.16)
This equation provides an incremental update for the B matrix, which in turn (through Equa-
tion (14.15)) allows us to compute the new backward message bt−d+2:t+1. The complete
algorithm, which requires storing and updating f and B, is shown in Figure 14.6.
14.3.2 Hidden Markov model example: Localization
On page 151, we introduced a simple form of the localization problem for the vacuum world.
In that version, the robot had a single nondeterministic Move action and its sensors reported
perfectly whether or not obstacles lay immediately to the north, south, east, and west; the
robot’s belief state was the set of possible locations it could be in.
Here we make the problem slightly more realistic by allowing for noise in the sensors,
and formalizing the idea that the robot moves randomly—it is equally likely to move to
any adjacent empty square. The state variable Xt represents the location of the robot on the
discrete grid; the domain of this variable is the set of empty squares, which we will label by
the integers{1,...,S}. Let NEIGHBORS(i) be the set of empty squares that are adjacent to i
and let N(i) be the size of that set. Then the transition model for the Move action says that
the robot is equally likely to end up at any neighboring square:
P(Xt+1 = j|Xt =i) = Tij =
 1/N(i) if j ∈NEIGHBORS(i)
0 otherwise.
We don’t know where the robot starts, so we will assume a uniform distribution over all the
squares; that is, P(X0 =i)=1/S. For the particular environment we consider (Figure 14.7),
S=42 and the transition matrix T has 42×42=1764 entries.
The sensor variable Et has 16 possible values, each a four-bit sequence giving the pres-
ence or absence of an obstacle in each of the compass directions NESW. For example, 1010
means that the north and south sensors report an obstacle and the east and west do not. Sup-
pose that each sensor’s error rate is ϵ and that errors occur independently for the four sensor
directions. In that case, the probability of getting all four bits right is (1−ϵ)4 and the proba-
bility of getting them all wrong is ϵ4. Furthermore, if dit is the discrepancy—the number of
