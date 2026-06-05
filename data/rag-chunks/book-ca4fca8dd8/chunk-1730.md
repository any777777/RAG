---
chunk_id: "book-ca4fca8dd8-chunk-1730"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1730
confidence: "first-pass"
extraction_method: "structured-local"
---

1054
Chapter 28
Philosophy, Ethics, and Safety of AI
• Monitor the resource with accountable monitors.
• Sanctions, proportional to the severity of the violation.
• Easy conﬂict resolution procedures.
• Hierarchical control for large shared resources.
Victoria Krakovna (2018) has cataloged examples of AI agents that have gamed the system,
ﬁguring out how to maximize utility without actually solving the problem that their designers
intended them to solve. To the designers this looks like cheating, but to the agents, they
are just doing their job. Some agents took advantage of bugs in the simulation (such as
ﬂoating point overﬂow bugs) to propose solutions that would not work once the bug was
ﬁxed. Several agents in video games discovered ways to crash or pause the game when they
were about to lose, thus avoiding a penalty. And in a speciﬁcation where crashing the game
was penalized, one agent learned to use up just enough of the game’s memory so that when it
was the opponent’s turn, it would run out of memory and crash the game. Finally, a genetic
algorithm operating in a simulated world was supposed to evolve fast-moving creatures but
in fact produced creatures that were enormously tall and moved fast by falling over.
Designers of agents should be aware of these kinds of speciﬁcation failures and take steps
to avoid them. To help them do that, Krakovna was part of the team that released the AI Safety
Gridworlds environments (Leike et al., 2017), which allows designers to test how well their
agents perform.
The moral is that we need to be very careful in specifying what we want, because with
utility maximizers we get what we actually asked for. The value alignment problem is the
Value alignment
problem
problem of making sure that what we ask for is what we really want; it is also known as the
King Midas problem, as discussed on page 51. We run into trouble when a utility function
fails to capture background societal norms about acceptable behavior. For example, a human
who is hired to clean ﬂoors, when faced with a messy person who repeatedly tracks in dirt,
knows that it is acceptable to politely ask the person to be more careful, but it is not acceptable
to kidnap or incapacitate said person.
A robotic cleaner needs to know these things too, either through explicit programming or
by learning from observation. Trying to write down all the rules so that the robot always does
the right thing is almost certainly hopeless. We have been trying to write loophole-free tax
laws for several thousand years without success. Better to make the robot want to pay taxes,
so to speak, than to try to make rules to force it to do so when it really wants to do something
else. A sufﬁciently intelligent robot will ﬁnd a way to do something else.
Robots can learn to conform better with human preferences by observing human behav-
ior. This is clearly related to the notion of apprenticeship learning (Section 23.6). The robot
may learn a policy that directly suggests what actions to take in what situations; this is often
a straightforward supervised learning problem if the environment is observable. For exam-
ple, a robot can watch a human playing chess: each state–action pair is an example for the
learning process. Unfortunately, this form of imitation learning means that the robot will
repeat human mistakes. Instead, the robot can apply inverse reinforcement learning to dis-
cover the utility function that the humans must be operating under. Watching even terrible
chess players is probably enough for the robot to learn the objective of the game. Given just
this information, the robot can then go on to exceed human performance—as, for example,
ALPHAZERO did in chess—by computing optimal or near-optimal policies from the objec-
