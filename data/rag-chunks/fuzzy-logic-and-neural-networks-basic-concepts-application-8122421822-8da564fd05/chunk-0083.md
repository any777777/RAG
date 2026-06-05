---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0083"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 83
confidence: "first-pass"
extraction_method: "structured-local"
---

FUZZY LOGIC APPLICATIONS
103
importantly, the process operators. The rules can include both the normal operation of the process as
well as the experience obtained through upsets and other abnormal conditions. Exception handling is a
particular strength of fuzzy control systems.
For very complex systems, the experts may not be able to identify their thought processes in
sufficient detail for rule creation. Rules may also be generated from operating data by searching for
clusters in the input data space. A simple temperature control model can be constructed from the
example of Fig. 9.7:
Rule 1 :
IF (Temperature is Cold) THEN (Heater is On)
Rule 2 :
IF (Temperature is Comfortable) THEN (Heater is Off)
Rule 3 :
IF (Temperature is Hot) THEN (Heater is Off)
In Rule 1, (Temperature is Cold) is the membership value of the actual temperature in the ‘cold’ set.
Rule 1 transfers the 0.66 membership in ‘cold’ to become 0.66 membership in the heater setting ‘on’.
Similar values from rules 2 and 3 are 0.33 and 0.00 in the ‘off’ setting for the heater. When several rules
give membership values for the same output set, Mamdani used the maximum of the membership
values. The result for the three rules is then 0.66 membership in ‘on’ and 0.33 membership in ‘off’.
The rules presented in the above example are simple yet effective. To extend these to more complex
control models, compound rules may be formulated. For example, if humidity was to be included in the
room temperature control example, rules of the form: IF (Temperature is Cold) AND (Humidity is High)
THEN (Heater is ON) might be used. Zadeh defined the logical operators as AND = Min (mA, mB) and
OR = Max (mA, mB), where mA and mB are membership values in sets A and B respectively. In the above
rule, the membership in ‘on’ will be the minimum of the two antecedent membership values. Zadeh also
defined the NOT operator by assuming that complete membership in the set A is given by mA = 1. The
membership in NOT (A) is then given by mNOT (A) = 1 – mA. This gives the interesting result that A
AND NOT (A) does not vanish, but gives a distribution corresponding to the overlap between A and its
adjacent sets.
9.5.4
Defuzzification
The results of rule application are membership values in each of the consequent or output sets. These
can be used directly where the membership values are viewed as the strength of the recommendations
provided by the rules. It is possible that several outputs are recommended and some may be
contradictory (e.g. heater on and heater off). In automatic control, one physical value of a controller
output must be chosen from multiple recommendations. In decision support systems, there must be a
consistent method to resolve conflict and define an appropriate compromise. Defuzzification is the
process for converting fuzzy output values to a single value or final decision. Two methods are
commonly used.
The first is the maximum membership method. All of the output membership functions are
combined using the OR operator and the position of the highest membership value in the range of the
output variable is used as the controller output. This method fails when there are two or more equal
maximum membership values for different recommendations. Here the method becomes indecisive and
does not produce a satisfactory result.
