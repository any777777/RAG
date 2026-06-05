---
chunk_id: "ml-06-05-mlp-the-backpropagation-algorithm-fixed-c022f7fed6-chunk-0003"
source_id: "ml-06-05-mlp-the-backpropagation-algorithm-fixed-c022f7fed6"
source_file: "_ML_06_05 - MLP - The Backpropagation Algorithm_Fixed.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

The BP Algorithm: Backward Pass 
(Input-to-Hidden Layer)
• The new weight for input unit λ in the input-
to-hidden layer is:
𝑤λ𝐵+ = 𝑤λ𝐵+ (λo × δ𝐵)
𝑤λ𝐵+ = 0.6 + ((0.9) × (−0.0082))
𝑤λ𝐵+ = 0.5926

## Page 27

Lets test the new network weights
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

## Page 28

Lets test the new network weights
A
B
θ
Ω
λ
0.0991
0.3971
0.7976
0.5926
0.2723
0.8730
𝑜𝑢𝑡𝑝𝑢𝑡
(𝑑𝑒𝑠𝑖𝑟𝑒𝑑𝑜𝑢𝑡𝑝𝑢𝑡= 0.5)
0.35
0.90

## Page 29

Lets test the new network weights
Input to A:
𝑖𝑛𝑝𝑢𝑡𝐴= 𝑤Ω𝐴Ωo + 𝑤𝜆𝐴𝜆o
Input to B:
𝑖𝑛𝑝𝑢𝑡𝐵= 𝑤Ω𝐵Ωo + 𝑤𝜆𝐵𝜆o

## Page 30

Lets test the new network weights
Input to A:
𝑖𝑛𝑝𝑢𝑡𝐴= 0.0991
0.35 + 0.7976
0.9 = 0.7525
Input to B:
𝑖𝑛𝑝𝑢𝑡𝐵= 0.3971
0.35 + 0.5926
0.9 = 0.6724

## Page 31

Lets test the new network weights
Output of A:
𝑜𝑢𝑡𝑝𝑢𝑡𝐴= F(𝑖𝑛𝑝𝑢𝑡𝐴)
Output of B:
𝑜𝑢𝑡𝑝𝑢𝑡𝐵= F(𝑖𝑛𝑝𝑢𝑡𝐵)

## Page 32

Lets test the new network weights
Output of A:
𝑜𝑢𝑡𝑝𝑢𝑡𝐴=
F 0.7525 = 0.6797
Output of B:
𝑜𝑢𝑡𝑝𝑢𝑡𝐵=
F 0.6724 = 0.6620

## Page 33

Lets test the new network weights
Input to θ:
𝑖𝑛𝑝𝑢𝑡𝜃= 𝑤𝐴𝜃𝐴o + 𝑤𝐵𝜃𝐵o
𝑖𝑛𝑝𝑢𝑡𝜃= 0.2723
0.6797 + 0.8730
0.6620
𝑖𝑛𝑝𝑢𝑡𝜃= 0.7631

## Page 34

Lets test the new network weights
Output of θ :
𝑜𝑢𝑡𝑝𝑢𝑡𝜃= F(𝑖𝑛𝑝𝑢𝑡𝜃)
𝑜𝑢𝑡𝑝𝑢𝑡𝜃= F(0.7631)
𝑜𝑢𝑡𝑝𝑢𝑡𝜃= 0.6820

## Page 35

Lets test the new network weights
• For sigmoid activation functions, the output 
error is calculated as:
δ𝜃= (𝑡𝑎𝑟𝑔𝑒𝑡𝜃−𝑜𝑢𝑡𝑝𝑢𝑡𝜃)(1 −𝑜𝑢𝑡𝑝𝑢𝑡𝜃)𝑜𝑢𝑡𝑝𝑢𝑡𝜃
• From our example, the output error is 
calculated:
δ𝜃=
0.5 −0.6820 
1 −0.6820  0.6820
δ𝜃= −0.0395

## Page 36

Lets test the new network weights
• From our first pass, the output error is:
δ𝜃= −0.0407 
• And in the second pass, the output error is:
δ𝜃= −0.0395
     as a result of the weight change.
• The backpropagation algorithm is continued
until a sufficiently small error value has been
obtained.

## Page 37
