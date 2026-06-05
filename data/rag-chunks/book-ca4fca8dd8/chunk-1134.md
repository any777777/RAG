---
chunk_id: "book-ca4fca8dd8-chunk-1134"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1134
confidence: "first-pass"
extraction_method: "structured-local"
---

682
Chapter 19
Learning from Examples
distribution with d −1 degrees of freedom. We can use a χ2 statistics function to see if a
particular ∆value conﬁrms or rejects the null hypothesis. For example, consider the restaurant
Type attribute, with four values and thus three degrees of freedom. A value of ∆=7.82 or
more would reject the null hypothesis at the 5% level (and a value of ∆=11.35 or more
would reject at the 1% level). Values below that lead to accepting the hypothesis that the
attribute is irrelevant, and thus the associated branch of the tree should be pruned away. This
is known as χ2 pruning.
χ2 pruning
With pruning, noise in the examples can be tolerated. Errors in the example’s label (e.g.,
an example (x,Yes) that should be (x,No)) give a linear increase in prediction error, whereas
errors in the descriptions of examples (e.g., Price=$ when it was actually Price=$$) have
an asymptotic effect that gets worse as the tree shrinks down to smaller sets. Pruned trees
perform signiﬁcantly better than unpruned trees when the data contain a large amount of
noise. Also, the pruned trees are often much smaller and hence easier to understand and more
efﬁcient to execute.
One ﬁnal warning: You might think that χ2 pruning and information gain look similar,
so why not combine them using an approach called early stopping—have the decision tree
Early stopping
algorithm stop generating nodes when there is no good attribute to split on, rather than going
to all the trouble of generating nodes and then pruning them away. The problem with early
stopping is that it stops us from recognizing situations where there is no one good attribute,
but there are combinations of attributes that are informative. For example, consider the XOR
function of two binary attributes. If there are roughly equal numbers of examples for all
four combinations of input values, then neither attribute will be informative, yet the correct
thing to do is to split on one of the attributes (it doesn’t matter which one), and then at the
second level we will get splits that are very informative. Early stopping would miss this, but
generate-and-then-prune handles it correctly.
19.3.5 Broadening the applicability of decision trees
Decision trees can be made more widely useful by handling the following complications:
• Missing data: In many domains, not all the attribute values will be known for every
example. The values might have gone unrecorded, or they might be too expensive to
obtain. This gives rise to two problems: First, given a complete decision tree, how
should one classify an example that is missing one of the test attributes? Second, how
should one modify the information-gain formula when some examples have unknown
values for the attribute? These questions are addressed in Exercise 19.MISS.
• Continuous and multivalued input attributes: For continuous attributes like Height,
Weight, or Time, it may be that every example has a different attribute value. The
information gain measure would give its highest score to such an attribute, giving us a
shallow tree with this attribute at the root, and single-example subtrees for each possible
value below it. But that doesn’t help when we get a new example to classify with an
attribute value that we haven’t seen before.
A better way to deal with continuous values is a split point test—an inequality test
Split point
on the value of an attribute. For example, at a given node in the tree, it might be the
case that testing on Weight > 160 gives the most information. Efﬁcient methods exist
for ﬁnding good split points: start by sorting the values of the attribute, and then con-
sider only split points that are between two examples in sorted order that have different
