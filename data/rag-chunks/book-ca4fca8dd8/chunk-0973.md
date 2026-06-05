---
chunk_id: "book-ca4fca8dd8-chunk-0973"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 973
confidence: "first-pass"
extraction_method: "structured-local"
---

588
Chapter 16
Making Complex Decisions
More recent work in AI has focused on point-based value iteration methods that, at each
iteration, generate conditional plans and α-vectors for a ﬁnite set of belief states rather than
for the entire belief space. Lovejoy (1991) proposed such an algorithm for a ﬁxed grid of
points, an approach taken also by Bonet (2002). An inﬂuential paper by Pineau et al. (2003)
suggested generating reachable points by simulating trajectories in a somewhat greedy fash-
ion; Spaan and Vlassis (2005) observe that one need generate plans for only a small, randomly
selected subset of points to improve on the plans from the previous iteration for all points in
the set. Shani et al. (2013) survey these and other developments in point-based algorithms,
which have led to good solutions for problems with thousands of states. Because POMDPs
are PSPACE-hard (Papadimitriou and Tsitsiklis, 1987), further progress on ofﬂine solution
methods may require taking advantage of various kinds of structure in value functions arising
from a factored representation of the model.
The online approach for POMDPs—using look-ahead search to select an action for the
current belief state—was ﬁrst examined by Satia and Lave (1973). The use of sampling at
chance nodes was explored analytically by Kearns et al. (2000) and Ng and Jordan (2000).
The POMCP algorithm is due to Silver and Veness (2011).
With the development of reasonably effective approximation algorithms for POMDPs,
their use as models for real-world problems has increased, particularly in education (Rafferty
et al., 2016), dialog systems (Young et al., 2013), robotics (Hsiao et al., 2007; Huynh and
Roy, 2009), and self-driving cars (Forbes et al., 1995; Bai et al., 2015). An important large-
scale application is the Airborne Collision Avoidance System X (ACAS X), which keeps
airplanes and drones from colliding midair. The system uses POMDPs with neural networks
to do function approximation. ACAS X signiﬁcantly improves safety compared to the legacy
TCAS system, which was built in the 1970s using expert system technology (Kochenderfer,
2015; Julian et al., 2018).
Complex decision making has also been studied by economists and psychologists. They
ﬁnd that decision makers are not always rational, and may not be operating exactly as de-
scribed by the models in this chapter. For example, when given a choice, a majority of people
prefer $100 today over a guarantee of $200 in two years, but those same people prefer $200
in eight years over $100 in six years. One way to interpret this result is that people are not
using additive exponentially discounted rewards; perhaps they are using hyperbolic rewards
Hyperbolic reward
(the hyperbolic function dips more steeply in the near term than does the exponential decay
function). This and other possible interpretations are discussed by Rubinstein (2003).
The texts by Bertsekas (1987) and Puterman (1994) provide rigorous introductions to
sequential decision problems and dynamic programming. Bertsekas and Tsitsiklis (1996)
include coverage of reinforcement learning. Sutton and Barto (2018) cover similar ground
but in a more accessible style. Sigaud and Buffet (2010), Mausam and Kolobov (2012) and
Kochenderfer (2015) cover sequential decision making from an AI perspective. Krishna-
murthy (2016) provides thorough coverage of POMDPs.
