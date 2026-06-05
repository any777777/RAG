---
chunk_id: "book-ca4fca8dd8-chunk-0268"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 268
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 5.1
Deﬁning Constraint Satisfaction Problems
165
CSPs deal with assignments of values to variables, {Xi = vi,Xj = vj,...}. An assignment
Assignments
that does not violate any constraints is called a consistent or legal assignment. A complete
Consistent
assignment is one in which every variable is assigned a value, and a solution to a CSP is
Complete
assignment
Solution
a consistent, complete assignment. A partial assignment is one that leaves some variables
Partial assignment
unassigned, and a partial solution is a partial assignment that is consistent. Solving a CSP
Partial solution
is an NP-complete problem in general, although there are important subclasses of CSPs that
can be solved very efﬁciently.
5.1.1 Example problem: Map coloring
Suppose that, having tired of Romania, we are looking at a map of Australia showing each of
its states and territories (Figure 5.1(a)). We are given the task of coloring each region either
red, green, or blue in such a way that no two neighboring regions have the same color. To
formulate this as a CSP, we deﬁne the variables to be the regions:
X = {WA,NT,Q,NSW,V,SA,T}.
The domain of every variable is the set Di = {red,green,blue}. The constraints require neigh-
boring regions to have distinct colors. Since there are nine places where regions border, there
are nine constraints:
C = {SA ̸= WA,SA ̸= NT,SA ̸= Q,SA ̸= NSW,SA ̸= V,
WA ̸= NT,NT ̸= Q,Q ̸= NSW,NSW ̸= V}.
Here we are using abbreviations; SA ̸= WA is a shortcut for ⟨(SA,WA),SA ̸= WA⟩, where
SA ̸= WA can be fully enumerated in turn as
{(red,green),(red,blue),(green,red),(green,blue),(blue,red),(blue,green)}.
There are many possible solutions to this problem, such as
{WA=red,NT =green,Q=red,NSW =green,V =red,SA=blue,T =red }.
It can be helpful to visualize a CSP as a constraint graph, as shown in Figure 5.1(b). The
Constraint graph
nodes of the graph correspond to variables of the problem, and an edge connects any two
variables that participate in a constraint.
Why formulate a problem as a CSP? One reason is that the CSPs yield a natural repre-
sentation for a wide variety of problems; it is often easy to formulate a problem as a CSP.
Another is that years of development work have gone into making CSP solvers fast and ef-
ﬁcient. A third is that a CSP solver can quickly prune large swathes of the search space
that an atomic state-space searcher cannot. For example, once we have chosen {SA=blue}
in the Australia problem, we can conclude that none of the ﬁve neighboring variables can
take on the value blue. A search procedure that does not use constraints would have to con-
sider 35 =243 assignments for the ﬁve neighboring variables; with constraints we have only
25 =32 assignments to consider, a reduction of 87%.
In atomic state-space search we can only ask: is this speciﬁc state a goal? No? What
about this one? With CSPs, once we ﬁnd out that a partial assignment violates a constraint,
we can immediately discard further reﬁnements of the partial assignment. Furthermore, we
can see why the assignment is not a solution—we see which variables violate a constraint—
so we can focus attention on the variables that matter. As a result, many problems that are
intractable for atomic state-space search can be solved quickly when formulated as a CSP.
