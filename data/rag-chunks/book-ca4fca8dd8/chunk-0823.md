---
chunk_id: "book-ca4fca8dd8-chunk-0823"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 823
confidence: "first-pass"
extraction_method: "structured-local"
---

496
Chapter 14
Probabilistic Reasoning over Time
 0
 1
 2
 3
 4
 5
 6
 7
 0
 5
 10
 15
 20
 25
 30
 35
 40
Localization error
Number of observations
ε = 0.40
ε = 0.20
ε = 0.10
ε = 0.05
ε = 0.02
ε = 0.00
 0
 1
 2
 3
 4
 5
 6
 7
 8
 9
 10
 0
 5
 10
 15
 20
 25
 30
 35
 40
Viterbi path error
Number of observations
ε = 0.40
ε = 0.20
ε = 0.10
ε = 0.05
ε = 0.02
ε = 0.00
(a)
(b)
Figure 14.8 Performance of HMM localization as a function of the length of the observation
sequence for various different values of the sensor error probability ϵ; data averaged over 400
runs. (a) The localization error, deﬁned as the Manhattan distance from the true location. (b)
The Viterbi path error, deﬁned as the average Manhattan distance of states on the Viterbi path
from corresponding states on the true path.
on the location sequence by the transition model. When ϵ is 0.10 or less, the robot needs
only a few observations to work out where it is and to track its position accurately. When
ϵ is 0.40, both the localization error and the Viterbi path error remain large; in other words,
the robot is lost. This is because a sensor with an error probability of 0.40 provides too little
information to counteract the loss of information about the robot’s position that comes from
the unpredictable random motion.
The state variable for the example we have considered in this section is a physical loca-
tion in the world. Other problems can, of course, include other aspects of the world. Exer-
cise 14.ROOM asks you to consider a version of the vacuum robot that has the policy of going
straight for as long as it can; only when it encounters an obstacle does it change to a new
heading. To model this robot, each state in the model consists of a (location, heading) pair.
For the environment in Figure 14.7, which has 42 empty squares, this leads to 168 states and
a transition matrix with 1682 =28,224 entries—still a manageable number.
If we add the possibility of dirt in each of the 42 squares, the number of states is multiplied
by 242 and the transition matrix has more than 1029 entries—no longer a manageable number.
In general, if the state is composed of n discrete variables with at most d values each, the
corresponding HMM transition matrix will have size O(d2n) and the per-update computation
time will also be O(d2n).
For these reasons, although HMMs have many uses in areas ranging from speech recogni-
tion to molecular biology, they are fundamentally limited in their ability to represent complex
processes. In the terminology introduced in Chapter 2, HMMs are an atomic representation:
states of the world have no internal structure and are simply labeled by integers. Section 14.5
shows how to use dynamic Bayesian networks—a factored representation—to model domains
with many state variables. The next section shows how to handle domains with continuous
state variables, which of course lead to an inﬁnite state space.
