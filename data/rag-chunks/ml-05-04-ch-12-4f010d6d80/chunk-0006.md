---
chunk_id: "ml-05-04-ch-12-4f010d6d80-chunk-0006"
source_id: "ml-05-04-ch-12-4f010d6d80"
source_file: "_ML_05_04_Ch_12.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 6
confidence: "first-pass"
extraction_method: "structured-local"
---

• A low learning error on the (small) learning set is no 
guarantee for a good network performance!
• With increasing number of learning samples the two error 
rates converge to the same value. 
– This value depends on the representational power of the network: 
given the optimal weights, how good is the approximation. 
– This error depends on the number of hidden units and the 
activation function. 
• If the learning error rate does not converge to the test error 
rate the learning procedure has not found a global 
minimum.

## Page 31

12.8.2 The Effect of the Number of Hidden Units
•
The same function as in the previous subsection is used, but now the 
number of hidden units is varied.
•
The original (desired) function, learning samples and network 
approximation is shown in Fig. 12.9A for 5 hidden units and in Fig. 
12.9B for 20 hidden units. 
•
The effect visible in Fig. 12.9B is called over training.
– The network fits exactly with the learning samples, but because of the 
large number of hidden units the function which is actually represented by 
the network is far more wild than the original one.

## Page 32

_No reliable embedded text extracted._

## Page 33

•
Particularly in case of learning samples which contain a certain amount 
of noise (which all real-world data have), the network will “fit the 
noise” of the learning samples instead of making a smooth 
approximation.
•
This example shows that a large number of hidden units leads to a 
small error on the training set but not necessarily leads to a small error 
on the test set. 
•
Adding hidden units will always lead to a reduction of the Elearning.
– However, adding hidden units will first lead to a reduction of the Etest, but 
then lead to an increase of  Etest. 
– This effect is called the peaking effect. 
•
The average learning and test error rates as a function of the learning 
set size are given in Fig. 12.10.

## Page 34

_No reliable embedded text extracted._

## Page 35
