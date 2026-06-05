---
chunk_id: "book-ca4fca8dd8-chunk-1000"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1000
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 602

602
Chapter 17
Multiagent Decision Making
one
one
one
two
two
two
E
O
one
one
one
two
two
two
O
E
one
two
E
O
one
two
O
E
+4
+3
+2
+1
 0
–1
–2
–3
1
two
one
U
p
+4
+3
+2
+1
 0
–1
–2
–3
1
two
one
U
q
(a)
(b)
(c)
(d)
(e)
(f)
[p: one; (1 – p): two]
[q: one; (1 – q): two]
2p – 3(1 – p
2
)
q – 3(1 – q)
3p + 4(1 – p
3
)
q + 4(1 – q)
2
-3
-3
-3
-3
-3
4
2
2
2
-3
-3
4
4
Figure 17.2 (a) and (b): Minimax game trees for two-ﬁnger Morra if the players take turns
playing pure strategies. (c) and (d): Parameterized game trees where the ﬁrst player plays
a mixed strategy. The payoffs depend on the probability parameter (p or q) in the mixed
strategy. (e) and (f): For any particular value of the probability parameter, the second player
will choose the “better” of the two actions, so the value of the ﬁrst player’s mixed strategy is
given by the heavy lines. The ﬁrst player will choose the probability parameter for the mixed
strategy at the intersection point.
• If O moves ﬁrst, the situation is as shown in Figure 17.2(d). O chooses the strategy
[q:one;(1 −q):two] at the root, and then E chooses a move given the value of q. The
payoffs are 2q−3(1−q)=5q−3 and −3q+4(1−q)=4−7q.2 Again, Figure 17.2(f)
shows that the best O can do at the root is to choose the intersection point:
5q−3 = 4−7q
⇒
q = 7/12.
The utility for E at this point is UO,E = −1/12.
2
It is a coincidence that these equations are the same as those for p; the coincidence arises because
UE(one,two)=UE(two,one)= −3. This also explains why the optimal strategy is the same for both players.

## Page 603
