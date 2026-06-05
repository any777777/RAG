---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0098"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 98
confidence: "first-pass"
extraction_method: "structured-local"
---

118
FUZZY LOGIC AND NEURAL NETWORKS
% If service is excellent or food is delicious, tip is generous
else,
tip=(((highTip–averTip)/ ...
(greatService–goodService))* ...
(service–goodService)+averTip)*servRatio + ...
(1–servRatio)*(tipRange/foodRange*food+lowTip);
end
Notice the tendency here, as with all code, for creeping generality to render the algorithm more and
more opaque, threatening eventually to obscure it completely. What we are doing here is not that
complicated. True, we can fight this tendency to be obscure by adding still more comments, or perhaps
by trying to rewrite it in slightly more self-evident ways, but the medium is not on our side.
The truly fascinating thing to notice is that if we remove everything except for three comments,
what remain are exactly the fuzzy rules we wrote down before:
% If service is poor or food is rancid, tip is cheap
% If service is good, tip is average
% If service is excellent or food is delicious, tip is generous
If, as with a fuzzy system, the comment is identical with the code, think how much more likely your
code is to have comments! Fuzzy logic lets the language that’s clearest to you, high level comments,
also have meaning to the machine, which is why it is a very successful technique for bridging the gap
between people and machines.
 QUESTION BANK.
1. Why use fuzzy logic?
2. What are the applications of fuzzy logic?
3. When not use fuzzy logic?
4. Compare non-fuzzy logic and fuzzy logic approaches.
 REFERENCES.
1. L.A. Zadeh, Fuzzy sets, Information and Control, Vol. 8, pp. 338-353, 1965.
2. USDA Agricultural Marketing Service, United States Standards for Grades of Apples,
Washington, D.C., 1976.
3. W.J.M. Kickert and H.R. Van Nauta Lemke, Application of a fuzzy controller in a warm water
plat, Automatica, Vol. 12, No. 4, pp. 301-308, 1976.
4. C.P. Pappis and E.H. Mamdani, A fuzzy logic controller for a traffic junction, IEEE Transactions
on Systems, Man and Cybernetics, Vol. 7, No. 10, pp. 707-717, 1977.

## Page 138
