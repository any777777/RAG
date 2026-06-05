---
chunk_id: "book-ca4fca8dd8-chunk-0904"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 904
confidence: "first-pass"
extraction_method: "structured-local"
---

546
Chapter 15
Making Simple Decisions
The upshot is that Robbie has a positive incentive to defer to Harriet—that is, to allow
himself to be switched off. This incentive comes directly from Robbie’s uncertainty about
Harriet’s preferences. Robbie is aware that there’s a chance (40% in this example) that he
might be about to do something that will make Harriet unhappy, in which case being switched
off would be preferable to going ahead. Were Robbie already certain about Harriet’s prefer-
ences, he would just go ahead and make the decision (or switch himself off); there would
be absolutely nothing to be gained from consulting Harriet, because, according to Robbie’s
deﬁnite beliefs, he can already predict exactly what she is going to decide.
In fact, it is possible to prove the same result in the general case: as long as Robbie is
not completely certain that he’s about to do what Harriet herself would do, he is better off
allowing her to switch him off. Intuitively, her decision provides Robbie with information,
and the expected value of information is always nonnegative. Conversely, if Robbie is certain
about Harriet’s decision, her decision provides no new information, and so Robbie has no
incentive to allow her to decide.
Formally, let P(u) be Robbie’s prior probability density over Harriet’s utility for the pro-
posed action a. Then the value of going ahead with a is
EU(a) =
Z ∞
−∞P(u)·udu =
Z 0
−∞P(u)·udu+
Z ∞
0 P(u)·udu.
(We will see shortly why the integral is split up in this way.) On the other hand, the value of
action d, deferring to Harriet, is composed of two parts: if u > 0 then Harriet lets Robbie go
ahead, so the value is u, but if u < 0 then Harriet switches Robbie off, so the value is 0:
EU(d) =
Z 0
−∞P(u)·0du+
Z ∞
0 P(u)·udu.
Comparing the expressions for EU(a) and EU(d), we see immediately that
EU(d) ≥EU(a)
because the expression for EU(d) has the negative-utility region zeroed out. The two choices
have equal value only when the negative region has zero probability—that is, when Robbie is
already certain that Harriet likes the proposed action.
There are some obvious elaborations on the model that are worth exploring immediately.
The ﬁrst elaboration is to impose a cost for Harriet’s time. In that case, Robbie is less inclined
to bother Harriet if the downside risk is small. This is as it should be. And if Harriet is really
grumpy about being interrupted, she shouldn’t be too surprised if Robbie occasionally does
things she doesn’t like.
The second elaboration is to allow for some probability of human error—that is, Harriet
might sometimes switch Robbie off even when his proposed action is reasonable, and she
might sometimes let Robbie go ahead even when his proposed action is undesirable. It is
straightforward to fold this error probability into the model (see Exercise 15.OFFS). As one
might expect, the solution shows that Robbie is less inclined to defer to an irrational Harriet
who sometimes acts against her own best interests. The more randomly she behaves, the more
uncertain Robbie has to be about her preferences before deferring to her. Again, this is as it
should be: for example, if Robbie is a self-driving car and Harriet is his naughty two-year-old
passenger, Robbie should not allow Harriet to switch him off in the middle of the highway.
