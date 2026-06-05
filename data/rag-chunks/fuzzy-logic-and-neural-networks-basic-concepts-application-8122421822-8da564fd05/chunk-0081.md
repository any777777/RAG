---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0081"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 81
confidence: "first-pass"
extraction_method: "structured-local"
---

FUZZY LOGIC APPLICATIONS
101
boundary between the sets. In fuzzy logic, the boundaries between sets are blurred. In the overlap
region, an object can be a partial member of each of the overlapping sets. The blurred set boundaries
give fuzzy logic its name. By admitting multiple possibilities in the model, the linguistic imprecision is
taken into account.
The membership functions defining the three fuzzy sets shown in Fig. 9.7 are triangular. There are
no constraints on the specification of the form of the membership distribution. The Gaussian form from
statistics has been used, but the triangular form is commonly chosen, as its computation is simple. The
number of values and the range of actual values covered by each one are also arbitrary. Finer resolution
is possible with additional sets, but the computation cost increases.
Guidance for these choices is provided by Zadeh’s Principle of Incompatibility: As the complexity
of a system increases, our ability to make precise and yet significant statements about its behaviour
diminishes until a threshold is reached beyond which precision and significance (or relevance) become
almost mutually exclusive characteristics.
The operation of a fuzzy controller proceeds in three steps. The first is fuzzification, where
measurements are converted into memberships in the fuzzy sets. The second step is the application of
the linguistic model, usually in the form of if-then rules. Finally the resulting fuzzy output is converted
back into physical values through a defuzzfication process.
9.5.2
Fuzzification
For a single measured value, the fuzzification process is simple, as shown in Fig. 9.7. The membership
functions are used to calculate the memberships in all of the fuzzy sets. Thus, a temperature of 15°C
becomes three fuzzy values, 0.66 ‘cold’, 0.33 ‘comfortable’ and 0.00 ‘hot’.
Fig. 9.7
Room temperature.
1.2
Hot
Comfortable
Cold
0.67
0.33
1.0
0.8
0.6
0.4
0.2
0.00
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

## Page 121
