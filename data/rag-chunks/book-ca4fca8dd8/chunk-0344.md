---
chunk_id: "book-ca4fca8dd8-chunk-0344"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 344
confidence: "first-pass"
extraction_method: "structured-local"
---

212
Chapter 6
Adversarial Search and Games
CHANCE
MIN
MAX
CHANCE
MAX
. . .
. . .
B
1
. . .
1-1
1/36
1-2
1/18
TERMINAL
1-2
1/18
...
...
...
...
...
...
...
1-1
1/36
...
...
...
...
...
...
C
. . .
1/18
6-5
6-6
1/36
1/18
6-5
6-6
1/36
2
–1
1
–1
Figure 6.13 Schematic game tree for a backgammon position.
compute the expected value, which is the sum of the value over all outcomes, weighted by
the probability of each chance action:
EXPECTIMINIMAX(s) =







UTILITY(s, MAX)
if IS-TERMINAL(s)
maxa EXPECTIMINIMAX(RESULT(s,a))
if TO-MOVE(s)= MAX
mina EXPECTIMINIMAX(RESULT(s,a))
if TO-MOVE(s)= MIN
∑r P(r)EXPECTIMINIMAX(RESULT(s,r)) if TO-MOVE(s)= CHANCE
where r represents a possible dice roll (or other chance event) and RESULT(s,r) is the same
state as s, with the additional fact that the result of the dice roll is r.
6.5.1 Evaluation functions for games of chance
As with minimax, the obvious approximation to make with expectiminimax is to cut the
search off at some point and apply an evaluation function to each leaf. One might think that
evaluation functions for games such as backgammon should be just like evaluation functions
for chess—they just need to give higher values to better positions. But in fact, the presence
of chance nodes means that one has to be more careful about what the values mean.
Figure 6.14 shows what happens: with an evaluation function that assigns the values [1,
2, 3, 4] to the leaves, move a1 is best; with values [1, 20, 30, 400], move a2 is best. Hence,
the program behaves totally differently if we make a change to some of the evaluation values,
even if the preference order remains the same.
It turns out that to avoid this problem, the evaluation function must return values that are
a positive linear transformation of the probability of winning (or of the expected utility, for
games that have outcomes other than win/lose). This relation to probability is an important

## Page 213
