---
chunk_id: "book-ca4fca8dd8-chunk-0155"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 155
confidence: "first-pass"
extraction_method: "structured-local"
---

92
Chapter 3
Solving Problems by Searching
We need a data structure to store the frontier. The appropriate choice is a queue of some
Queue
kind, because the operations on a frontier are:
• IS-EMPTY(frontier) returns true only if there are no nodes in the frontier.
• POP(frontier) removes the top node from the frontier and returns it.
• TOP(frontier) returns (but does not remove) the top node of the frontier.
• ADD(node, frontier) inserts node into its proper place in the queue.
Three kinds of queues are used in search algorithms:
• A priority queue ﬁrst pops the node with the minimum cost according to some evalu-
Priority queue
ation function, f. It is used in best-ﬁrst search.
• A FIFO queue or ﬁrst-in-ﬁrst-out queue ﬁrst pops the node that was added to the queue
FIFO queue
ﬁrst; we shall see it is used in breadth-ﬁrst search.
• A LIFO queue or last-in-ﬁrst-out queue (also known as a stack) pops ﬁrst the most
LIFO queue
Stack
recently added node; we shall see it is used in depth-ﬁrst search.
The reached states can be stored as a lookup table (e.g. a hash table) where each key is a state
and each value is the node for that state.
3.3.3 Redundant paths
The search tree shown in Figure 3.4 (bottom) includes a path from Arad to Sibiu and back to
Arad again. We say that Arad is a repeated state in the search tree, generated in this case by
Repeated state
a cycle (also known as a loopy path). So even though the state space has only 20 states, the
Cycle
Loopy path
complete search tree is inﬁnite because there is no limit to how often one can traverse a loop.
A cycle is a special case of a redundant path. For example, we can get to Sibiu via the
Redundant path
path Arad–Sibiu (140 miles long) or the path Arad–Zerind–Oradea–Sibiu (297 miles long).
This second path is redundant—it’s just a worse way to get to the same state—and need not
be considered in our quest for optimal paths.
Consider an agent in a 10 ×10 grid world, with the ability to move to any of 8 adjacent
squares. If there are no obstacles, the agent can reach any of the 100 squares in 9 moves or
fewer. But the number of paths of length 9 is almost 89 (a bit less because of the edges of
the grid), or more than 100 million. In other words, the average cell can be reached by over a
million redundant paths of length 9, and if we eliminate redundant paths, we can complete a
search roughly a million times faster. As the saying goes, algorithms that cannot remember
▶
the past are doomed to repeat it. There are three approaches to this issue.
First, we can remember all previously reached states (as best-ﬁrst search does), allowing
us to detect all redundant paths, and keep only the best path to each state. This is appropriate
for state spaces where there are many redundant paths, and is the preferred choice when the
table of reached states will ﬁt in memory.
Second, we can not worry about repeating the past. There are some problem formulations
where it is rare or impossible for two paths to reach the same state. An example would be an
assembly problem where each action adds a part to an evolving assemblage, and there is an
ordering of parts so that it is possible to add A and then B, but not B and then A. For those
problems, we could save memory space if we don’t track reached states and we don’t check
for redundant paths. We call a search algorithm a graph search if it checks for redundant
Graph search
paths and a tree-like search6 if it does not check. The BEST-FIRST-SEARCH algorithm in
Tree-like search
