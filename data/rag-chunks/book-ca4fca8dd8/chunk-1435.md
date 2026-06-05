---
chunk_id: "book-ca4fca8dd8-chunk-1435"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1435
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.7
Applications of Reinforcement Learning
867
icy, NEUROGAMMON converted each move (s,a,s′) into a set of training examples, each of
which labeled s′ as a better position than some other position s′′ reachable from s by a differ-
ent move. The network had two separate halves, one for s′ and one for s′′, and was constrained
to choose which was better by comparing the outputs of the two halves. In this way, each half
was forced to learn an evaluation function ˆUθ. NEUROGAMMON won the 1989 Computer
Olympiad—the ﬁrst learning program ever to win a computer game tournament—but never
progressed past Tesauro’s own intermediate level of play.
Tesauro’s next system, TD-GAMMON (1992), adopted Sutton’s recently published TD
learning method—essentially returning to the approach explored by Samuel, but with much
greater technical understanding of how to do it right. The evaluation function ˆUθ was repre-
sented by a fully connected neural network with a single hidden layer containing 80 nodes.
(It also used some manually designed input features borrowed from NEUROGAMMON.) Af-
ter 300,000 training games, it reached a standard of play comparable to the top three human
players in the world. Kit Woolsey, a top-ten player, said, “There is no question in my mind
that its positional judgment is far better than mine.”
The next challenge was to learn from raw perceptual inputs—something closer to the real
world—rather than discrete game board representations. Beginning in 2012, a team at Deep-
Mind developed the deep Q-network (DQN) system, the ﬁrst modern deep RL system. DQN
Deep Q-network
(DQN)
uses a deep neural network to represent the Q-function; otherwise it is a typical reinforcement
learning system. DQN was trained separately on each of 49 different Atari video games. It
learned to drive simulated race cars, shoot alien spaceships, and bounce balls with paddles.
In each case, the agent learned a Q-function from raw image data with the reward signal be-
ing the game score. Overall, the system performed at roughly human expert level, although
a few games gave it trouble. One game in particular, Montezuma’s Revenge, proved far too
difﬁcult, because it required extended planning strategies, and the rewards were too sparse.
Subsequent work produced deep RL systems that generated more extensive exploratory be-
haviors and were able to conquer Montezuma’s Revenge and other difﬁcult games.
DeepMind’s ALPHAGO system also used deep reinforcement learning to beat the best
human players at the game of Go (see Chapter 6). Whereas a Q-function with no look-ahead
sufﬁces for Atari games, which are primarily reactive in nature, Go requires substantial look-
ahead. For this reason, ALPHAGO learned both a value function and a Q-function that guided
its search by predicting which moves are worth exploring. The Q-function, implemented as
a convolutional neural network, is accurate enough by itself to beat most amateur human
players without any search at all.
23.7.2 Application to robot control
The setup for the famous cart–pole balancing problem, also known as the inverted pendu-
Cart–pole
lum, is shown in Figure 23.9(a). The problem is to keep the pole roughly upright (θ ≈90◦)
Inverted pendulum
by applying forces to move the cart right or left, while keeping the position x within the limits
of the track. Several thousand papers in reinforcement learning and control theory have been
published on this seemingly simple problem. One difﬁculty is that the state variables x, θ, ˙x,
and ˙θ are continuous. The actions, however, are deﬁned to be discrete: jerk left or jerk right,
the so-called bang-bang control regime.
Bang-bang control
The earliest work on learning for this problem was carried out by Michie and Cham-
bers (1968), using a real cart and pole, not a simulation. Their BOXES algorithm was able
