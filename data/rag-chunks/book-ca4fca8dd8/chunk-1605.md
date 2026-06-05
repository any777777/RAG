---
chunk_id: "book-ca4fca8dd8-chunk-1605"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1605
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 974

974
Chapter 26
Robotics
Figure 26.30 A human teacher pushes the robot down to teach it to stay closer to the ta-
ble. The robot appropriately updates its understanding of the desired cost function and starts
optimizing it. Courtesy of Anca Dragan. See Bajcsy et al. (2017).
Figure 26.31 A programming interface that involves placing specially designed blocks in
the robot’s workspace to select objects and specify high-level actions. Images courtesy of
Maya Cakmak. See Seﬁdgar et al. (2017).
The ALVINN autonomous car project used this approach, and found that even when
starting from a state in D, π will make small errors, which will take the car off the demon-
strated trajectory. There, π will make a larger error, which will take the car even further off
the desired course.
We can address this at training time if we interleave collecting labels and learning: start
with a demonstration, learn a policy, then roll out that policy and ask the human for what
action to take at every state along the way, then repeat. The robot then learns how to correct
its mistakes as it deviates from the human’s desired actions.
Alternatively, we can address it by leveraging reinforcement learning. The robot can ﬁt a
dynamics model based on the demonstrations, and then use optimal control (Section 26.5.4)
to generate a policy that optimizes for staying close to the demonstration. A version of this
has been used to perform very challenging maneuvers at an expert level in a small radio-
controlled helicopter (see Figure 23.9(b)).
The DAGGER (Data Aggregation) system starts with a human expert demonstration.
From that it learns a policy, π1 and uses the policy to generate a data set D. Then from
D it generates a new policy π2 that best imitates the original human data. This repeats, and

## Page 975
