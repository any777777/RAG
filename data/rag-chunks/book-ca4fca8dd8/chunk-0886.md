---
chunk_id: "book-ca4fca8dd8-chunk-0886"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 886
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 15.6
The Value of Information
537
1. Set the evidence variables for the current state.
2. For each possible value of the decision node:
(a) Set the decision node to that value.
(b) Calculate the posterior probabilities for the parent nodes of the utility node, using
a standard probabilistic inference algorithm.
(c) Calculate the resulting utility for the action.
3. Return the action with the highest utility.
This is a straightforward approach that can utilize any available Bayesian network algorithm
and can be incorporated directly into the agent design given in Figure 12.1 on page 406. We
will see in Chapter 16 that the possibility of executing several actions in sequence makes the
problem much more interesting.
15.6 The Value of Information
In the preceding analysis, we have assumed that all relevant information, or at least all avail-
able information, is provided to the agent before it makes its decision. In practice, this is
hardly ever the case. One of the most important parts of decision making is knowing what ◀
questions to ask. For example, a doctor cannot expect to be provided with the results of all
possible diagnostic tests and questions at the time a patient ﬁrst enters the consulting room.
Tests are often expensive and sometimes hazardous (both directly and because of associated
delays). Their importance depends on two factors: whether the test results would lead to a
signiﬁcantly better treatment plan, and how likely the various test results are.
This section describes information value theory, which enables an agent to choose what
Information value
theory
information to acquire. We assume that prior to selecting a “real” action represented by the
decision node, the agent can acquire the value of any of the potentially observable chance
variables in the model. Thus, information value theory involves a simpliﬁed form of se-
quential decision making—simpliﬁed because the observation actions affect only the agent’s
belief state, not the external physical state. The value of any particular observation must
derive from the potential to affect the agent’s eventual physical action; and this potential can
be estimated directly from the decision model itself.
15.6.1 A simple example
Suppose an oil company is hoping to buy one of n indistinguishable blocks of ocean-drilling
rights. Let us assume further that exactly one of the blocks contains oil that will generate net
proﬁts of C dollars, while the others are worthless. The asking price of each block is C/n
dollars. If the company is risk-neutral, then it will be indifferent between buying a block and
not buying one because the expected proﬁt is zero in both cases.
Now suppose that a seismologist offers the company the results of a survey of block
number 3, which indicates deﬁnitively whether the block contains oil. How much should
the company be willing to pay for the information? The way to answer this question is to
examine what the company would do if it had the information:
• With probability 1/n, the survey will indicate oil in block 3. In this case, the company
will buy block 3 for C/n dollars and make a proﬁt of C −C/n = (n−1)C/n dollars.
