---
chunk_id: "book-ca4fca8dd8-chunk-1247"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1247
confidence: "first-pass"
extraction_method: "structured-local"
---

752
Chapter 20
Knowledge in Learning
Rewrite(u,v)∧Simplify(v,w) ⇒Simplify(u,w) .
Primitive(u) ⇒Simplify(u,u) .
ArithmeticUnknown(u) ⇒Primitive(u) .
Number(u) ⇒Primitive(u) .
Rewrite(1×u,u) .
Rewrite(0+u,u) .
...
The proof that the answer is X is shown in the top half of Figure 20.7. The EBL method
actually constructs two proof trees simultaneously. The second proof tree uses a variabilized
goal in which the constants from the original goal are replaced by variables. As the original
proof proceeds, the variabilized proof proceeds in step, using exactly the same rule applica-
tions. This could cause some of the variables to become instantiated. For example, in order
to use the rule Rewrite(1×u,u), the variable x in the subgoal Rewrite(x×(y+z),v) must be
bound to 1. Similarly, y must be bound to 0 in the subgoal Rewrite(y + z,v′) in order to use
the rule Rewrite(0+u,u). Once we have the generalized proof tree, we take the leaves (with
the necessary bindings) and form a general rule for the goal predicate:
Rewrite(1×(0+z),0+z)∧Rewrite(0+z,z)∧ArithmeticUnknown(z)
⇒Simplify(1×(0+z),z) .
Notice that the ﬁrst two conditions on the left-hand side are true regardless of the value of z.
We can therefore drop them from the rule, yielding
ArithmeticUnknown(z) ⇒Simplify(1×(0+z),z) .
In general, conditions can be dropped from the ﬁnal rule if they impose no constraints on the
variables on the right-hand side of the rule, because the resulting rule will still be true and will
be more efﬁcient. Notice that we cannot drop the condition ArithmeticUnknown(z), because
not all possible values of z are arithmetic unknowns. Values other than arithmetic unknowns
might require different forms of simpliﬁcation: for example, if z were 2×3, then the correct
simpliﬁcation of 1×(0+(2×3)) would be 6 and not 2×3.
To recap, the basic EBL process works as follows:
1. Given an example, construct a proof that the goal predicate applies to the example using
the available background knowledge.
2. In parallel, construct a generalized proof tree for the variabilized goal using the same
inference steps as in the original proof.
3. Construct a new rule whose left-hand side consists of the leaves of the proof tree and
whose right-hand side is the variabilized goal (after applying the necessary bindings
from the generalized proof).
4. Drop any conditions from the left-hand side that are true regardless of the values of the
variables in the goal.
20.3.2 Improving eﬃciency
The generalized proof tree in Figure 20.7 actually yields more than one generalized rule. For
example, if we terminate, or prune, the growth of the right-hand branch in the proof tree
when it reaches the Primitive step, we get the rule
Primitive(z) ⇒Simplify(1×(0+z),z) .
