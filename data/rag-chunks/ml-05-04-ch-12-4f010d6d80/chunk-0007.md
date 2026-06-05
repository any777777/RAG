---
chunk_id: "ml-05-04-ch-12-4f010d6d80-chunk-0007"
source_id: "ml-05-04-ch-12-4f010d6d80"
source_file: "_ML_05_04_Ch_12.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 7
confidence: "first-pass"
extraction_method: "structured-local"
---

•
clc
•
close all
•
clear all
•
 
•
P = 0:0.1:5;
•
T=sin(.4*pi*P);
•
net = newff(P,T,10); % Here a network is created with one hidden layer of ten neurons. 
•
% The network is trained for 50 epochs. Again the network's output is plotted. 
•
net.trainParam.epochs = 50;
•
net = train(net,P,T);
•
Y = sim(net,P);
•
figure
•
plot(P,T,P,Y,'o')
•
 
•
 P1 = 0:0.1:5;
•
T1=sin(.4*pi*P1);
•
net = newff(P1,T1,50); % Here a network is created with one hidden layer of fifty neurons. 
•
 
•
% The network is trained for 50 epochs. Again the network's output is plotted. 
•
net.trainParam.epochs = 50;
•
net = train(net,P1,T1);
•
Y1 = sim(net,P1);
•
figure
•
plot(P,T,P1,Y1,'o')

## Page 36

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
t1 = 0:0.1:5;
•
d1=sin(.4*pi*t1);
•
net = newff(t1,d1,50); % Here a network is created with one hidden layer of fifty neurons. 
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

## Page 37

_No reliable embedded text extracted._

## Page 38

12.9 APPLICATIONS
•
Back-propagation has been applied to a wide variety of research 
applications.
– Sejnowski and Rosenberg (1986) produced a spectacular success with 
NETtalk, a system that converts printed English text into highly 
intelligible speech.
– A feed-forward network with one layer of hidden units has been described 
by Gorman and Sejnowski (1988) as a classification machine for sonar 
signals.
•
A multi-layer feed-forward network with a back-propagation training 
algorithm is used to learn an unknown function between input and 
output signals from the presentation of examples. 
– It is hoped that the network is able to generalize correctly, so that input 
values which are not presented as learning patterns will result in correct 
output values. 
– An example is the work of Josin (1988), who used a two-layer feed-
forward network with back-propagation learning to perform the inverse 
kinematic transform which is needed by a robot arm controller.
