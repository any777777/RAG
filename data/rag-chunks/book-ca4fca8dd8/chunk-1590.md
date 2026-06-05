---
chunk_id: "book-ca4fca8dd8-chunk-1590"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1590
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 965

Section 26.7
Reinforcement Learning in Robotics
965
v
Cv
motion
envelope
initial
conﬁguration
Figure 26.24 The ﬁrst motion command and the resulting envelope of possible robot mo-
tions. No matter what actual motion ensues, we know the ﬁnal conﬁguration will be to the
left of the hole.
v
Cv
motion
envelope
Figure 26.25 The second motion command and the envelope of possible motions. Even with
error, we will eventually get into the hole.
leading to the robot explicitly reasoning about how much information each action might bring
when deciding what to do. While more difﬁcult computationally, such approaches have the
advantage that the robot invents its own information gathering actions rather than relying on
human-provided heuristics and scripted strategies that often lack ﬂexibility.
26.7 Reinforcement Learning in Robotics
Thus far we have considered tasks in which the robot has access to the dynamics model of
the world. In many tasks, it is very difﬁcult to write down such a model, which puts us in the
domain of reinforcement learning (RL).
One challenge of RL in robotics is the continuous nature of the state and action spaces,
which we handle either through discretization, or, more commonly, through function approxi-
mation. Policies or value functions are represented as combinations of known useful features,
or as deep neural networks. Neural nets can map from raw inputs directly to outputs, and thus
largely avoid the need for feature engineering, but they do require more data.
A bigger challenge is that robots operate in the real world. We have seen how reinforce-
ment learning can be used to learn to play chess or Go by playing simulated games. But when
a real robot moves in the real world, we have to make sure that its actions are safe (things

## Page 966
