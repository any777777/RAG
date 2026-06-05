---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0093"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 93
confidence: "first-pass"
extraction_method: "structured-local"
---

112
FUZZY LOGIC AND NEURAL NETWORKS
9.6.8
Conclusion
Fuzzy logic was successfully applied to serve as a decision support technique in grading apples. Grading
results obtained from fuzzy logic showed a good general agreement with the results from the human
expert, providing good flexibility in reflecting the expert’s expectations and grading standards into the
results. It was also seen that color, defects and size are three important criteria in apple classification.
However, variables such as firmness, internal defects and some other sensory evaluations, in addition to
the features mentioned earlier, could increase the efficiency of decisions made regarding apple quality.
9.7
AN INTRODUCTORY EXAMPLE: FUZZY V/S NON-FUZZY
To illustrate the value of fuzzy logic, fuzzy and non-fuzzy approaches are applied to the same problem.
First the problem is solved using the conventional (non-fuzzy) method, writing MATLAB commands
that spell out linear and piecewise-linear relations. Then, the same system is solved using fuzzy logic.
Consider the tipping problem: what is the “right” amount to tip your waitperson? Given a number
between 0 and 10 that represents the quality of service at a restaurant (where 10 is excellent), what
should the tip be?
This problem is based on tipping as it is typically practiced in the United States. An average tip for
a meal in the U.S. is 15%, though the actual amount may vary depending on the quality of the service
provided.
9.7.1
The Non-Fuzzy Approach
Let’s start with the simplest possible relationship (Fig. 9.13). Suppose that the tip always equals 15% of
the total bill.
tip = 0.15
0.25
0.15
0.05
0.2
0.1
Tip
Service
00
2
4
6
8
10
Fig. 9.13
Constant tipping.

## Page 132
