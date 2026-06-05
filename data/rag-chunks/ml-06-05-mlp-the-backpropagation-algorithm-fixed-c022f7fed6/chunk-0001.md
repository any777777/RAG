---
chunk_id: "ml-06-05-mlp-the-backpropagation-algorithm-fixed-c022f7fed6-chunk-0001"
source_id: "ml-06-05-mlp-the-backpropagation-algorithm-fixed-c022f7fed6"
source_file: "_ML_06_05 - MLP - The Backpropagation Algorithm_Fixed.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1

Introduction
• As we have seen in the previous lecture, the 
weights of the neural network are responsible for 
the learning capabilities of the neural network.
• These weights need to be updated through a 
process called training in order to store the 
experiential knowledge of the neural network.
• The backpropagation (BP) algorithm is the most 
basic algorithm for training neural networks.

## Page 2

The BP Algorithm
• Lets begin with an example of a neural 
network and work our way towards 
understanding the algorithm.
• Consider a neural network shown in the next 
slide.
• The three-layer network consists of an input 
layer (2 units), a hidden layer (2 units) and an 
output layer (1 unit).

## Page 3

The BP Algorithm
• The activation function for the hidden and 
output layers is the sigmoid activation 
function.
                   F(s)=1/(1+exp(-s))
• For simplicity, lets remove the bias 
connections.

## Page 4

The BP Algorithm
A
B
θ
Ω
λ
𝑤Ω𝐴
𝑤Ω𝐵
𝑤𝜆𝐴
𝑤𝜆𝐵
𝑤𝐴𝜃
𝑤𝐵

## Page 5

The BP Algorithm
• Prior to training, the weights are typically set 
at random values between -1 and +1.
• Lets assume that the weights are as in the 
next slide.

## Page 6

The BP Algorithm
A
B
θ
Ω
λ
0.1
0.4
0.8
0.6
0.3
0.9
𝑜𝑢𝑡𝑝𝑢𝑡
𝑖𝑛𝑝𝑢𝑡1
𝑖𝑛𝑝𝑢𝑡2

## Page 7

The BP Algorithm
• The first step in the BP algorithm is to perform 
a forward pass on the network based on the 
training inputs.
• The forward pass is required to estimate the 
error, which is the difference between the 
target (from the training set) and the 
estimated output (from the neural network).
• For this example, lets consider the target 
output as 0.5.

## Page 8

The BP Algorithm: Forward Pass
A
B
θ
Ω
λ
𝑤Ω𝐴
𝑤Ω𝐵
𝑤𝜆𝐴
𝑤𝜆𝐵
𝑤𝐴𝜃
𝑤𝐵𝜃
0.35
0.90
𝑜𝑢𝑡𝑝𝑢𝑡
(𝑑𝑒𝑠𝑖𝑟𝑒𝑑𝑜𝑢𝑡𝑝𝑢𝑡= 0.5)

## Page 9

The BP Algorithm: Forward Pass
Input to A:
𝑖𝑛𝑝𝑢𝑡𝐴= 𝑤Ω𝐴Ωo + 𝑤𝜆𝐴𝜆o
Input to B:
𝑖𝑛𝑝𝑢𝑡𝐵= 𝑤Ω𝐵Ωo + 𝑤𝜆𝐵𝜆o

## Page 10

The BP Algorithm: Forward Pass
Input to A:
𝑖𝑛𝑝𝑢𝑡𝐴= 0.1
0.35 + 0.8
0.9 = 0.7550
Input to B:
𝑖𝑛𝑝𝑢𝑡𝐵= 0.4
0.35 + 0.6
0.9 = 0.6800

## Page 11

The BP Algorithm: Forward Pass
Output of A:
𝑜𝑢𝑡𝑝𝑢𝑡𝐴= F(𝑖𝑛𝑝𝑢𝑡𝐴)
Output of B:
𝑜𝑢𝑡𝑝𝑢𝑡𝐵= F(𝑖𝑛𝑝𝑢𝑡𝐵)

## Page 12

The BP Algorithm: Forward Pass
Output of A:
𝑜𝑢𝑡𝑝𝑢𝑡𝐴=
F 0.7550 = 0.6803
Output of B:
𝑜𝑢𝑡𝑝𝑢𝑡𝐵=
F 0.6800 = 0.6637

## Page 13

The BP Algorithm: Forward Pass
Input to θ:
𝑖𝑛𝑝𝑢𝑡𝜃= 𝑤𝐴𝜃𝐴o + 𝑤𝐵𝜃𝐵o
𝑖𝑛𝑝𝑢𝑡𝜃= 0.3
 0.6803 + 0.9
0.6637
𝑖𝑛𝑝𝑢𝑡𝜃= 0.8014

## Page 14

The BP Algorithm: Forward Pass
Output of θ :
𝑜𝑢𝑡𝑝𝑢𝑡𝜃= F(𝑖𝑛𝑝𝑢𝑡𝜃)
𝑜𝑢𝑡𝑝𝑢𝑡𝜃= F(0.8014)
𝑜𝑢𝑡𝑝𝑢𝑡𝜃= 0.6903

## Page 15
