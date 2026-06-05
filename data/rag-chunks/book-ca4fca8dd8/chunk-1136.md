---
chunk_id: "book-ca4fca8dd8-chunk-1136"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1136
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.4
Model Selection and Optimization
683
classiﬁcations, while keeping track of the running totals of positive and negative exam-
ples on each side of the split point. Splitting is the most expensive part of real-world
decision tree learning applications.
For attributes that are not continuous and do not have a meaningful ordering, but
have a large number of possible values (e.g., Zipcode or CreditCardNumber), a measure
called the information gain ratio (see Exercise 19.GAIN) can be used to avoid splitting
into lots of single-example subtrees. Another useful approach is to allow an equality
test of the form A=vk. For example, the test Zipcode=10002 could be used to pick out
a large group of people in this zip code in New York City, and to lump everyone else
into the “other” subtree.
• Continuous-valued output attribute: If we are trying to predict a numerical output
value, such as the price of an apartment, then we need a regression tree rather than a
Regression tree
classiﬁcation tree. A regression tree has at each leaf a linear function of some subset of
numerical attributes, rather than a single output value. For example, the branch for two-
bedroom apartments might end with a linear function of square footage and number
of bathrooms. The learning algorithm must decide when to stop splitting and begin
applying linear regression (see Section 19.6) over the attributes. The name CART,
CART
standing for Classiﬁcation And Regression Trees, is used to cover both classes.
A decision tree learning system for real-world applications must be able to handle all of
these problems. Handling continuous-valued variables is especially important, because both
physical and ﬁnancial processes provide numerical data. Several commercial packages have
been built that meet these criteria, and they have been used to develop thousands of ﬁelded
systems. In many areas of industry and commerce, decision trees are the ﬁrst method tried
when a classiﬁcation method is to be extracted from a data set.
Decision trees have a lot going for them: ease of understanding, scalability to large data
sets, and versatility in handling discrete and continuous inputs as well as classiﬁcation and
regression. However, they can have suboptimal accuracy (largely due to the greedy search),
and if trees are very deep, then getting a prediction for a new example can be expensive in run
time. Decision trees are also unstable in that adding just one new example can change the
Unstable
test at the root, which changes the entire tree. In Section 19.8.2 we will see that the random
forest model can ﬁx some of these issues.
19.4 Model Selection and Optimization
Our goal in machine learning is to select a hypothesis that will optimally ﬁt future examples.
To make that precise we need to deﬁne “future example” and “optimal ﬁt.”
First we will make the assumption that the future examples will be like the past. We call
this the stationarity assumption; without it, all bets are off. We assume that each example E j
Stationarity
has the same prior probability distribution:
P(E j) = P(E j+1) = P(E j+2) = ··· ,
and is independent of the previous examples:
P(E j) = P(E j|E j−1,E j−2,...).
Examples that satisfy these equations are independent and identically distributed or i.i.d..
I.i.d.
