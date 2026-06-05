---
chunk_id: "book-ca4fca8dd8-chunk-1417"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1417
confidence: "first-pass"
extraction_method: "structured-local"
---

858
Chapter 23
Reinforcement Learning
As we explain in Section 23.7, deep RL has achieved very signiﬁcant results, including
learning to play a wide range of video games at an expert level, defeating the human world
champion at Go, and training robots to perform complex tasks.
Despite its impressive successes, deep RL still faces signiﬁcant obstacles: it is often
difﬁcult to get good performance and the trained system may behave very unpredictably if
the environment differs even a little from the training data. Compared to other applications
of deep learning, deep RL is rarely applied in commercial settings. It is, nonetheless, a very
active area of research.
23.4.4 Reward shaping
As noted in the introduction to this chapter, real-world environments may have very sparse
rewards: many primitive actions are required to achieve any nonzero reward. For example, a
soccer-playing robot might send a hundred thousand motor control commands to its various
joints before conceding a goal. Now it has to work out what it did wrong. The technical term
for this is the credit assignment problem. Other than playing trillions of soccer games so
Credit assignment
that the negative reward eventually propagates back to the actions responsible for it, is there
a good solution?
One common method, originally used in animal training, is called reward shaping. This
Reward shaping
involves supplying the agent with additional rewards, called pseudorewards, for “making
Pseudoreward
progress.” For example, we might give pseudorewards to the robot for making contact with
the ball or for advancing it toward the goal. Such rewards can speed up learning enormously
and are simple to provide, but there is a risk that the agent will learn to maximize the pseu-
dorewards rather than the true rewards; for example, standing next to the ball and “vibrating”
causes many contacts with the ball.
In Chapter 16 (page 559), we saw a way to modify the reward function without changing
the optimal policy. For any potential function Φ(s) and any reward function R, we can create
a new reward function R′ as follows:
R′(s,a,s′) = R(s,a,s′)+γΦ(s′)−Φ(s).
The potential fuction Φ can be constructed to reﬂect any desirable aspects of the state, such as
achievement of subgoals or distance to a desired terminal state. For example, Φ for the soccer-
playing robot could add a constant bonus for states where the robot’s team has possession and
another bonus for reducing the distance of the ball from the opponents’ goal. This will result
in faster learning overall, but will not prevent the robot from, say, learning to pass back to the
goalkeeper when danger threatens.
23.4.5 Hierarchical reinforcement learning
Another way to cope with very long action sequences is to break them up into a few smaller
pieces, and then break those into smaller pieces still, and so on until the action sequences
are short enough to make learning easy. This approach is called hierarchical reinforcement
learning (HRL), and it has much in common with the HTN planning methods described
Hierarchical
reinforcement
learning
in Chapter 11. For example, scoring a goal in soccer can be broken down into obtaining
possession, passing to a teammate, receiving the ball from a team-mate, dribbling toward
the goal, and shooting; each of these can be broken down further into lower-level motor
behaviors. Obviously, there are multiple ways of obtaining possession and shooting, multiple
