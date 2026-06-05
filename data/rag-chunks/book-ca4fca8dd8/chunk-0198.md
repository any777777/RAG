---
chunk_id: "book-ca4fca8dd8-chunk-0198"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 198
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.6
Heuristic Functions
119
Start State
Goal State
1
2
3
4
6
8
5
2
1
3
6
7
8
54
Figure 3.27 A subproblem of the 8-puzzle instance given in Figure 3.25. The task is to
get tiles 1, 2, 3, 4, and the blank into their correct positions, without worrying about what
happens to the other tiles.
the cost of the complete problem. It turns out to be more accurate than Manhattan distance in
some cases.
The idea behind pattern databases is to store these exact solution costs for every possible
Pattern database
subproblem instance—in our example, every possible conﬁguration of the four tiles and the
blank. (There will be 9 × 8 × 7 × 6 × 5=15,120 patterns in the database. The identities
of the other four tiles are irrelevant for the purposes of solving the subproblem, but moves
of those tiles do count toward the solution cost of the subproblem.) Then we compute an
admissible heuristic hDB for each state encountered during a search simply by looking up the
corresponding subproblem conﬁguration in the database. The database itself is constructed
by searching back from the goal and recording the cost of each new pattern encountered;15
the expense of this search is amortized over subsequent problem instances, and so makes
sense if we expect to be asked to solve many problems.
The choice of tiles 1-2-3-4 to go with the blank is fairly arbitrary; we could also construct
databases for 5-6-7-8, for 2-4-6-8, and so on. Each database yields an admissible heuristic,
and these heuristics can be combined, as explained earlier, by taking the maximum value.
A combined heuristic of this kind is much more accurate than the Manhattan distance; the
number of nodes generated when solving random 15-puzzles can be reduced by a factor of
1000. However, with each additional database there are diminishing returns and increased
memory and computation costs.
One might wonder whether the heuristics obtained from the 1-2-3-4 database and the 5-
6-7-8 could be added, since the two subproblems seem not to overlap. Would this still give
an admissible heuristic? The answer is no, because the solutions of the 1-2-3-4 subproblem
and the 5-6-7-8 subproblem for a given state will almost certainly share some moves—it
is unlikely that 1-2-3-4 can be moved into place without touching 5-6-7-8, and vice versa.
But what if we don’t count those moves—what if we don’t abstract the other tiles to stars,
but rather make them disappear? That is, we record not the total cost of solving the 1-2-3-4
subproblem, but just the number of moves involving 1-2-3-4. Then the sum of the two costs is
still a lower bound on the cost of solving the entire problem. This is the idea behind disjoint
pattern databases. With such databases, it is possible to solve random 15-puzzles in a few
Disjoint pattern
databases
15 By working backward from the goal, the exact solution cost of every instance encountered is immediately
available. This is an example of dynamic programming, which we discuss further in Chapter 16.
