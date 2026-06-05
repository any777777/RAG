---
chunk_id: "book-ca4fca8dd8-chunk-1385"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1385
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.1
Learning from Rewards
841
function is often (as we saw for chess) very concise and easy to specify: it requires only a
few lines of code to tell the chess agent if it has won or lost the game or to tell the car-racing
agent that it has won or lost the race or has crashed. Second, we don’t have to be experts,
capable of supplying the correct action in any situation, as would be the case if we tried to
apply supervised learning.
It turns out, however, that a little bit of expertise can go a long way in reinforcement
learning. The two examples in the preceding paragraph—the win/loss rewards for chess and
racing—are what we call sparse rewards, because in the vast majority of states the agent is
Sparse
given no informative reward signal at all. In games such as tennis and cricket, we can easily
supply additional rewards for each point won or for each run scored. In car racing, we could
reward the agent for making progress around the track in the right direction. When learning
to crawl, any forward motion is an achievement. These intermediate rewards make learning
much easier.
As long as we can provide the correct reward signal to the agent, reinforcement learning
provides a very general way to build AI systems. This is particularly true for simulated
environments, where there is no shortage of opportunities to gain experience. The addition of
deep learning as a tool within RL systems has also made new applications possible, including
learning to play Atari video games from raw visual input (Mnih et al., 2013), controlling
robots (Levine et al., 2016), and playing poker (Brown and Sandholm, 2017).
Literally hundreds of different reinforcement learning algorithms have been devised, and
many of them can employ as tools a wide range of learning methods from Chapters 19, 21, and
22. In this chapter, we cover the basic ideas and give some sense of the variety of approaches
through a few examples. We categorize the approaches as follows:
• Model-based reinforcement learning: In these approaches the agent uses a transition
Model-based
reinforcement
learning
model of the environment to help interpret the reward signals and to make decisions
about how to act. The model may be initially unknown, in which case the agent learns
the model from observing the effects of its actions, or it may already be known—for
example, a chess program may know the rules of chess even if it does not know how
to choose good moves. In partially observable environments, the transition model is
also useful for state estimation (see Chapter 14). Model-based reinforcement learning
systems often learn a utility function U(s), deﬁned (as in Chapter 16) in terms of the
sum of rewards from state s onward.2
• Model-free reinforcement learning: In these approaches the agent neither knows nor
Model-free
reinforcement
learning
learns a transition model for the environment. Instead, it learns a more direct represen-
tation of how to behave. This comes in one of two varieties:
• Action-utility learning: We introduced action-utility functions in Chapter 16. The
Action-utility
learning
most common form of action-utility learning is Q-learning, where the agent learns
Q-learning
a Q-function, or quality-function, Q(s,a), denoting the sum of rewards from state
Q-function
s onward if action a is taken. Given a Q-function, the agent can choose what to do
in s by ﬁnding the action with the highest Q-value.
• Policy search: The agent learns a policy π(s) that maps directly from states to
Policy search
actions. In the terminology of Chapter 2, this a reﬂex agent.
2
In the RL literature, which draws more on operations research than economics, utility functions are often called
value functions and denoted V(s).
