---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0078"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 78
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 116

FUZZY LOGIC APPLICATIONS
97
9.4.2
Fuzzy Logic Approach
The basic elements of each fuzzy logic system are, as shown in Figure 9.1, rules, fuzzifier, inference
engine, and defuzzifier. Input data are most often crisp values. The task of the fuzzifier is to map crisp
numbers into fuzzy sets (cases are also encountered where inputs are fuzzy variables described by fuzzy
membership functions). Models based on fuzzy logic consist of “If-Then” rules. A typical “If-Then”
rule would be:
If
the ratio between the flow intensity and capacity of an arterial road is SMALL
Then
vehicle speed in the flow is BIG
The fact following “If” is called a premise or hypothesis or antecedent. Based on this fact we can
infer another fact that is called a conclusion or consequent (the fact following “Then”). A set of a large
number of rules of the type:
If
premise
Then
conclusion is called a fuzzy rule base.
Fig. 9.1
Basic elements of a fuzzy logic.
In fuzzy rule-based systems, the rule base is formed with the assistance of human experts; recently,
numerical data has been used as well as through a combination of numerical data-human experts. An
interesting case appears when a combination of numerical information obtained from measurements
and linguistic information obtained from human experts is used to form the fuzzy rule base. In this case,
rules are extracted from numerical data in the first step. In the next step this fuzzy rule base can (but
need not) be supplemented with the rules collected from human experts. The inference engine of the
fuzzy logic maps fuzzy sets onto fuzzy sets. A large number of different inferential procedures are found
in the literature. In most papers and practical engineering applications, minimum inference or product
inference is used. During defuzzification, one value is chosen for the output variable. The literature also
contains a large number of different defuzzification procedures. The final value chosen is most often
either the value corresponding to the highest grade of membership or the coordinate of the center of
gravity.
9.4.3
Application
In the study, a model was established which estimates brake rate using fuzzy logic. The general
structure of the model is shown in Fig. 9.2.
Fuzzifier
Defuzzifier
Rules
Inference
Input
Crips output

## Page 117
