---
chunk_id: "ml-05-04-ch-12-4f010d6d80-chunk-0005"
source_id: "ml-05-04-ch-12-4f010d6d80"
source_file: "_ML_05_04_Ch_12.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 5
confidence: "first-pass"
extraction_method: "structured-local"
---

•
In this section we particularly address the effect of the number of learning 
samples and the effect of the number of hidden units.
•
The average error per learning sample is defined as the learning error rate:
in which Ep is the difference between the desired output value and the actual
network output for the learning samples:
•
This is the error, which is measurable during the training process.
• We now define the test error rate as the average error of the test set:
• In the following subsections we will see how these error measures  
depend on learning set size and number of hidden units.

## Page 25

12.8.1 The Effect Of the Number of Learning Samples
•
A simple problem is used as example: a function y = f(x) has to be 
approximated with a feed-forward neural network. 
•
A neural network is created with an input layer, 5 hidden units with 
sigmoid activation function and a linear output unit. 
•
Suppose we have only a small number of learning samples (e.g., 4)  
and the networks is trained with these samples. 
•
Training is stopped when the error does not decrease anymore.

## Page 26

_No reliable embedded text extracted._

## Page 27

•
clc
•
close all
•
clear all
•
t = 0:0.1:5;
•
d=sin(.4*pi*t);
•
net = newff(t,d,10); % Here a network is created with one hidden layer of ten neurons. 
•
•
% The network is trained for 50 epochs. Again the network's output is plotted. 
•
net.trainParam.epochs = 50;
•
net = train(net,t,d);
•
Y = sim(net,t);
•
figure
•
plot(t,d,t,Y,'o')
•
xlabel('t')
•
ylabel('d')
•
t1 = 0:0.5:5;
•
d1=sin(.4*pi*t1);
•
net = newff(t1,d1,10); % Here a network is created with one hidden layer of ten neurons. 
•
% The network is trained for 50 epochs. Again the network's output is plotted. 
•
net.trainParam.epochs = 50;
•
net = train(net,t1,d1);
•
Y1 = sim(net,t1);
•
figure
•
plot(t,d,t1,Y1,'o')
•
xlabel('t1')
•
ylabel('d1')
•

## Page 28

_No reliable embedded text extracted._

## Page 29

•
This experiment was carried out with other learning set sizes, where for 
each learning set size the experiment was repeated 10 times. 
•
The average learning and test error rates as a function of the learning set 
size are given in Fig. 12.8. 
•
Note that 
– the learning error increases with an increasing learning set size,
– and the test error decreases with increasing learning set size.

## Page 30
