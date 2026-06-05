---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0094"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 94
confidence: "first-pass"
extraction_method: "structured-local"
---

FUZZY LOGIC APPLICATIONS
113
This does not really take into account the quality of the service, so we need to add a new term to the
equation. Since service is rated on a scale of 0 to 10, we might have the tip go linearly from 5% if the
service is bad to 25% if the service is excellent (Fig. 9.14). Now our relation looks like this:
tip = 0.20/10 * service + 0.05
0.25
0.15
0.05
0.2
0.1
Tip
Service
0
2
4
6
8
10
Fig. 9. 14
Linear tipping.
The formula does what we want it to do, and it is pretty straight forward. However, we may want
the tip to reflect the quality of the food as well. This extension of the problem is defined as follows:
Given two sets of numbers between 0 and 10 (where 10 is excellent) that respectively represent the
quality of the service and the quality of the food at a restaurant, what should the tip be? Let’s see how the
formula will be affected now that we’ve added another variable (Fig. 9.15). Suppose we try:
tip = 0.20/20 ¥ (service + food) + 0.05
10
5
0
0
5
10
0.05
0.1
0.15
0.2
0.25
Food
Service
Tip
Fig. 9.15
Tipping depend on service and quality of food.

## Page 133

114
FUZZY LOGIC AND NEURAL NETWORKS
In this case, the results look pretty, but when you look at them closely, they do not seem quite right.
Suppose you want the service to be a more important factor than the food quality. Let’s say that the
service will account for 80% of the overall tipping “grade” and the food will make up the other 20%.
Try:
servRatio = 0.8;
tip= servRatio ¥ (0.20/10 ¥ service + 0.05) + (1– servRatio) ¥ (0.20/10 ¥ food + 0.05);
The response is still somehow too uniformly linear. Suppose you want more of a flat response in the
middle, i.e., you want to give a 15% tip in general, and will depart from this plateau only if the service
is exceptionally good or bad (Fig. 9.16).
10
5
0
0
5
10
0.05
0.1
0.15
0.2
0.25
Food
Service
Tip
Fig. 9.16
Tipping based on the service to be a more important factor than the food quality.
This, in turn, means that those nice linear mappings no longer apply. We can still salvage things by
using a piecewise linear construction (Fig. 9.17). Let’s return to the one-dimensional problem of just
considering the service. You can string together a simple conditional statement using breakpoints like
this:
if service < 3,
tip = (0.10/3) ¥ service + 0.05;
else if service < 7 ,
tip = 0.15;
else if service < =10,
tip = (0.10/3) ¥ (service –7) + 0.15;
end

## Page 134
