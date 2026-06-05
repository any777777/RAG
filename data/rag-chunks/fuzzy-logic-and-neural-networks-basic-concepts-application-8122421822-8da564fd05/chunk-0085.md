---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0085"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 85
confidence: "first-pass"
extraction_method: "structured-local"
---

104
FUZZY LOGIC AND NEURAL NETWORKS
The second method uses the center of gravity of the combined output distribution to resolve this
potential conflict and to consider all recommendations based on the strengths of their membership
values. The center of gravity is given by XF = 
x
x dx
x dx
( )
( )
zz
 where x is a point in the output range and XF
is the final control value. These integrals are taken over the entire range of the output. By taking the
center of gravity, conflicting rules essentially cancel and a fair weighting is obtained.
The output values used in the thermostat example are singletons. Singletons are fuzzy values with a
membership of 1.00 at a single value rather than a membership function between 0 and 1 defined over
an interval of values. In the example there were two, ‘off’ at 0% power and ‘on’ at 100% power. With
singletons, the center of gravity equation integrals become a simple weighted average. Applying the
rules gave mON = 0.67 and mOFF = 0.33. Defuzzifying these gives a control output of 67% power.
Although only two singleton output functions were used, with center of gravity defuzzification, the
heater power decreases smoothly between fully on and fully off as the temperature increases between
10°C and 25°C.
In the histogram input case, applying the same rules gave mON = 0.73 and mOFF = 0.40. Center of
gravity defuzzification gave, in this case, a heater power of 65%. The sum of the membership functions
was normalized by the denominator of the center of gravity calculation.
9.5.5
Conclusions
Linguistic descriptions in the form of membership functions and rules make up the model. The rules are
generated a priori from expert knowledge or from data through system identification methods. Input
membership functions are based on estimates of the vagueness of the descriptors used. Output
membership functions can be initially set, but can be revised for controller tuning.
Once these are defined, the operating procedures for the calculations are well set out. Measurement
data are converted to memberships through fuzzification procedures. The rules are applied using
formalized operations to yield memberships in output sets. Finally, these are combined through
defuzzification to give a final control output.
9.6
FUZZY LOGIC MODEL FOR GRADING OF APPLES
Agricultural produce is subject to quality inspection for optimum evaluation in the consumption cycle.
Efforts to develop automated fruit classification systems have been increasing recently due to the
drawbacks of manual grading such as subjectivity, tediousness, labor requirements, availability, cost
and inconsistency.
However, applying automation in agriculture is not as simple as automating the industrial
operations. There are two main differences. First, the agricultural environment is highly variable, in
terms of weather, soil, etc. Second, biological materials, such as plants and commodities, display high
variation due to their inherent morphological diversity. Techniques used in industrial applications, such
as template matching and fixed object modeling are unlikely to produce satisfactory results in the
classification or control of input from agricultural products. Therefore, self-learning techniques such as
neural networks (NN) and fuzzy logic (FL) seem to represent a good approach.
