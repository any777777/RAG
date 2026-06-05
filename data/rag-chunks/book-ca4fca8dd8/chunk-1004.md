---
chunk_id: "book-ca4fca8dd8-chunk-1004"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1004
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 605

Section 17.2
Non-Cooperative Game Theory
605
testify
testify
testify
testify
testify
testify
testify
testify
testify
testify
testify
testify
refuse
HAWK
GRIM
TAT-FOR-TIT
TIT-FOR-TAT
DOVE
refuse
refuse
refuse
refuse
refuse
refuse
refuse
refuse
refuse
refuse
refuse
Figure 17.3 Some common, colorfully named ﬁnite-state machine strategies for the in-
ﬁnitely repeated prisoner’s dilemma.
The HAWK and DOVE strategies are simpler: HAWK simply plays testify on every round,
while DOVE simply plays refuse on every round. The GRIM strategy is somewhat similar to
TIT-FOR-TAT, but with one important difference: if ever its counterpart plays testify, then it
essentially turns into HAWK: it plays testify forever. While TIT-FOR-TAT is forgiving, in the
sense that it will respond to a subsequent refuse by reciprocating the same, with GRIM there
is no way back. Just playing testify once will result in punishment (playing testify) that goes
on forever. (Can you see what TAT-FOR-TIT does?)
The next issue with inﬁnitely repeated games is how to measure the utility of an inﬁnite
sequence of payoffs. Here, we will focus on the limit of means approach—essentially, this
Limit of means
means taking the average of utilities received over the inﬁnite sequence. With this approach,
given an inﬁnite sequence of payoffs (U0,U1,U2,...), we deﬁne the utility of the sequence to
the corresponding player to be:
lim
T→∞
1
T
T
∑
t=0
Ut .
This value cannot be guaranteed to converge for arbitrary sequences of utilities, but it is
guaranteed to do so for the utility sequences that are generated if we use FSM strategies. To
see this, observe that if FSM strategies play against each other, then eventually, the FSMs will ◀
reenter a conﬁguration that they were in previously, at which point they will start to repeat

## Page 606
