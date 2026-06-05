---
chunk_id: "book-ca4fca8dd8-chunk-1604"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1604
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.8
Humans and Robots
973
Figure 26.29 Left: A mobile robot is shown a demonstration that stays on the dirt road.
Middle: The robot infers the desired cost function, and uses it in a new scene, knowing to
put lower cost on the road there. Right: The robot plans a path for the new scene that also
stays on the road, reproducing the preferences behind the demonstration. Images courtesy of
Nathan Ratliff and James A. Bagnell. See Ratliff et al. (2006).
We have actually already seen the answer to this back in Section 26.8.1. There, the setup
was a little different: we had another person taking actions in the same space as the robot, and
the robot needed to predict what the person would do. But one technique we went over for
making these predictions was to assume that people act to noisily optimize some cost function
JH, and we can use their ongoing actions as evidence about what cost function that is. We
can do the same here, except not for the purpose of predicting human behavior in the future,
but rather acquiring the cost function the robot itself should optimize. If the person drives
defensively, the cost function that will explain their actions will put a lot of weight on safety
and less so on efﬁciency. The robot can adopt this cost function as its own and optimize it
when driving the car itself.
Roboticists have experimented with different algorithms for making this cost inference
computationally tractable. In Figure 26.29, we see an example of teaching a robot to prefer
staying on the road to going over the grassy terrain. Traditionally in such methods, the cost
function has been represented as a combination of hand-crafted features, but recent work has
also studied how to represent it using a deep neural network, without feature engineering.
There are other ways for a person to provide input. A person could use language rather
than demonstration to instruct the robot. A person could act as a critic, watching the robot
perform a task one way (or two ways) and then saying how well the task was done (or which
way was better), or giving advice on how to improve.
Learning policies directly via imitation
An alternative is to bypass cost functions and learn the desired robot policy directly. In our
car example, the human’s demonstrations make for a convenient data set of states labeled by
the action the robot should take at each state: D = {(xi,ui)}. The robot can run supervised
learning to ﬁt a policy π : x 7→u, and execute that policy. This is called imitation learning or
behavioral cloning.
Behavioral cloning
A challenge with this approach is in generalization to new states. The robot does not
Generalization
know why the actions in its database have been marked as optimal. It has no causal rule; all
it can do is run a supervised learning algorithm to try to learn a policy that will generalize to
unknown states. However, there is no guarantee that the generalization will be correct.
