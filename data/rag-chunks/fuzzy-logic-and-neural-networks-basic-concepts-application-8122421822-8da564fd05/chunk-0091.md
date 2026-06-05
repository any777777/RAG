---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0091"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 91
confidence: "first-pass"
extraction_method: "structured-local"
---

108
FUZZY LOGIC AND NEURAL NETWORKS
9.6.4
Fuzzy Rules
At this stage, human linguistic expressions were involved in fuzzy rules. The rules used in the
evaluations of apple quality are given in Table 9.2. Two of the rules used to evaluate the quality of
Golden Delicious apples are given below:
If the color is greenish, there is no defect, and it is a well formed large apple, then quality is very
good (rule Q1,1 in Table 9.2).
Table 9.2:
Fuzzy rule tabulation
C1 + S1
C1 + S2
C1 + S3
C2 + S1
C2 + S2
C2 + S3
C3 + S1
C2 + S2
C3 + S3
D1
Q1,1
Q1,2
Q2,3
Q1,3
Q2,5
Q3,8
Q2,6
Q2,7
Q3,15
D2
Q2,1
Q2,2
Q3,3
Q2,4
Q3,6
Q3,9
Q3,11
Q3,13
Q3,16
D3
Q3,1
Q3,2
Q3,4
Q3,5
Q3,7
Q3,10
Q3,12
Q3,14
Q3,17
Where, C1 is the greenish color quality (desired), C2 is greenish-yellow color quality medium), and C3 is yellow color
quality (bad); S1, on the other hand, is well formed size (desired), S2 is moderately formed size (medium), S3 is badly
formed size (bad). Finally, D1 represents a low amount of defects (desired), while D2 and D3 represent moderate
(medium) and high (bad) amounts of defects, respectively. For quality groups represented with “Q” in Table 1, the first
subscript 1 stands for the best quality group, while 2 and 3 stand for the moderate and bad quality groups, respectively.
The second subscript of Q shows the number of rules for the particular quality group, which ranges from 1 to 17 for the
bad quality group.
If the color is pure yellow (overripe), there are a lot of defects, and it is a badly formed (small)
apple, then quality is very bad (rule Q3,17 in Table 9.2).
A fuzzy set is defined by the expression below:
D = {X. m0(x))| x Œ X}
...(9.4)
m0(x): Æ [0, 1]
where X represents the universal set, D is a fuzzy subset in X and μD(x) is the membership function of
fuzzy set D. Degree of membership for any set ranges from 0 to1. A value of 1.0 represents a 100%
membership while a value of 0 means 0% membership. If there are three subgroups of size, then three
memberships are required to express the size values in a fuzzy rule.
Three primary set operations in fuzzy logic are AND, OR, and the Complement, which are given as
follows
AND:
mC Ÿ mD = min {mC, mD}
...(9.5)
OR:
mC » mD = (mC ⁄ mD) = max {mC, mD}
...(9.6)
complement = 
C
 = 1 – mD
...(9.7)
The minimum method given by equation (9.5) was used to combine the membership degrees from
each rule established. The minimum method chooses the most certain output among all the membership
degrees. An example of the fuzzy AND (the minimum method) used in if-then rules to form the Q11
quality group in Table 9.2 is given as follows;
