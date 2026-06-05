---
chunk_id: "book-ca4fca8dd8-chunk-0247"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 247
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 152

152
Chapter 4
Search in Complex Environments
(a) Possible locations of robot after  E1 = 1011
(b) Possible locations of robot after  E1 = 1011, E2 = 1010
Figure 4.18 Possible positions of the robot, ⊙, (a) after one observation, E1 =1011, and
(b) after moving one square and making a second observation, E2 =1010. When sensors are
noiseless and the transition model is accurate, there is only one possible location for the robot
consistent with this sequence of two observations.
where in the corridor(s) it was. But for environments with reasonable variation in geography,
localization often converges quickly to a single point, even when actions are nondeterministic.
What happens if the sensors are faulty? If we can reason only with Boolean logic, then we
have to treat every sensor bit as being either correct or incorrect, which is the same as having
no perceptual information at all. But we will see that probabilistic reasoning (Chapter 12),
allows us to extract useful information from a faulty sensor as long as it is wrong less than
half the time.
4.5 Online Search Agents and Unknown Environments
So far we have concentrated on agents that use ofﬂine search algorithms. They compute
Oﬄine search
a complete solution before taking their ﬁrst action. In contrast, an online search8 agent
Online search
interleaves computation and action: ﬁrst it takes an action, then it observes the environment
and computes the next action. Online search is a good idea in dynamic or semi-dynamic
environments, where there is a penalty for sitting around and computing too long. Online
8
The term “online” here refers to algorithms that must process input as it is received rather than waiting for the
entire input data set to become available. This usage of “online” is unrelated to the concept of “having an Internet
connection.”

## Page 153
