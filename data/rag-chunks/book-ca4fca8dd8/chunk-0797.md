---
chunk_id: "book-ca4fca8dd8-chunk-0797"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 797
confidence: "first-pass"
extraction_method: "structured-local"
---

480
Chapter 14
Probabilistic Reasoning over Time
dynamic aspects of the problem are essential. Blood sugar levels and measurements thereof
can change rapidly over time, depending on recent food intake and insulin doses, metabolic
activity, the time of day, and so on. To assess the current state from the history of evidence
and to predict the outcomes of treatment actions, we must model these changes.
The same considerations arise in many other contexts, such as tracking the location of a
robot, tracking the economic activity of a nation, and making sense of a spoken or written
sequence of words. How can dynamic situations like these be modeled?
14.1.1 States and observations
This chapter discusses discrete-time models, in which the world is viewed as a series of
Discrete time
snapshots or time slices.1 We’ll just number the time slices 0, 1, 2, and so on, rather than
Time slice
assigning speciﬁc times to them. Typically, the time interval ∆between slices is assumed to
be the same for every interval. For any particular application, a speciﬁc value of ∆has to be
chosen. Sometimes this is dictated by the sensor; for example, a video camera might supply
images at intervals of 1/30 of a second. In other cases, the interval is dictated by the typical
rates of change of the relevant variables; for example, in the case of blood glucose monitoring,
things can change signiﬁcantly in the course of ten minutes, so a one-minute interval might
be appropriate. On the other hand, in modeling continental drift over geological time, an
interval of a million years might be ﬁne.
Each time slice in a discrete-time probability model contains a set of random variables,
some observable and some not. For simplicity, we will assume that the same subset of vari-
ables is observable in each time slice (although this is not strictly necessary in anything that
follows). We will use Xt to denote the set of state variables at time t, which are assumed to
be unobservable, and Et to denote the set of observable evidence variables. The observation
at time t is Et =et for some set of values et.
Consider the following example: You are the security guard stationed at a secret under-
ground installation. You want to know whether it’s raining today, but your only access to the
outside world occurs each morning when you see the director coming in with, or without,
an umbrella. For each day t, the set Et thus contains a single evidence variable Umbrellat
or Ut for short (whether the umbrella appears), and the set Xt contains a single state vari-
able Raint or Rt for short (whether it is raining). Other problems can involve larger sets of
variables. In the diabetes example, the evidence variables might be MeasuredBloodSugart
and PulseRatet while the state variables might include BloodSugart and StomachContentst.
(Notice that BloodSugart and MeasuredBloodSugart are not the same variable; this is how
we deal with noisy measurements of actual quantities.)
We will assume that the state sequence starts at t =0 and evidence starts arriving at t =1.
Hence, our umbrella world is represented by state variables R0, R1, R2,... and evidence vari-
ables U1, U2,.... We will use the notation a:b to denote the sequence of integers from a to
b inclusive and the notation Xa:b to denote the set of variables from Xa to Xb inclusive. For
example, U1:3 corresponds to U1, U2, U3. (Note that this is different from the notation used in
programming languages such as Python and Go, where U[1:3] would not include U[3].)
1
Uncertainty over continuous time can be modeled by stochastic differential equations (SDEs). The models
studied in this chapter can be viewed as discrete-time approximations to SDEs.
