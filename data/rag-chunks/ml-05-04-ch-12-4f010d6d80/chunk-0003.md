---
chunk_id: "ml-05-04-ch-12-4f010d6d80-chunk-0003"
source_id: "ml-05-04-ch-12-4f010d6d80"
source_file: "_ML_05_04_Ch_12.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

12.4.2 Learning Rate And Momentum
•
The learning procedure requires that the change in weight is proportional to 
dE/dw. 
•
True gradient descent requires that extremely small steps are taken. 
•
The constant of proportionality is the learning rate γ. 
•
For practical purposes we choose a learning rate that is as large as possible 
without leading to oscillation.
•
One way to avoid oscillation at large gamma, is to make the change in weight 
dependent of the past weight change by adding a momentum term:
where t indexes the presentation number and α is a constant which determines 
the effect of the previous weight change.

## Page 13

12.4.3 Learning Per Pattern
• The learning rule is applied to each pattern separately, i.e., 
when a pattern p is applied, Ep is calculated, and the 
weights are adapted (p = 1, 2, ., P). 
• Care has to be taken, however, with the order in which the 
patterns are taught. 
– For example, when using the same sequence over and over again 
the network may become focused on the first few patterns. 
– This problem can be overcome by using a permuted training 
method.

## Page 14

Example 12.1
•
A feed-forward network can be used to approximate a function from examples. 
•
Suppose we have a system (for example a chemical process or a financial 
market) of which we want to know the characteristics. 
•
The input of the system is given by the two-dimensional vector x and the 
output is given by the one-dimensional vector d. 
•
We want to estimate the relationship d = f(x) from 80 examples {xp, dp} as 
depicted in Fig. 12.3 (top left). 
•
A feed-forward network was programmed with 2 inputs units, 10 hidden units 
with sigmoid activation function and an output unit with a linear activation 
function. 
•
The network weights are initialized to small values and the network is trained 
for 5,000 learning iterations with the back-propagation training rule, described 
in the previous section.

## Page 15

Example 12.1
•
The relationship between x and d as represented by the network is 
shown in Fig. 12.3 (top right).
•
The function which generated the learning samples is given in Fig. 
12.3 (bottom left). 
•
The approximation error is depicted in Fig. 12.3 (bottom right). 
•
We see that the error is higher at the edges. 
•
The network is considerably better at interpolation than extrapolation.

## Page 16

_No reliable embedded text extracted._

## Page 17

_No reliable embedded text extracted._

## Page 18
