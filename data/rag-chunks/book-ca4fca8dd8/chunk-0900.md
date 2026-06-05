---
chunk_id: "book-ca4fca8dd8-chunk-0900"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 900
confidence: "first-pass"
extraction_method: "structured-local"
---

544
Chapter 15
Making Simple Decisions
U
+$8
+$1
D/V
durian
vanilla
U
+$98
–$82
LikesDurian
true
false
true
false
+$1
+$1
D/V
durian
durian
vanilla
vanilla
+$98
0.5
0.0
D/V
durian
vanilla
…
…
…
…
…
…
…
…
…
…
…
…
+$1
+$0
–$82
0.0
0.0
0.5
1.0
0.0
0.0
(a)
(b)
(c)
U
Durian/Vanilla
U
Durian/Vanilla
U
Durian/Vanilla
LikesDurian
Figure 15.10 (a) A decision network for the ice cream choice with an uncertain utility func-
tion. (b) The network with the expected utility of each action. (c) Moving the uncertainty
from the utility function into a new random variable.
To put some numbers on this, let’s say there’s a 50% chance you’ll ﬁnd it sublime (+$100)
and a 50% chance you’ll hate it (-$80 if the taste lingers all afternoon). Here, there’s no uncer-
tainty about what prize you’re going to win—it’s the same durian ice cream either way—but
there’s uncertainty about your own preferences for that prize.
We could extend the decision network formalism to allow for uncertain utilities, as shown
in Figure 15.10(a). If there is no more information to be obtained about your durian prefer-
ences, however—for example, if the shop won’t let you taste it ﬁrst—then the decision prob-
lem is identical to the one shown in Figure 15.10(b). We can simply replace the uncertain
value of the durian with its expected net gain of (0.5×$100) −(0.5×$80) −$2=$8 and
your decision will remain unchanged.
If it’s possible for your beliefs about durian to change—perhaps you get a tiny taste,
or you ﬁnd out that all of your living relatives love durian—then the transformation in Fig-
ure 15.10(b) is not valid. It turns out, however, that we can still ﬁnd an equivalent model in
which the utility function is deterministic. Rather than saying there is uncertainty about the
utility function, we move that uncertainty “into the world,” so to speak. That is, we create a
new random variable LikesDurian with prior probabilities of 0.5 for true and false, as shown
in Figure 15.10(c). With this extra variable, the utility function becomes deterministic, but
we can still handle changing beliefs about your durian preferences.
The fact that unknown preferences can be modeled by ordinary random variables means
that we can keep using the machinery and theorems developed for known preferences. On
the other hand, it doesn’t mean that we can always assume that preferences are known. The
uncertainty is still there and still affects how agents should behave.
15.7.2 Deference to humans
Now let’s turn to the second case mentioned above: a machine that is supposed to help a
human but is uncertain about what the human wants. The full treatment of this case must be
deferred to Chapter 17, where we discuss decisions involving more than one agent. Here, we
ask one simple question: under what circumstances will such a machine defer to the human?
