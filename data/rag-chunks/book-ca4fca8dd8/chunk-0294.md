---
chunk_id: "book-ca4fca8dd8-chunk-0294"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 294
confidence: "first-pass"
extraction_method: "structured-local"
---

180
Chapter 5
Constraint Satisfaction Problems
The eagle-eyed reader may have noticed something odd: backjumping occurs when ev-
ery value in a domain is in conﬂict with the current assignment; but forward checking detects
this event and prevents the search from ever reaching such a node! In fact, it can be shown
that every branch pruned by backjumping is also pruned by forward checking. Hence, sim-
ple backjumping is redundant in a forward-checking search or, indeed, in a search that uses
stronger consistency checking, such as MAC—you need only do one or the other.
Despite the observations of the preceding paragraph, the idea behind backjumping re-
mains a good one: to backtrack based on the reasons for failure. Backjumping notices failure
when a variable’s domain becomes empty, but in many cases a branch is doomed long before
this occurs. Consider again the partial assignment {WA=red,NSW =red} (which, from our
earlier discussion, is inconsistent). Suppose we try T =red next and then assign NT, Q, V,
SA. We know that no assignment can work for these last four variables, so eventually we run
out of values to try at NT. Now, the question is, where to backtrack? Backjumping cannot
work, because NT does have values consistent with the preceding assigned variables—NT
doesn’t have a complete conﬂict set of preceding variables that caused it to fail. We know,
however, that the four variables NT, Q, V, and SA, taken together, failed because of a set of
preceding variables, which must be those variables that directly conﬂict with the four.
This leads to a different–and deeper–notion of the conﬂict set for a variable such as NT:
it is that set of preceding variables that caused NT, together with any subsequent variables,
to have no consistent solution. In this case, the set is WA and NSW, so the algorithm should
backtrack to NSW and skip over Tasmania. A backjumping algorithm that uses conﬂict sets
deﬁned in this way is called conﬂict-directed backjumping.
Conﬂict-directed
backjumping
We must now explain how these new conﬂict sets are computed. The method is in fact
quite simple. The “terminal” failure of a branch of the search always occurs because a vari-
able’s domain becomes empty; that variable has a standard conﬂict set. In our example, SA
fails, and its conﬂict set is (say) {WA,NT,Q}. We backjump to Q, and Q absorbs the conﬂict
set from SA (minus Q itself, of course) into its own direct conﬂict set, which is {NT,NSW};
the new conﬂict set is {WA,NT,NSW}. That is, there is no solution from Q onward, given
the preceding assignment to {WA,NT,NSW}. Therefore, we backtrack to NT, the most recent
of these. NT absorbs {WA,NT,NSW} −{NT} into its own direct conﬂict set {WA}, giving
{WA,NSW} (as stated in the previous paragraph). Now the algorithm backjumps to NSW, as
we would hope. To summarize: let Xj be the current variable, and let conf(Xj) be its conﬂict
set. If every possible value for Xj fails, backjump to the most recent variable Xi in conf(Xj)
and recompute the conﬂict set for Xi as follows:
conf(Xi) ←conf(Xi)∪conf(Xj)−{Xi}.
5.3.4 Constraint learning
When we reach a contradiction, backjumping can tell us how far to back up, so we don’t
waste time changing variables that won’t ﬁx the problem. But we would also like to avoid
running into the same problem again. When the search arrives at a contradiction, we know
that some subset of the conﬂict set is responsible for the problem. Constraint learning is
Constraint learning
the idea of ﬁnding a minimum set of variables from the conﬂict set that causes the problem.
This set of variables, along with their corresponding values, is called a no-good. We then
No-good
record the no-good, either by adding a new constraint to the CSP to forbid this combination
of assignments or by keeping a separate cache of no-goods.
