---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0080"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 80
confidence: "first-pass"
extraction_method: "structured-local"
---

100
FUZZY LOGIC AND NEURAL NETWORKS
9.5
FUZZY LOGIC MODEL TO CONTROL ROOM TEMPERATURE
Although the behaviour of complex or nonlinear systems is difficult or impossible to describe using
numerical models, quantitative observations are often required to make quantitative control decisions.
These decisions could be the determination of a flow rate for a chemical process or a drug dosage in
medical practice. The form of the control model also determines the appropriate level of precision in the
result obtained. Numerical models provide high precision, but the complexity or non-linearity of a
process may make a numerical model unfeasible. In these cases, linguistic models provide an
alternative. Here the process is described in common language.
The linguistic model is built from a set of if-then rules, which describe the control model. Although
Zadeh was attempting to model human activities, Mamdani showed that fuzzy logic could be used to
develop operational automatic control systems.
9.5.1
The Mechanics of Fuzzy Logic
The mechanics of fuzzy mathematics involve the manipulation of fuzzy variables through a set of
linguistic equations, which can take the form of if–then rules. Much of the fuzzy literature uses set
theory notation, which obscures the ease of the formulation of a fuzzy controller. Although the
controllers are simple to construct, the proof of stability and other validations remain important topics.
The outline of fuzzy operations will be shown here through the design of a familiar room thermostat.
A fuzzy variable is one of the parameters of a fuzzy model, which can take one or more fuzzy
values, each represented by a fuzzy set and a word descriptor. The room temperature is the variable
shown in Fig. 9.7. Three fuzzy sets: ‘hot’, ‘cold’ and ‘comfortable’ have been defined by membership
distributions over a range of actual temperatures.
The power of a fuzzy model is the overlap between the fuzzy values. A single temperature value at
an instant in time can be a member of both of the overlapping sets. In conventional set theory, an object
(in this case a temperature value) is either a member of a set or it is not a member. This implies a crisp
80
60
40
20
0
50
100
150
100
50
0
Speed
Distance
Brake rate
Fig. 9.6
Relationship between inputs and brake rate.

## Page 120
