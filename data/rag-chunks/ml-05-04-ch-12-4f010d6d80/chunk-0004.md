---
chunk_id: "ml-05-04-ch-12-4f010d6d80-chunk-0004"
source_id: "ml-05-04-ch-12-4f010d6d80"
source_file: "_ML_05_04_Ch_12.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

To illustrate the use of other activation functions we have trained a feed-forward network 
with one output unit, four hidden units, and one input with ten patterns drawn from the 
function f(x)=sin(2x)sin(x). The result is depicted in Fig. 12.4.

## Page 19

The same function is learned with a network with eight sigmoid hidden 
units (see Figure 12.5). From the figures it is clear that it pays off to use 
as much knowledge of the problem at hand as possible.

## Page 20

12.6 DEFICIENCIES OF BACK-PROPAGATION
• Despite the apparent success of the back-propagation 
learning algorithm, there are some aspects, which make the 
algorithm not guaranteed to be universally useful. 
– This can be a result of a non-optimum learning rate and 
momentum. 
– A lot of advanced algorithms based on back-propagation learning 
have some optimized method to adapt this learning rate, as will be 
discussed in the next section. 
• Training failures generally arise from two sources:
– network paralysis and 
– local minima.

## Page 21

_No reliable embedded text extracted._

## Page 22

12.6.2 Local Minima
• The error surface of a complex network is full of hills and 
valleys. Because of the gradient descent, the network  can  
get  trapped  in  a  local  minimum  when  there  is  a  much  
deeper  minimum  nearby.
– Probabilistic methods can help to avoid this trap, but they tend to 
be slow.
– Another suggested possibility is to increase the number of hidden 
units.
• But there is some upper limit of the number of hidden units 
which, when exceeded, again results in the system being 
trapped in local minima.
• It might affect the system generalization.

## Page 23

12.8 HOW GOOD ARE MULTI-LAYER FEED-FORWARD 
NETWORKS?
•
From the example shown in Fig. 12.3 it is clear that the approximation 
of the network is not perfect. The resulting approximation error is 
influenced by:
     1. The learning algorithm and number of iterations. 
- This determines how good the error on the training set is minimized.
 
2. The number of learning samples. 
 
 
- This determines how good the training samples represent the actual function.
 
3. The  number  of  hidden  units.  
 
       - This  determines  the  “expressive  power”  of  the  network.  
 
        - For “smooth” functions  only  a  few  number  of  hidden  units  
 
 
are  needed,  for wildly  fluctuating functions more hidden units
 
 
will be needed.

## Page 24
