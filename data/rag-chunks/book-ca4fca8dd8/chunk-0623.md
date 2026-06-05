---
chunk_id: "book-ca4fca8dd8-chunk-0623"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 623
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.4
Hierarchical Planning
377
function HIERARCHICAL-SEARCH(problem,hierarchy) returns a solution or failure
frontier←a FIFO queue with [Act] as the only element
while true do
if IS-EMPTY( frontier) then return failure
plan←POP( frontier)
// chooses the shallowest plan in frontier
hla←the ﬁrst HLA in plan, or null if none
preﬁx,sufﬁx←the action subsequences before and after hla in plan
outcome←RESULT(problem.INITIAL, preﬁx)
if hla is null then
// so plan is primitive and outcome is its result
if problem.IS-GOAL(outcome) then return plan
else for each sequence in REFINEMENTS(hla,outcome,hierarchy) do
add APPEND(preﬁx,sequence,sufﬁx) to frontier
Figure 11.8 A breadth-ﬁrst implementation of hierarchical forward planning search. The
initial plan supplied to the algorithm is [Act]. The REFINEMENTS function returns a set of
action sequences, one for each reﬁnement of the HLA whose preconditions are satisﬁed by
the speciﬁed state, outcome.
In essence, this form of hierarchical search explores the space of sequences that conform
to the knowledge contained in the HLA library about how things are to be done. A great deal
of knowledge can be encoded, not just in the action sequences speciﬁed in each reﬁnement but
also in the preconditions for the reﬁnements. For some domains, HTN planners have been
able to generate huge plans with very little search. For example, O-PLAN (Bell and Tate,
1985), which combines HTN planning with scheduling, has been used to develop production
plans for Hitachi. A typical problem involves a product line of 350 different products, 35
assembly machines, and over 2000 different operations. The planner generates a 30-day
schedule with three 8-hour shifts a day, involving tens of millions of steps. Another important
aspect of HTN plans is that they are, by deﬁnition, hierarchically structured; usually this
makes them easy for humans to understand.
The computational beneﬁts of hierarchical search can be seen by examining an ideal-
ized case. Suppose that a planning problem has a solution with d primitive actions. For
a nonhierarchical, forward state-space planner with b allowable actions at each state, the
cost is O(bd), as explained in Chapter 3. For an HTN planner, let us suppose a very reg-
ular reﬁnement structure: each nonprimitive action has r possible reﬁnements, each into
k actions at the next lower level. We want to know how many different reﬁnement trees
there are with this structure. Now, if there are d actions at the primitive level, then the
number of levels below the root is logk d, so the number of internal reﬁnement nodes is
1+k +k2 +···+klogk d−1 = (d −1)/(k −1). Each internal node has r possible reﬁnements,
so r(d−1)/(k−1) possible decomposition trees could be constructed.
Examining this formula, we see that keeping r small and k large can result in huge sav-
ings: we are taking the kth root of the nonhierarchical cost, if b and r are comparable. Small r
and large k means a library of HLAs with a small number of reﬁnements each yielding a long
action sequence. This is not always possible: long action sequences that are usable across a
wide range of problems are extremely rare.
