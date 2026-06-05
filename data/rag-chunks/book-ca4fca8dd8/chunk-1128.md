---
chunk_id: "book-ca4fca8dd8-chunk-1128"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1128
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.3
Learning Decision Trees
677
(a)
None
Some
Full
Patrons?
Yes
No
Hungry?
(b)
No
Yes
12
1
3
4
6
8
2
5
7
9
10 11
French
Italian
Thai
Burger
Type?
12
1
3
4
6
8
2
5
7
9
10 11
1
5
6
10
4
8
2
11
12
3
7
9
7
11
1
3
6
8
12
4
2
5
9
10
12
4
2
10
5
9
Figure 19.4 Splitting the examples by testing on attributes. At each node we show the
positive (light boxes) and negative (dark boxes) examples remaining. (a) Splitting on Type
brings us no nearer to distinguishing between positive and negative examples. (b) Splitting
on Patrons does a good job of separating positive and negative examples. After splitting on
Patrons, Hungry is a fairly good second test.
outcomes, each of which has the same number of positive as negative examples. On the other
hand, in (b) we see that Patrons is a fairly important attribute, because if the value is None or
Some, then we are left with example sets for which we can answer deﬁnitively (No and Yes,
respectively). If the value is Full, we are left with a mixed set of examples. There are four
cases to consider for these recursive subproblems:
1. If the remaining examples are all positive (or all negative), then we are done: we can
answer Yes or No. Figure 19.4(b) shows examples of this happening in the None and
Some branches.
2. If there are some positive and some negative examples, then choose the best attribute to
split them. Figure 19.4(b) shows Hungry being used to split the remaining examples.
3. If there are no examples left, it means that no example has been observed for this com-
bination of attribute values, and we return the most common output value from the set
of examples that were used in constructing the node’s parent.
4. If there are no attributes left, but both positive and negative examples, it means that
these examples have exactly the same description, but different classiﬁcations. This can
happen because there is an error or noise in the data; because the domain is nondeter-
Noise
ministic; or because we can’t observe an attribute that would distinguish the examples.
The best we can do is return the most common output value of the remaining examples.
The LEARN-DECISION-TREE algorithm is shown in Figure 19.5. Note that the set of exam-
ples is an input to the algorithm, but nowhere do the examples appear in the tree returned by
the algorithm. A tree consists of tests on attributes in the interior nodes, values of attributes
on the branches, and output values on the leaf nodes. The details of the IMPORTANCE func-
tion are given in Section 19.3.3. The output of the learning algorithm on our sample training
set is shown in Figure 19.6. The tree is clearly different from the original tree shown in Fig-
