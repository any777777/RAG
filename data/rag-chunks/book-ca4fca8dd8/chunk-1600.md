---
chunk_id: "book-ca4fca8dd8-chunk-1600"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1600
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.8
Humans and Robots
971
(a)
(b)
Figure 26.28 (a) Left: An autonomous car (middle lane) predicts that the human driver (left
lane) wants to keep going forward, and plans a trajectory that slows down and merges behind.
Right: The car accounts for the inﬂuence its actions can have on human actions, and realizes
it can merge in front and rely on the human driver to slow down. (b) That same algorithm
produces an unusual strategy at an intersection: the car realizes that it can make it more
likely for the person (bottom) to proceed faster through the intersection by starting to inch
backwards. Images courtesy of Anca Dragan. See Sadigh et al. (2016).
Human predictions about the robot
Incomplete information is often two-sided: the robot does not know the human’s objective
and the human, in turn, does not know the robot’s objective—people need to be making
predictions about robots. As robot designers, we are not in charge of how the human makes
predictions; we can only control what the robot does. However, the robot can act in a way
to make it easier for the human to make correct predictions. The robot can assume that
the human is using something roughly analogous to Equation (26.8) to estimate the robot’s
objective JR, and thus the robot will act so that its true objective can be easily inferred.
A special case of the game is when the human and the robot are on the same team,
working toward the same goal or objective: JH = JR. Imagine getting a personal home robot
that is helping you make dinner or clean up—these are examples of collaboration.
We can now deﬁne a joint agent whose actions are tuples of human–robot actions,
Joint agent
(uH,uR) and who optimizes for JH(x,uH,uR) = JR(x,uR,uH), and we’re solving a regular
planning problem. We compute the optimal plan or policy for the joint agent, and voila, we
now know what the robot and human should do.
This would work really well if people were perfectly optimal. The robot would do its part
of the joint plan, the human theirs. Unfortunately, in practice, people don’t seem to follow
the perfectly laid out joint-agent plan; they have a mind of their own! We’ve already learned
one way to handle this though, back in Section 26.6. We called it model predictive control
(MPC): the idea was to come up with a plan, execute the ﬁrst action, and then replan. That
way, the robot always adapts its plan to what the human is actually doing.
Let’s work through an example. Suppose you and the robot are in your kitchen, and have
decided to make wafﬂes. You are slightly closer to the fridge, so the optimal joint plan would
