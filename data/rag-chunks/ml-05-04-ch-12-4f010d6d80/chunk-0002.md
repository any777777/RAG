---
chunk_id: "ml-05-04-ch-12-4f010d6d80-chunk-0002"
source_id: "ml-05-04-ch-12-4f010d6d80"
source_file: "_ML_05_04_Ch_12.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

12.3.1 Understanding Back-Propagation
•
The equations derived in the previous section may be mathematically correct, 
but what do they actually mean? 
•
Is there a way of understanding back-propagation other than reciting the 
necessary equations?
–
The answer is, of course, yes. 
•
What happens in the above equations is the following. 
–
When a learning pattern is used, 
•
the activation values are propagated to the output units, 
•
and the actual network output is compared with the desired output values, 
•
we usually end up with an error in each of the output units.
–
Lets call this error eo for a particular output unit o. We have to bring eo to zero.
–
The simplest method to do this is the greedy method: 
•
we strive to change the connections in the neural network in such a way that the error eo 
will be zero for this particular pattern.

## Page 8

•
The previous was step one. But it alone is not enough.
–
When we only apply this rule, the weights from input to hidden units are never 
changed, and therefore, we do not have the full representational power of the feed-
forward network.
•
In order to adapt the weights from input to hidden units, we again want to 
apply the delta rule. 
•
In this case, however, we do not have a value for  δ for the hidden units. The 
simplest way is to find δ  for the hidden units as follows: 
δo1
δo2
δo3
δh
who1
who2
who3
Hidden unit
Output layer

## Page 9

_No reliable embedded text extracted._

## Page 10

12.4 WORKING WITH BACK-PROPAGATION
• The application of the generalized delta rule involves two 
phases:
1) During the first phase the input x is presented and propagated 
forward through the network to compute the output values yo  for 
each output unit. 
– This output is compared with its desired value do, resulting in an error 
signal δo for each output unit.
 
 2) The second phase involves a backward pass through the network    
           during which the error signal is passed to each unit in the network   
           and appropriate weight changes are calculated.

## Page 11

_No reliable embedded text extracted._

## Page 12
