---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0092"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 92
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 128

FUZZY LOGIC APPLICATIONS
109
Q11 = (C1 Ÿ S1 Ÿ D1) = min {C1, S1, D1}
...(9.8)
On the other hand, the fuzzy OR (the maximum method) rule was used in evaluating the results of
the fuzzy rules given in Table 9.2; determination of the quality group that an apple would belong to, for
instance, was done by calculating the most likely membership degree using equations 9.9 through 9.13.
If,
k1 = (
,
,
)
,
,
,
Q
Q
Q
11
1 2
1 3
...(9.9)
k2 = (
,
,
,
,
)
,
,
,
,
,
,
Q
Q
Q
Q
Q
Q
2 1
2 2
2 3
2 4
2 5
2 6
...(9.10)
k3 = (
,
,
,
,
,
,
,
,
,
Q
Q
Q
Q
Q
3 1
3 2
3 3
3 4
3 5
Q
Q
Q
Q
Q
Q
Q
Q
Q
Q
Q
Q
3 6
3 7
3 8
3 9
3 10
3 11
3 12
3 13
3 14
3 15
3 16
3 17
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
)
...(9.11)
where k is the quality output group that contains different class membership degrees and the output
vector y given in equation 10 below determines the probabilities of belonging to a quality group for an
input sample before defuzzification:
y = [max (k1) max (k2) max (k3)]
...(9.12)
where, for example,
max (k1) = (Q1,1 ⁄ Q1,2 ⁄ Q1,3) = max {Q1,1, Q1,2, Q1,3}
...(9.13)
then, equation 11 produces the membership degree for the best class (Lee, 1990).
9.6.5
Determination of Membership Functions
Membership functions are in general developed by using intuition and qualitative assessment of the
relations between the input variable(s) and output classes. In the existence of more than one
membership function that is actually in the nature of the fuzzy logic approach, the challenge is to assign
input data into one or more of the overlapping membership functions. These functions can be defined
either by linguistic terms or numerical ranges, or both. The membership function used in this study for
defect quality in general is given in equation 9.4. The membership function for high amounts of defects,
for instance, was formed as given below:
If the input vector x is given as x = [defects, size, color], then the membership function for the class
of a high amount of defects (D3) is
m(D3) = 0, when x (1) < 1.75
m(D3) = ( ( ) – .
)
.
x 1
175
2 77
, when 1.75 £ x(1) £ 4.52 or
...(9.14)
m(D3) = 1, when x(1) ≥ 4.52
For a medium amount of defects (D2), the membership function is
m(D2) = 0, when defect innput x (1) < 0.24 or x (1) > 7.6
m(D2) = 
( ( ) – .
)
.
x 1
0 24
1 76
, when 0.24 £ x (1) £ 2
...(9.15)

## Page 129

_No reliable embedded text extracted._

## Page 130

_No reliable embedded text extracted._

## Page 131
