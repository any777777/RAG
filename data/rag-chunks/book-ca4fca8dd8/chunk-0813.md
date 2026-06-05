---
chunk_id: "book-ca4fca8dd8-chunk-0813"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 813
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.2
Inference in Temporal Models
489
and the sequences are long. It uses O(|f|t) space where |f| is the size of the representation of
the forward message. The space requirement can be reduced to O(|f|logt) with a concomitant
increase in the time complexity by a factor of logt, as shown in Exercise 14.ISLE. In some
cases (see Section 14.3), a constant-space algorithm can be used.
The second drawback of the basic algorithm is that it needs to be modiﬁed to work in an
online setting where smoothed estimates must be computed for earlier time slices as new ob-
servations are continuously added to the end of the sequence. The most common requirement
is for ﬁxed-lag smoothing, which requires computing the smoothed estimate P(Xt−d |e1:t)
Fixed-lag smoothing
for ﬁxed d. That is, smoothing is done for the time slice d steps behind the current time t; as t
increases, the smoothing has to keep up. Obviously, we can run the forward–backward algo-
rithm over the d-step “window” as each new observation is added, but this seems inefﬁcient.
In Section 14.3, we will see that ﬁxed-lag smoothing can, in some cases, be done in constant
time per update, independent of the lag d.
14.2.3 Finding the most likely sequence
Suppose that [true,true,false,true,true] is the observed umbrella sequence for the security
guard’s ﬁrst ﬁve days on the job. What weather sequence is most likely to explain this? Does
the absence of the umbrella on day 3 mean that it wasn’t raining, or did the director forget
to bring it? If it didn’t rain on day 3, perhaps (because weather tends to persist) it didn’t
rain on day 4 either, but the director brought the umbrella just in case. In all, there are 25
possible weather sequences we could pick. Is there a way to ﬁnd the most likely one, short of
enumerating all of them and calculating their likelihoods?
We could try this linear-time procedure: use smoothing to ﬁnd the posterior distribution
for the weather at each time step; then construct the sequence, using at each step the weather
that is most likely according to the posterior. Such an approach should set off alarm bells
in the reader’s head, because the posterior distributions computed by smoothing are distri-
butions over single time steps, whereas to ﬁnd the most likely sequence we must consider
joint probabilities over all the time steps. The results can in fact be quite different. (See
Exercise 14.VITE.)
There is a linear-time algorithm for ﬁnding the most likely sequence, but it requires more
thought. It relies on the same Markov property that yielded efﬁcient algorithms for ﬁltering
and smoothing. The idea is to view each sequence as a path through a graph whose nodes
are the possible states at each time step. Such a graph is shown for the umbrella world in
Figure 14.5(a). Now consider the task of ﬁnding the most likely path through this graph,
where the likelihood of any path is the product of the transition probabilities along the path
and the probabilities of the given observations at each state.
Let’s focus in particular on paths that reach the state Rain5 =true. Because of the Markov
property, it follows that the most likely path to the state Rain5 =true consists of the most
likely path to some state at time 4 followed by a transition to Rain5 =true; and the state at
time 4 that will become part of the path to Rain5 =true is whichever maximizes the likelihood
of that path. In other words, there is a recursive relationship between most likely paths to each ◀
state xt+1 and most likely paths to each state xt.
We can use this property directly to construct a recursive algorithm for computing the
most likely path given the evidence. We will use a recursively computed message m1:t, like
