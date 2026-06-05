---
chunk_id: "ml-05-04-ch-12-4f010d6d80-chunk-0001"
source_id: "ml-05-04-ch-12-4f010d6d80"
source_file: "_ML_05_04_Ch_12.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1

Ch 12: Back-Propagation
•
12. 1 INTRODUCTION
•
As we have seen in the previous chapter, a single-layer network has severe restrictions: 
the class of tasks that can be accomplished is very limited. 
•
In this chapter we will focus on feed forward networks with layers of processing units.
•
Minsky and Papert showed in 1969 that a two layer feed-forward network can overcome 
many restrictions, 
–
but did not present a solution to the problem of how to adjust the weights from input to hidden 
units. 
–
An answer to this question was presented by Rumelhart, Hinton and Williams in 1986, and 
similar solutions appeared to have been published earlier (Parker, 1985; Cun, 1985).
•
The  central  idea  behind  this  solution  is  that  the  errors  for  the  units  of  the  
hidden  layer  are determined by back-propagating the errors of the units of the output 
layer. 
–
For this reason the method is often  called  the  back-propagation learning  rule.  
–
Back-propagation  can  also  be  considered  as  a generalization of the delta rule for non-linear 
activation functions and multilayer networks.

## Page 2

12.2 MULTI - LAYER FEED - FORWARD NETWORKS

## Page 3

The universal approximation theorem
•
It has been shown (Cybenko, 1989; Funahashi, 1989; Hornik, 
Stinchcombe, & White, 1989; Hartman, Keeler, & Kowalski, 1990) that 
– only one layer of hidden units suffices to approximate any function with 
finitely many discontinuities to arbitrary precision, 
• provided the activation functions of the hidden units are non-linear
– In most applications a feed-forward network with a single layer of hidden 
units is used with a sigmoid activation function for the units.

## Page 4

_No reliable embedded text extracted._

## Page 5

The difference is instead of x we have y 
which is the output of the previous layer.
Generalized Delta Rule
12.3 THE GENERALISED DELTA RULE

## Page 6

True at the output layer, harder to 
find at any other layer else!!!.

## Page 7
