---
chunk_id: "book-ca4fca8dd8-chunk-1373"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1373
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
835
the agent can learn a value function, a Q-function, a policy, and so on. From the point of
view of deep learning, all these are functions that can be represented by computation graphs.
For example, a value function in Go takes a board position as input and returns an estimate
of how advantageous the position is for the agent. While the methods of training in RL differ
from those of supervised learning, the ability of multilayer computation graphs to represent
complex functions over large input spaces has proved to be very useful. The resulting ﬁeld of
research is called deep reinforcement learning.
Deep reinforcement
learning
In the 1950s, Arthur Samuel experimented with multilayer representations of value func-
tions in his work on reinforcement learning for checkers, but he found that in practice a linear
function approximator worked best. (This may have been a consequence of working with a
computer roughly 100 billion times less powerful than a modern tensor processing unit.) The
ﬁrst major successful demonstration of deep RL was DeepMind’s Atari-playing agent, DQN
(Mnih et al., 2013). Different copies of this agent were trained to play each of several differ-
ent Atari video games, and demonstrated skills such as shooting alien spaceships, bouncing
balls with paddles, and driving simulated racing cars. In each case, the agent learned a Q-
function from raw image data with the reward signal being the game score. Subsequent work
has produced deep RL systems that play at a superhuman level on the majority of the 57
different Atari games. DeepMind’s ALPHAGO system also used deep RL to defeat the best
human players at the game of Go (see Chapter 6).
Despite its impressive successes, deep RL still faces signiﬁcant obstacles: it is often
difﬁcult to get good performance, and the trained system may behave very unpredictably
if the environment differs even a little from the training data (Irpan, 2018). Compared to
other applications of deep learning, deep RL is rarely applied in commercial settings. It is,
nonetheless, a very active area of research.
Summary
This chapter described methods for learning functions represented by deep computational
graphs. The main points were:
• Neural networks represent complex nonlinear functions with a network of parameter-
ized linear-threshold units.
• The back-propagation algorithm implements a gradient descent in parameter space to
minimize the loss function.
• Deep learning works well for visual object recognition, speech recognition, natural lan-
guage processing, and reinforcement learning in complex environments.
• Convolutional networks are particularly well suited for image processing and other tasks
where the data have a grid topology.
• Recurrent networks are effective for sequence-processing tasks including language mod-
eling and machine translation.
