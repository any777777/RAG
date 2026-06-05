---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0095"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 95
confidence: "first-pass"
extraction_method: "structured-local"
---

FUZZY LOGIC APPLICATIONS
115
If we extend this to two dimensions (Fig. 9.18), where we take food into account again, something
like this result:
servRatio = 0.8;
if service < 3,
tip = ((0.10/3) ¥ service + 0.05) ¥ servRatio + (1 – servRatio) ¥ (0.20/10 ¥ food + 0.05);
else if service < 7,
tip = (0.15) ¥ servRatio + (1 – servRatio) ¥ (0.20/10 ¥ food + 0.05);
else,
tip = ((0.10/3) ¥ (service – 7) + 0.15) ¥ servRatio + (1 – servRatio) ¥ (0.20/10 ¥ food + 0.05);
end
0.25
0.2
0.15
0.1
0.050
2
4
6
8
10
Service
Tip
Fig. 9. 17
Tipping using a piecewise linear construction.
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
Fig. 9.18
Tipping with two-dimensional variation.

## Page 135
