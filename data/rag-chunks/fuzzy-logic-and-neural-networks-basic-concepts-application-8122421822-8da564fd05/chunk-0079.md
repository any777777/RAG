---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0079"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 79
confidence: "first-pass"
extraction_method: "structured-local"
---

98
FUZZY LOGIC AND NEURAL NETWORKS
9.4.4
Membership Functions
In the established model, different membership functions were formed for speed, distance and brake
rate. Membership functions are given in Figures 9.3, 9.4, and 9.5. For maximum allowable car speed (in
motorways) in India, speed scale selected as 0-120 km/h on its membership function. Because of the
fact that current distance sensors perceive approximately 100-150 m distance, distance membership
function is used 0-150 m scale. Brake rate membership function is used 0-100 scale for expressing
percent type.
Fig. 9.2
General structure of fuzzy logic model.
Low
Medium
High
1
0.5
0
0
20
40
60
80
100
120
Fig. 9.3
Membership function of speed.
Low
Medium
High
1
0.5
0
0
50
100
150
Fig. 9.4
Membership function of distance.
Brake rate
Speed
Distance
Rule base

## Page 118

FUZZY LOGIC APPLICATIONS
99
9.4.5
Rule Base
We need a rule base to run the fuzzy model. Fuzzy Allocation Map (rules) of the model was constituted
for membership functions whose figures are given on Table-9.1. It is important that the rules were not
completely written for all probability. Figure 6 shows that the relationship between inputs, speed and
distance, and brake rate.
Table 9.1:
Fuzzy allocation map of the model
Speed
Distance
Brake rate
LOW
LOW
LOW
LOW
MEDIUM
LOW
LOW
HIGH
MEDIUM
MEDIUM
LOW
MEDIUM
MEDIUM
MEDIUM
LOW
MEDIUM
HIGH
LOW
HIGH
LOW
HIGH
HIGH
MEDIUM
MEDIUM
HIGH
HIGH
LOW
9.4.6
Output
Fuzzy logic is also an estimation algorithm. For this model, various alternatives are able to cross-
examine using the developed model. Fig. 9.6 is an example for such the case.
9.4.7
Conclusions
Many people die or injure because of traffic accidents in India. Many reasons can contribute these
results for example mainly driver fault, lack of infrastructure, environment, weather conditions etc. In
this study, a model was established for estimation of brake rate using fuzzy logic approach. Car brake
rate is estimated using the developed model from speed and distance data. So, it can be said that this
fuzzy logic approach can be effectively used for reduce to traffic accident rate. This model can be
adapted to vehicles.
Low
Medium
High
1
0.5
0
0
10
20
30
40
50
60
70
80
90 100
Fig. 9.5
Membership function of brake rate.

## Page 119
