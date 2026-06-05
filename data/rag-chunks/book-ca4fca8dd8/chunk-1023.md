---
chunk_id: "book-ca4fca8dd8-chunk-1023"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1023
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.2
Non-Cooperative Game Theory
615
for Harriet, given Robbie’s strategy; and so on. The process unfolds as follows:
1. Start with the greedy strategy for Harriet: make two paperclips if she prefers paperclips;
make one of each if she is indifferent; make two staples if she prefers staples.
2. There are three possibilities Robbie has to consider, given this strategy for Harriet:
(a) If Robbie sees Harriet make two paperclips, he infers that she prefers paperclips,
so he now believes the value of a paperclip is uniformly distributed between 0.5
and 1.0, with an average of 0.75. In that case, his best plan is to make 90 paperclips
with an expected value of $67.50 for Harriet.
(b) If Robbie sees Harriet make one of each, he infers that she values paperclips and
staples at 0.50, so the best choice is to make 50 of each.
(c) If Robbie sees Harriet make two staples, then by the same argument as in (a), he
should make 90 staples.
3. Given this strategy for Robbie, Harriet’s best strategy is now somewhat different from
the greedy strategy in step 1. If Robbie is going to respond to her making one of each
by making 50 of each, then she is better off making one of each not just if she is exactly
indifferent, but if she is anywhere close to indifferent. In fact, the optimal policy is now
to make one of each if she values paperclips anywhere between about 0.446 and 0.554.
4. Given this new strategy for Harriet, Robbie’s strategy remains unchanged. For example,
if she chooses one of each, he infers that the value of a paperclip is uniformly distributed
between 0.446 and 0.554, with an average of 0.50, so the best choice is to make 50 of
each. Because Robbie’s strategy is the same as in step 2, Harriet’s best response will be
the same as in step 3, and we have found the equilibrium.
With her strategy, Harriet is, in effect, teaching Robbie about her preferences using a simple
code–—a language, if you like–—that emerges from the equilibrium analysis. Note also that
Robbie never learns Harriet’s preferences exactly, but he learns enough to act optimally on
her behalf–—i.e., he acts just as he would if he did know her preferences exactly. He is
provably beneﬁcial to Harriet under the assumptions stated, and under the assumption that
Harriet is playing the game correctly.
Myopic best response works for this example and others like it, but not for more complex
cases. It is possible to prove that provided there are no ties that cause coordination problems,
ﬁnding an optimal strategy proﬁle for an assistance game is reducible to solving a POMDP
whose state space is the underlying state space of the game plus the human preference pa-
rameters θ. POMDPs in general are very hard to solve (Section 16.5), but the POMDPs that
represent assistance games have additional structure that enables more efﬁcient algorithms.
Assistance games can be generalized to allow for multiple human participants, multiple
robots, imperfectly rational humans, humans who don’t know their own preferences, and
so on. By providing a factored or structured action space, as opposed to the simple atomic
actions in the paperclip game, the opportunities for communication can be greatly enhanced.
Few of these variations have been explored so far, but we expect the key property of assistance
games to remain true: the more intelligent the robot, the better the outcome for the human.
