---
chunk_id: "book-ca4fca8dd8-chunk-0629"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 629
confidence: "first-pass"
extraction_method: "structured-local"
---

382
Chapter 11
Automated Planning
function ANGELIC-SEARCH(problem,hierarchy,initialPlan) returns a solution or fail
frontier←a FIFO queue with initialPlan as the only element
while true do
if IS-EMPTY?(frontier) then return fail
plan←POP( frontier)
// chooses the shallowest node in frontier
if REACH+(problem.INITIAL,plan) intersects problem.GOAL then
if plan is primitive then return plan
// REACH+ is exact for primitive plans
guaranteed←REACH−(problem.INITIAL,plan) ∩problem.GOAL
if guaranteed̸={} and MAKING-PROGRESS(plan, initialPlan) then
ﬁnalState←any element of guaranteed
return DECOMPOSE(hierarchy,problem.INITIAL,plan,ﬁnalState)
hla←some HLA in plan
preﬁx,sufﬁx←the action subsequences before and after hla in plan
outcome←RESULT(problem.INITIAL, preﬁx)
for each sequence in REFINEMENTS(hla,outcome,hierarchy) do
add APPEND(preﬁx,sequence, sufﬁx) to frontier
function DECOMPOSE(hierarchy,s0,plan,sf ) returns a solution
solution←an empty plan
while plan is not empty do
action←REMOVE-LAST(plan)
si ←a state in REACH−(s0,plan) such that sf ∈REACH−(si,action)
problem←a problem with INITIAL = si and GOAL = sf
solution←APPEND(ANGELIC-SEARCH(problem,hierarchy,action),solution)
sf ←si
return solution
Figure 11.11 A hierarchical planning algorithm that uses angelic semantics to identify and
commit to high-level plans that work while avoiding high-level plans that don’t. The predi-
cate MAKING-PROGRESS checks to make sure that we aren’t stuck in an inﬁnite regression
of reﬁnements. At top level, call ANGELIC-SEARCH with [Act] as the initialPlan.
The ability to commit to or reject high-level plans can give ANGELIC-SEARCH a sig-
niﬁcant computational advantage over HIERARCHICAL-SEARCH, which in turn may have a
large advantage over plain old BREADTH-FIRST-SEARCH. Consider, for example, cleaning
up a large vacuum world consisting of an arrangement of rooms connected by narrow corri-
dors, where each room is a w × h rectangle of squares. It makes sense to have an HLA for
Navigate (as shown in Figure 11.7) and one for CleanWholeRoom. (Cleaning the room could
be implemented with the repeated application of another HLA to clean each row.) Since there
are ﬁve primitive actions, the cost for BREADTH-FIRST-SEARCH grows as 5d, where d is the
length of the shortest solution (roughly twice the total number of squares); the algorithm
cannot manage even two 3×3 rooms. HIERARCHICAL-SEARCH is more efﬁcient, but still
suffers from exponential growth because it tries all ways of cleaning that are consistent with
the hierarchy. ANGELIC-SEARCH scales approximately linearly in the number of squares—
it commits to a good high-level sequence of room-cleaning and navigation steps and prunes
away the other options.
