---
chunk_id: "book-ca4fca8dd8-chunk-1547"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1547
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 933

Section 26.2
Robot Hardware
933
(a)
(b)
Figure 26.1 (a) An industrial robotic arm with a custom end-effector. Image credit: Ma-
cor/123RF. (b) A Kinova® JACO® Assistive Robot arm mounted on a wheelchair. Kinova
and JACO are trademarks of Kinova, Inc.
learned in simulation to a real robot in the real world—the sim-to-real problem—is an active
area of research. Practical robotic systems need to embody prior knowledge about the robot,
the physical environment, and the tasks to be performed so that the robot can learn quickly
and perform safely.
Robotics brings together many of the concepts we have seen in this book, including prob-
abilistic state estimation, perception, planning, unsupervised learning, reinforcement learn-
ing, and game theory. For some of these concepts robotics serves as a challenging example
application. For other concepts this chapter breaks new ground, for instance in introducing
the continuous version of techniques that we previously saw only in the discrete case.
26.2 Robot Hardware
So far in this book, we have taken the agent architecture—sensors, effectors, and processors—
as given, and have concentrated on the agent program. But the success of real robots depends
at least as much on the design of sensors and effectors that are appropriate for the task.
26.2.1 Types of robots from the hardware perspective
When you think of a robot, you might imagine something with a head and two arms, moving
around on legs or wheels. Such anthropomorphic robots have been popularized in ﬁction
Anthropomorphic
robot
such as the movie The Terminator and the cartoon The Jetsons. But real robots come in many
shapes and sizes.
Manipulators are just robot arms. They do not necessarily have to be attached to a robot
Manipulator
body; they might simply be bolted onto a table or a ﬂoor, as they are in factories (Figure 26.1
(a)). Some have a large payload, like those assembling cars, while others, like wheelchair-
mountable arms that assist people with motor impairments (Figure 26.1(b)), can carry less
but are safer in human environments.

## Page 934
