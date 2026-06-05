---
chunk_id: "book-ca4fca8dd8-chunk-0213"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 213
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 129

Section 4.1
Local Search and Optimization Problems
129
current
state
objective function
state space
global maximum
local maximum
“flat” local maximum
shoulder
Figure 4.1 A one-dimensional state-space landscape in which elevation corresponds to the
objective function. The aim is to ﬁnd the global maximum.
function HILL-CLIMBING(problem) returns a state that is a local maximum
current←problem.INITIAL
while true do
neighbor←a highest-valued successor state of current
if VALUE(neighbor) ≤VALUE(current) then return current
current←neighbor
Figure 4.2 The hill-climbing search algorithm, which is the most basic local search tech-
nique. At each step the current node is replaced by the best neighbor.
then the aim is to ﬁnd the highest peak—a global maximum—and we call the process hill
Global maximum
climbing. If elevation corresponds to cost, then the aim is to ﬁnd the lowest valley—a global
minimum—and we call it gradient descent.
Global minimum
4.1.1 Hill-climbing search
The hill-climbing search algorithm is shown in Figure 4.2. It keeps track of one current state
Hill climbing
and on each iteration moves to the neighboring state with highest value—that is, it heads in
the direction that provides the steepest ascent. It terminates when it reaches a “peak” where
Steepest ascent
no neighbor has a higher value. Hill climbing does not look ahead beyond the immediate
neighbors of the current state. This resembles trying to ﬁnd the top of Mount Everest in a
thick fog while suffering from amnesia. Note that one way to use hill-climbing search is to
use the negative of a heuristic cost function as the objective function; that will climb locally
to the state with smallest heuristic distance to the goal.
To illustrate hill climbing, we will use the 8-queens problem (Figure 4.3). We will use
a complete-state formulation, which means that every state has all the components of a
Complete-state
formulation
solution, but they might not all be in the right place. In this case every state has 8 queens

## Page 130
