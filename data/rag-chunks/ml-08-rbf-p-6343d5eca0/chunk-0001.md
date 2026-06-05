---
chunk_id: "ml-08-rbf-p-6343d5eca0-chunk-0001"
source_id: "ml-08-rbf-p-6343d5eca0"
source_file: "_ML_08_RBF_P.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1

Radial Basis Functions

## Page 2

Architecture
Input layer
Hidden layer
Output layer
x1
x2
x3
xn
h1
h2
h3
hm
z(x)
W1
W2
W3
Wm
z(x) =  wjhj(x)
hj(x) = exp( -(x-cj)2 / rj
2 )
Where 
cj is a center of a region,
 
rj is width of the receptive field

## Page 3

Architecture: Three layers
• Input layer
– Source nodes that connect to the network to its 
environment
• Hidden layer
– Hidden units provide a set of basis function
– High dimensionality
• Output layer
– Linear combination of hidden functions

## Page 4

Architecture: Radial basis function
hj(x) = exp( -(x-cj)2 / rj
2 )
z(x) =  wjhj(x)
j=1
m
Where 
cj is center of a region,
 
rj is width of the receptive field

## Page 5

5
Exact Interpolation
• Goal (exact interpolation):
– Find a function h(x) such that  
z(xn) = dn n=1, ... N
• Radial Basis Function approach:
– Use a set of N basis functions of the form (||x-xn||), one 
for each point,where (.) is some non-linear function.
– Output: z(x) = n wn (||x-xn||)
w1 (||x1-x1||) + w2 (||x1-x2||) + ... + wN (||x1-xN||) = d1
w1 (||x2-x1||) + w2 (||x2-x2||) + ... + wN (||x2-xN||) = d2
W = D
...
w1 (||xN-x1||) + w2 (||xN-x2||) + ... + wN (||xN-xN||)= dN

## Page 6

6
Exact Interpolation
z(x) = n wn (||x-xn||)

## Page 7

7
Exact Interpolation

## Page 8

8
Exact Interpolation
• Due to noise that may be present in the data 
exact interpolation is rarely useful.
• By introducing a number of modifications, we 
arrive at RBF networks:
• Complexity rather than the size of the data is what is 
important
– Number of the basis functions need not be equal to N
• Centers need not be constrained by the input
• Each basis function can have its own adjustable width
parameter 
• Bias parameter may be included in the linear sum.

## Page 9

9
Training RBF Networks
• Approach 1: Exact RBF 
• Guarantees correct classification of  all training data instances. 
• Requires N hidden layer nodes, one for each training instance. 
• No iterative training is involved: w are obtained by solving a set 
of linear equations
• Non-smooth, bad generalization

## Page 10

10
Exact Interpolation

## Page 11
