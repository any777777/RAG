---
chunk_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05-chunk-0096"
source_id: "fuzzy-logic-and-neural-networks-basic-concepts-application-8122421822-8da564fd05"
source_file: "Fuzzy Logic and Neural Networks_ Basic Concepts  Application_8122421822.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 96
confidence: "first-pass"
extraction_method: "structured-local"
---

116
FUZZY LOGIC AND NEURAL NETWORKS
The plot looks good, but the function is surprisingly complicated. It was a little tricky to code this
correctly, and it is definitely not easy to modify this code in the future. Moreover, it is even less apparent
how the algorithm works to someone who did not witness the original design process.
9.7.2
The Fuzzy Approach
It would be nice if we could just capture the essentials of this problem, leaving aside all the factors that
could be arbitrary. If we make a list of what really matters in this problem, we might end up with the
following rule descriptions:
1. If service is poor, then tip is cheap
2. If service is good, then tip is average
3. If service is excellent, then tip is generous
The order in which the rules are presented here is arbitrary. It does not matter which rules come
first. If we wanted to include the food’s effect on the tip, we might add the following two rules:
4. If food is rancid, then tip is cheap
5. If food is delicious, then tip is generous
In fact, we can combine the two different lists of rules into one tight list of three rules like so:
1. If service is poor or the food is rancid, then tip is cheap
2. If service is good, then tip is average
3. If service is excellent or food is delicious, then tip is generous
These three rules are the core of our solution. And coincidentally, we have just defined the rules for
a fuzzy logic system. Now if we give mathematical meaning to the linguistic variables (what is an
“average” tip, for example?) we would have a complete fuzzy inference system. Of course, there’s a lot
left to the methodology of fuzzy logic that we’re not mentioning right now, things like:
• How are the rules all combined?
• How do I define mathematically what an “average” tip is?
The details of the method do not really change much from problem to problem - the mechanics of
fuzzy logic are not terribly complex. What matters is what we have shown in this preliminary
exposition: fuzzy is adaptable, simple, and easily applied.
Fig. 9.19
Tipping using fuzzy logic.
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

## Page 136
