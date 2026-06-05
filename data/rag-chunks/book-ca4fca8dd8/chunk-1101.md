---
chunk_id: "book-ca4fca8dd8-chunk-1101"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1101
confidence: "first-pass"
extraction_method: "structured-local"
---

658
Chapter 18
Probabilistic Programming
objects heading for unknown destinations, objects taking off or landing, etc.) can be han-
dled by small changes to the model without resorting to new mathematical derivations and
complex programming.
From a practical point of view, the challenge with this kind of model is the complexity
of inference. As for all probability models, inference means summing out the variables other
than the query and the evidence. For ﬁltering in HMMs and DBNs, we were able to sum out
the state variables from 1 to t −1 by a simple dynamic programming trick; for Kalman ﬁlters,
we also took advantage of special properties of Gaussians. For data association, we are less
fortunate. There is no (known) efﬁcient exact algorithm, for the same reason that there is none
for the switching Kalman ﬁlter (page 502): the ﬁltering distribution, which describes the joint
distribution over numbers and locations of aircraft at each time step, ends up as a mixture of
exponentially many distributions, one for each way of picking a sequence of observations to
assign to each aircraft.
As a response to the complexity of exact inference, several approximate methods have
been used. The simplest approach is to choose a single “best” assignment at each time step,
given the predicted positions of the objects at the current time. This assignment associates
observations with objects and enables the track of each object to be updated and a prediction
made for the next time step. For choosing the “best” assignment, it is common to use the
so-called nearest-neighbor ﬁlter, which repeatedly chooses the closest pairing of predicted
Nearest-neighbor
ﬁlter
position and observation and adds that pairing to the assignment. The nearest-neighbor ﬁlter
works well when the objects are well separated in state space and the prediction uncertainty
and observation error are small—in other words, when there is no possibility of confusion.
When there is more uncertainty as to the correct assignment, a better approach is to
choose the assignment that maximizes the joint probability of the current observations given
the predicted positions. This can be done efﬁciently using the Hungarian algorithm (Kuhn,
Hungarian algorithm
1955), even though there are n! assignments to choose from as each new time step arrives.
Any method that commits to a single best assignment at each time step fails miserably
under more difﬁcult conditions. In particular, if the algorithm commits to an incorrect assign-
ment, the prediction at the next time step may be signiﬁcantly wrong, leading to more incor-
rect assignments, and so on. Sampling approaches can be much more effective. A particle
ﬁltering algorithm (see page 510) for data association works by maintaining a large collec-
tion of possible current assignments. An MCMC algorithm explores the space of assignment
histories—for example, Figure 18.8(b–c) might be states in the MCMC state space—and can
change its mind about previous assignment decisions.
One obvious way to speed up sampling-based inference for multitarget tracking is to use
the Rao-Blackwellization trick from Chapter 14 (page 514): given a speciﬁc association
hypothesis for all the objects, the ﬁltering calculation for each object can typically be done
exactly and efﬁciently, instead of sampling many possible state sequences for the objects.
For example, with the model in Figure 18.9, the ﬁltering calculation just means running
a Kalman ﬁlter for the sequence of observations assigned to a given hypothesized object.
Furthermore, when changing from one association hypothesis to another, the calculations
have to be redone only for objects whose associated observations have changed. Current
MCMC data association methods can handle many hundreds of objects in real time while
giving a good approximation to the true posterior distributions.
