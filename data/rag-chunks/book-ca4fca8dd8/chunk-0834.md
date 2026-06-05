---
chunk_id: "book-ca4fca8dd8-chunk-0834"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 834
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 504

504
Chapter 14
Probabilistic Reasoning over Time
P(R1|R0)
R0
R1
P(U1|R1)
Figure 14.13 Left: Speciﬁcation of the prior, transition model, and sensor model for the
umbrella DBN. Subsequent slices are copies of slice 1. Right: A simple DBN for robot
motion in the X–Y plane.
is always a single multivariate Gaussian distribution—that is, a single “bump” in a particular
location. DBNs, on the other hand, can model arbitrary distributions.
For many real-world applications, this ﬂexibility is essential. Consider, for example, the
current location of my keys. They might be in my pocket, on the bedside table, on the kitchen
counter, dangling from the front door, or locked in the car. A single Gaussian bump that
included all these places would have to allocate signiﬁcant probability to the keys being in
mid-air above the front garden. Aspects of the real world such as purposive agents, obstacles,
and pockets introduce “nonlinearities” that require combinations of discrete and continuous
variables in order to get reasonable models.
14.5.1 Constructing DBNs
To construct a DBN, one must specify three kinds of information: the prior distribution over
the state variables, P(X0); the transition model P(Xt+1 |Xt); and the sensor model P(Et |Xt).
To specify the transition and sensor models, one must also specify the topology of the con-
nections between successive slices and between the state and evidence variables. Because
the transition and sensor models are assumed to be time-homogeneous—the same for all t—
it is most convenient simply to specify them for the ﬁrst slice. For example, the complete
DBN speciﬁcation for the umbrella world is given by the three-node network shown in Fig-
ure 14.13(a). From this speciﬁcation, the complete DBN with an unbounded number of time
slices can be constructed as needed by copying the ﬁrst slice.
Let us now consider a more interesting example: monitoring a battery-powered robot
moving in the X–Y plane, as introduced at the end of Section 14.1. First, we need state
variables, which will include both Xt =(Xt,Yt) for position and ˙Xt =( ˙Xt, ˙Yt) for velocity. We
assume some method of measuring position—perhaps a ﬁxed camera or onboard GPS (Global
Positioning System)—yielding measurements Zt. The position at the next time step depends
on the current position and velocity, as in the standard Kalman ﬁlter model. The velocity at
the next step depends on the current velocity and the state of the battery. We add Batteryt to
