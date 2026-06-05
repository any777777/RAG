---
chunk_id: "book-ca4fca8dd8-chunk-0110"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 110
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.4
The Structure of Agents
65
Task Environment
Observable
Agents
Deterministic
Episodic
Static
Discrete
Crossword puzzle
Fully
Single
Deterministic
Sequential
Static
Discrete
Chess with a clock
Fully
Multi
Deterministic
Sequential
Semi
Discrete
Poker
Partially
Multi
Stochastic
Sequential
Static
Discrete
Backgammon
Fully
Multi
Stochastic
Sequential
Static
Discrete
Taxi driving
Partially
Multi
Stochastic
Sequential
Dynamic
Continuous
Medical diagnosis
Partially
Single
Stochastic
Sequential
Dynamic
Continuous
Image analysis
Fully
Single
Deterministic
Episodic
Semi
Continuous
Part-picking robot
Partially
Single
Stochastic
Episodic
Dynamic
Continuous
Reﬁnery controller
Partially
Single
Stochastic
Sequential
Dynamic
Continuous
English tutor
Partially
Multi
Stochastic
Sequential
Dynamic
Discrete
Figure 2.6 Examples of task environments and their characteristics.
We have not included a “known/unknown” column because, as explained earlier, this is
not strictly a property of the environment. For some environments, such as chess and poker,
it is quite easy to supply the agent with full knowledge of the rules, but it is nonetheless
interesting to consider how an agent might learn to play these games without such knowledge.
The code repository associated with this book (aima.cs.berkeley.edu) includes mul-
tiple environment implementations, together with a general-purpose environment simulator
for evaluating an agent’s performance. Experiments are often carried out not for a single
environment but for many environments drawn from an environment class. For example, to
Environment class
evaluate a taxi driver in simulated trafﬁc, we would want to run many simulations with dif-
ferent trafﬁc, lighting, and weather conditions. We are then interested in the agent’s average
performance over the environment class.
2.4 The Structure of Agents
So far we have talked about agents by describing behavior—the action that is performed after
any given sequence of percepts. Now we must bite the bullet and talk about how the insides
work. The job of AI is to design an agent program that implements the agent function—
Agent program
the mapping from percepts to actions. We assume this program will run on some sort of
computing device with physical sensors and actuators—we call this the agent architecture:
Agent architecture
agent = architecture+program.
Obviously, the program we choose has to be one that is appropriate for the architecture. If the
program is going to recommend actions like Walk, the architecture had better have legs. The
architecture might be just an ordinary PC, or it might be a robotic car with several onboard
computers, cameras, and other sensors. In general, the architecture makes the percepts from
the sensors available to the program, runs the program, and feeds the program’s action choices
to the actuators as they are generated. Most of this book is about designing agent programs,
although Chapters 26 and 27 deal directly with the sensors and actuators.
