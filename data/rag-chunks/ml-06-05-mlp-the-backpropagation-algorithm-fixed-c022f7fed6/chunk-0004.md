---
chunk_id: "ml-06-05-mlp-the-backpropagation-algorithm-fixed-c022f7fed6-chunk-0004"
source_id: "ml-06-05-mlp-the-backpropagation-algorithm-fixed-c022f7fed6"
source_file: "_ML_06_05 - MLP - The Backpropagation Algorithm_Fixed.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

iteration     Output
   1                    0.6903
    2                    0.6820
    3                    0.6739
    4                    0.6661
    5                    0.6584
    6                    0.6510
    7                    0.6438
    8                    0.6368
    9                    0.6301
   10                    0.6237
   11                    0.6175
   12                    0.6115
   13                    0.6059
   14                    0.6004
   15                    0.5952
   16                    0.5903
   17                    0.5855
   18                    0.5810
   19                    0.5768
   20                    0.5727
   21                    0.5688
   22                    0.5651
   23                    0.5617
   24                    0.5583
   25                    0.5552
   26                    0.5522
   27                    0.5494
   28                    0.5467
   29                    0.5442
   30                    0.5418
   31                    0.5395
   32                    0.5374
   33                    0.5353
   34                    0.5334
   35                    0.5316
   36                    0.5299
   37                    0.5282
   38                    0.5267
   39                    0.5252
   40                    0.5239
   41                    0.5225
   42                    0.5213
   43                    0.5201
   44                    0.5190
   45                    0.5180
   46                    0.5170
   47                    0.5161
   48                    0.5152
   49                    0.5144
   50                    0.5136
   51                    0.5128
52
0 5121

## Page 38

clc, close all, clear all
WOA=0.1; WOB=0.4; WLA=0.8; WLB=0.6; WAT=0.3; WBT=0.9; O=0.35; L=0.9; TG=0.5
for i=1:100
IA=WOA*O+WLA*L
IB=WOB*O+WLB*L
OA=1/(1+exp(-IA))
OB=1/(1+exp(-IB))
IT=WAT*OA+WBT*OB
OT=1/(1+exp(-IT))
ET=(TG-OT)*(1-OT)*OT
WATN=WAT+OA*ET
WBTN=WBT+OB*ET
EA=WAT*ET*OA*(1-OA)
EB=WBT*ET*OB*(1-OB)
WOAN=WOA+O*EA
WOBN=WOB+O*EB
WLAN=WLA+L*EA
WLBN=WLB+L*EB
WAT=WATN; WBT=WBTN; WOA=WOAN; WOB=WOBN; WLA=WLAN; WLB=WLBN; 
oo(i,:)=[i OT]
End
plot(1:i,oo(:,2)), xlabel('Iteration'), ylabel('Output')
figure
plot(1:i,oo(:,2)-0.5), xlabel('Iteration'), ylabel('Abs error')

## Page 39
