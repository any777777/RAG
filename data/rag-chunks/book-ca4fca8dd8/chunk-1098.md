---
chunk_id: "book-ca4fca8dd8-chunk-1098"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1098
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 656

656
Chapter 18
Probabilistic Programming
2
1
3
5
4
2
1
3
5
4
3
(d)
(c)
(b)
(a)
track termination
false alarm
detection
failure
track
initiation
3
2
1
5
4
2
1
5
4
5
4
2
1
3
4
5
1
2
3
4
5
1
2
3
4
5
3
2
1
Figure 18.8 (a) Observations made of object locations in 2D space over ﬁve time steps. Each
observation blip is labeled with the time step but does not identify the object that produced it.
(b–c) Possible hypotheses about the underlying object tracks. (d) A hypothesis for the case
in which false alarms, detection failures, and track initiation/termination are possible.
18.3.1 Example: Multitarget tracking
The data association problem was studied originally in the context of radar tracking of mul-
tiple targets, where reﬂected pulses are detected at ﬁxed time intervals by a rotating radar
antenna. At each time step, multiple blips may appear on the screen, but there is no direct
observation of which blips at time t correspond to which blips at time t −1. Figure 18.8(a)
shows a simple example with two blips per time step for ﬁve steps. Each blip is labeled with
its time step but lacks any identifying information.
Let us assume, for the time being, that we know there are exactly two aircraft, A1 and
A2, generating the blips. In the terminology of OUPMs, A1 and A2 are guaranteed objects,
Guaranteed object
meaning that they are guaranteed to exist and to be distinct; moreover, in this case, there
are no other objects. (In other words, as far as aircraft are concerned, this scenario matches
the database semantics that is assumed in RPMs.) Let their true positions be X(A1,t) and
X(A2,t), where t is a nonnegative integer that indexes the sensor update times. We assume
the ﬁrst observation arrives at t =1, and at time 0 the prior distribution for every aircraft’s
location is InitX(). Just to keep things simple, we’ll also assume that each aircraft moves
independently according to a known transition model—e.g., a linear–Gaussian model as used
in the Kalman ﬁlter (Section 14.4).
The ﬁnal piece is the sensor model: again, we assume a linear–Gaussian model where an
aircraft at position x produces a blip b whose observed blip position Z(b) is a linear function
of x with added Gaussian noise. Each aircraft generates exactly one blip at each time step, so

## Page 657
