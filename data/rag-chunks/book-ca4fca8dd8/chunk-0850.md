---
chunk_id: "book-ca4fca8dd8-chunk-0850"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 850
confidence: "first-pass"
extraction_method: "structured-local"
---

514
Chapter 14
Probabilistic Reasoning over Time
The chance that the initial guesses are all correct is 2−42 or about 2×10−13, so it is
vanishingly unlikely that a thousand particles (or even a million particles) will include one
with the correct dirt map. Typically, the best particle out of a thousand will get about 32 right
and 10 wrong, and usually there will be only one such particle, or perhaps a handful. One
of those best particles will come to dominate the total likelihood as time progresses and the
diversity of the population of particles will collapse. Then, because all the particles agree on
a single, incorrect map, the algorithm becomes convinced that that map is correct and never
changes its mind.
Fortunately, the problem of simultaneous localization and mapping has a special struc-
ture: conditioned on the sequence of robot locations, the dirt statuses of the individual squares
are independent (Exercise 14.RBPF). More speciﬁcally,
P(Dirt1,0:t,...,Dirt42,0:t |DirtSensor1:t,WallSensor1:t,Location1:t)
= ∏
i
P(Dirti,0:t |DirtSensor1:t,Location1:t).
(14.24)
This means it is useful to apply a statistical trick called Rao-Blackwellization, which is based
Rao-Blackwellization
on the simple idea that exact inference is always more accurate than sampling, even if it’s only
for a subset of the variables. (See Exercise 14.RAOB.) For the SLAM problem, we run particle
ﬁltering on the robot location and then, for each particle, we run exact HMM inference for
each dirt square independently, conditioned on the location sequence in that particle. Each
particle therefore contains a sampled location plus 42 exact marginal posteriors for the 42
squares—exact, that is, assuming that the hypothesized location trajectory followed by that
particle is correct. This approach, called the Rao-Blackwellized particle ﬁlter, handles the
Rao-Blackwellized
particle ﬁlter
case of deterministic dirt with no difﬁculty, gradually building an exact dirt map with either
exact location sensing or noisy wall sensing, as shown in Figure 14.21(b).
In cases that do not satisfy the kind of conditional independence structure exempliﬁed by
Equation (14.24), Rao-Blackwellization is not applicable. The notes at the end of the chapter
mention a number of algorithms that have been proposed to handle the general problem of
ﬁltering with static variables. None has the elegance and broad applicability of the particle
ﬁlter, but several are effective in practice on certain classes of problems.
Summary
This chapter has addressed the general problem of representing and reasoning about proba-
bilistic temporal processes. The main points are as follows:
• The changing state of the world is handled by using a set of random variables to repre-
sent the state at each point in time.
• Representations can be designed to (roughly) satisfy the Markov property, so that the
future is independent of the past given the present. Combined with the assumption that
the process is time-homogeneous, this greatly simpliﬁes the representation.
• A temporal probability model can be thought of as containing a transition model de-
scribing the state evolution and a sensor model describing the observation process.
• The principal inference tasks in temporal models are ﬁltering (state estimation), pre-
diction, smoothing, and computing the most likely explanation. Each of these tasks
