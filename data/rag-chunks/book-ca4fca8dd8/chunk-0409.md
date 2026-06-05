---
chunk_id: "book-ca4fca8dd8-chunk-0409"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 409
confidence: "first-pass"
extraction_method: "structured-local"
---

252
Chapter 7
Logical Agents
function DPLL-SATISFIABLE?(s) returns true or false
inputs: s, a sentence in propositional logic
clauses←the set of clauses in the CNF representation of s
symbols←a list of the proposition symbols in s
return DPLL(clauses,symbols,{})
function DPLL(clauses,symbols,model) returns true or false
if every clause in clauses is true in model then return true
if some clause in clauses is false in model then return false
P,value←FIND-PURE-SYMBOL(symbols,clauses,model)
if P is non-null then return DPLL(clauses,symbols – P,model ∪{P=value})
P,value←FIND-UNIT-CLAUSE(clauses,model)
if P is non-null then return DPLL(clauses,symbols – P,model ∪{P=value})
P←FIRST(symbols); rest←REST(symbols)
return DPLL(clauses,rest,model ∪{P=true}) or
DPLL(clauses,rest,model ∪{P=false})
Figure 7.17 The DPLL algorithm for checking satisﬁability of a sentence in propositional
logic. The ideas behind FIND-PURE-SYMBOL and FIND-UNIT-CLAUSE are described in
the text; each returns a symbol (or null) and the truth value to assign to that symbol. Like
TT-ENTAILS?, DPLL operates over partial models.
1. Component analysis (as seen with Tasmania in CSPs): As DPLL assigns truth values
to variables, the set of clauses may become separated into disjoint subsets, called com-
ponents, that share no unassigned variables. Given an efﬁcient way to detect when this
occurs, a solver can gain considerable speed by working on each component separately.
2. Variable and value ordering (as seen in Section 5.3.1 for CSPs): Our simple imple-
mentation of DPLL uses an arbitrary variable ordering and always tries the value true
before false. The degree heuristic (see page 177) suggests choosing the variable that
appears most frequently over all remaining clauses.
3. Intelligent backtracking (as seen in Section 5.3.3 for CSPs): Many problems that
cannot be solved in hours of run time with chronological backtracking can be solved
in seconds with intelligent backtracking that backs up all the way to the relevant point
of conﬂict. All SAT solvers that do intelligent backtracking use some form of conﬂict
clause learning to record conﬂicts so that they won’t be repeated later in the search.
Usually a limited-size set of conﬂicts is kept, and rarely used ones are dropped.
4. Random restarts (as seen on page 131 for hill climbing): Sometimes a run appears not
to be making progress. In this case, we can start over from the top of the search tree,
rather than trying to continue. After restarting, different random choices (in variable
and value selection) are made. Clauses that are learned in the ﬁrst run are retained after
the restart and can help prune the search space. Restarting does not guarantee that a
solution will be found faster, but it does reduce the variance on the time to solution.
5. Clever indexing (as seen in many algorithms): The speedup methods used in DPLL
itself, as well as the tricks used in modern solvers, require fast indexing of such things
