---
chunk_id: "ml-06-05-mlp-the-backpropagation-algorithm-fixed-c022f7fed6-chunk-0002"
source_id: "ml-06-05-mlp-the-backpropagation-algorithm-fixed-c022f7fed6"
source_file: "_ML_06_05 - MLP - The Backpropagation Algorithm_Fixed.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

The BP Algorithm: Backward Pass
• The backward pass is the second step in the 
BP algorithm.
• It calculates the error between the desired 
output and the output of the network.
• The difference between the two will be used 
to make small adjustments to the network 
weights on a layer-by-layer basis.

## Page 16

The BP Algorithm: Backward Pass
• For sigmoid activation functions, the output 
error is calculated as:
δ𝜃= (𝑡𝑎𝑟𝑔𝑒𝑡𝜃−𝑜𝑢𝑡𝑝𝑢𝑡𝜃)(1 −𝑜𝑢𝑡𝑝𝑢𝑡𝜃)𝑜𝑢𝑡𝑝𝑢𝑡𝜃
• From our example, the output error is 
calculated:
δ𝜃=
0.5 −0.6903 1 −0.6903  0.6903
δ𝜃= -0.0407

## Page 17

The BP Algorithm: Backward Pass
• The calculated error value is the used to adjust 
the weights in the network.
• The weights are adjusted on a layer-to-layer 
basis, beginning with the weights in the 
hidden-to-output layer, followed by the 
weights in the input-to-hidden layer.

## Page 18

The BP Algorithm: Backward Pass
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

## Page 19

The BP Algorithm: Backward Pass 
(Hidden-to-Output Layer)
• The new weight for hidden unit A in the 
hidden-to-output layer is:
𝑤𝐴𝜃+ = 𝑤𝐴𝜃+ (𝐴o × δ𝜃)
𝑤𝐴𝜃+ = 0.3 + ((0.6803) × (-0.0407))
𝑤𝐴𝜃+ = 0.2723

## Page 20

The BP Algorithm: Backward Pass 
(Hidden-to-Output Layer)
• The new weight for hidden unit B in the 
hidden-to-output layer is:
𝑤𝐵𝜃+ = 𝑤𝐵𝜃+ (𝐵o × δ𝜃)
𝑤𝐵𝜃+ = 0.9 + ((0.6637) × (-0.0407))
𝑤𝐵𝜃+ = 0.8730

## Page 21

The BP Algorithm: Backward Pass 
(Input-to-Hidden Layer)
• The errors for unit A and B can be derived from
the output error and the new weights:
δ𝐴
= 𝑤𝐴𝜃× δ𝜃*(Ao*(1-Ao))
δ𝐴
= 0.3 × − 0.0407* 0.6803*(1-0.6803)
δ𝐴
= -0.0027

## Page 22

The BP Algorithm: Backward Pass 
(Input-to-Hidden Layer)
• The errors for unit A and B can be derived from
the output error and the new weights:
δ𝐵
= 𝑤𝐵𝜃× δ𝜃 *(Bo*(1-Bo))
δ𝐵
= 0.9 × −0.0407* 0.6637*(1- 0.6637)
δ𝐵
= - 0.0082

## Page 23

The BP Algorithm: Backward Pass 
(Input-to-Hidden Layer)
• The new weight for input unit Ω in the input-
to-hidden layer is:
𝑤Ω𝐴+ = 𝑤Ω𝐴+ (Ωo × δ𝐴)
𝑤Ω𝐴+ = 0.1 + ((0.35) × (− 0.0027))
𝑤Ω𝐴+ = 0.0991

## Page 24

The BP Algorithm: Backward Pass 
(Input-to-Hidden Layer)
• The new weight for input unit Ω in the input-
to-hidden layer is:
𝑤Ω𝐵+ = 𝑤Ω𝐵+ (Ωo × δ𝐵)
𝑤Ω𝐵+ = 0.4 + ((0.35) × (−0.0082))
𝑤Ω𝐵+ = 0.3971

## Page 25

The BP Algorithm: Backward Pass 
(Input-to-Hidden Layer)
• The new weight for input unit λ in the input-
to-hidden layer is:
𝑤λ𝐴+ = 𝑤λ𝐴+ (λo × δ𝐴)
𝑤λ𝐴+ = 0.8 + ((0.9) × (−0.0027))
𝑤λ𝐴+ = 0.7976

## Page 26
