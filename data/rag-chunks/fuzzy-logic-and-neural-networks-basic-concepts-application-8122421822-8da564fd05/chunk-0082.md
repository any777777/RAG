---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0082"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 82
confidence: "first-pass"
extraction_method: "structured-local"
---

102
FUZZY LOGIC AND NEURAL NETWORKS
A series of measurements are collected in the form of a histogram and use this as the fuzzy input as
shown in Fig. 9.8. The fuzzy inference is extended to include the uncertainty due to measurement error
as well as the vagueness in the linguistic descriptions. In Fig. 9.8 the measurement data histogram is
normalized so that its peak is a membership value of 1.0 and it can be used as a fuzzy set. The
membership of the histogram in ‘cold’ is given by: max {min [mcold(T), mhistogram(T)]} where the
maximum and minimum operations are taken using the membership values at each point T over the
temperature range of the two distributions.
The minimum operation yields the overlap region of the two sets and the maximum operation gives
the highest membership in the overlap. The membership of the histogram in ‘cold’, indicated by the
arrow in Fig. 9.8, is 0.73. By similar operations, the membership of the histogram in ‘comfortable’ and
‘hot’ are 0.40 and 0.00. It is interesting to note that there is no requirement that the sum of all
memberships be 1.00.
9.5.3
Rule Application
The linguistic model of a process is commonly made of a series of if - then rules. These use the
measured state of the process, the rule antecedents, to estimate the extent of control action, the rule
consequents. Although each rule is simple, there must be a rule to cover every possible combination of
fuzzy input values. Thus, the simplicity of the rules trades off against the number of rules. For complex
systems the number of rules required may be very large.
The rules needed to describe a process are often obtained through consultation with workers who
have expert knowledge of the process operation. These experts include the process designers, but more
Fig. 9.8
Fuzzification with measurement noise.
1.2
1.0
0.8
Hot
Comfortable
Cold
0.6
0.4
0.2
0.0
0
5
10
15
20
25
30
35
40
45
50
Temperature (Degrees C)
Membership value

## Page 122
