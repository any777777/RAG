---
chunk_id: "book-ca4fca8dd8-chunk-1248"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1248
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 753

Section 20.3
Explanation-Based Learning
753
Primitive(X)
ArithmeticUnknown(X)
Primitive(z)
ArithmeticUnknown(z)
Simplify(X,w)
Yes, {  }
Yes, {x / 1, v / y+z}
Simplify(y+z,w)
Rewrite(y+z,v')
Yes, {y / 0, v'/ z}
{w / X}
Yes, {  }
Yes, {v / 0+X}
Yes, {v' / X}
Simplify(z,w)
{w / z}
Simplify(1 × (0+X),w)
Rewrite(x × (y+z),v)
Simplify(x × (y+z),w)
Rewrite(1 × (0+X),v)
Simplify(0+X,w)
Rewrite(0+X,v')
Figure 20.7 Proof trees for the simpliﬁcation problem. The ﬁrst tree shows the proof for the
original problem instance, from which we can derive
ArithmeticUnknown(z) ⇒Simplify(1×(0+z),z) .
The second tree shows the proof for a problem instance with all constants replaced by vari-
ables, from which we can derive a variety of other rules.
This rule is as valid as, but more general than, the rule using ArithmeticUnknown, because it
covers cases where z is a number. We can extract a still more general rule by pruning after
the step Simplify(y+z,w), yielding the rule
Simplify(y+z,w) ⇒Simplify(1×(y+z),w) .
In general, a rule can be extracted from any partial subtree of the generalized proof tree. Now
we have a problem: which of these rules do we choose?
The choice of which rule to generate comes down to the question of efﬁciency. There are
three factors involved in the analysis of efﬁciency gains from EBL:
1. Adding large numbers of rules can slow down the reasoning process, because the in-
ference mechanism must still check those rules even in cases where they do not yield a
solution. In other words, it increases the branching factor in the search space.
2. To compensate for the slowdown in reasoning, the derived rules must offer signiﬁcant
increases in speed for the cases that they do cover. These increases come about mainly
because the derived rules avoid dead ends that would otherwise be taken, but also be-
cause they shorten the proof itself.
3. Derived rules should be as general as possible, so that they apply to the largest possible
set of cases.

## Page 754
