---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0089"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 89
confidence: "first-pass"
extraction_method: "structured-local"
---

106
FUZZY LOGIC AND NEURAL NETWORKS
The number of apples used was determined based on the availability of apples with quality features
of the 3 quality groups (bad, medium and good). A total of 181 golden delicious apples were graded first
by a human expert and then by the proposed fuzzy logic approach. The expert was trained on the
external quality criteria for good, medium and bad apple groups defined by USDA standards (USDA,
1976). The USDA standards for apple quality explicitly define the quality criteria so that it is quite
straightforward for an expert to follow up and apply them. Extremely large or small apples were already
excluded by the handling personnel. Eighty of the apples were kept at room temperature for 4 days
while another 80 were kept in a cooler (at about 3°C) for the same period to create color variation on the
surfaces of apples. In addition, 21 of the apples were harvested before the others and kept for 15 days at
room temperature for the same purpose of creating a variation in the appearance of the apples to be
tested.
The Hue angle (tan-1(b/a)), which was used to represent the color of apples, was shown to be the
best representation of human recognition of color. To simplify the problem, defects were collected
under a single numerical value, “defect” after normalizing each defect component such as bruises,
natural defects, russetting and size defects (lopsidedness).
Defect = 10 ¥ B + 5 ¥ ND + 3 ¥ R + 0.3 ¥ SD
...(9.1)
where B is the amount of bruising, ND is the amount of natural defects, such as scars and leaf roller, as
total area (normalized), R is the total area of russeting defect (normalized) and SD is the normalized size
defect. Similarly, circumference, blush (reddish spots on the cheek of an apple) percentage and weight
were combined under “Size” using the same procedure as with “Defect”
Size = 5 ¥ C + 3 ¥ W + 5 ¥ BL
...(9.2)
where C is the circumference of the apple (normalized), W is weight (normalized) and BL is the
normalized blush percentage. Coefficients used in the above equations were subjectively selected,
based on the expert’s expectations and USDA standards (USDA, 1976).
Although it was measured at the beginning, firmness was excluded from the evaluation, as it was
difficult for the human expert to quantify it nondestructively. After the combinations of features given
in the above equations, input variables were reduced to 3 defect, size and color. Along with the
measurements of features, the apples were graded by the human expert into three quality groups, bad,
medium and good, depending on the expert’s experience, expectations and USDA standards (USDA,
1976). Fuzzy logic techniques were applied to classify apples after measuring the quality features. The
grading performance of fuzzy logic proposed was determined by comparing the classification results
from FL and the expert.
9.6.3
Application of Fuzzy Logic
Three main operations were applied in the fuzzy logic decision making process: selection of fuzzy
inputs and outputs, formation of fuzzy rules, and fuzzy inference. A trial and error approach was used to
develop membership functions. Although triangular and trapezoidal functions were used in establishing
membership functions for defects and color (Fig. 9.9 and 9.10), an exponential function with the base
of the irrational number e was used to simulate the inclination of the human expert in grading apples in
terms of size (Fig. 9.11).
