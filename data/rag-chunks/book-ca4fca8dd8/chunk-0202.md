---
chunk_id: "book-ca4fca8dd8-chunk-0202"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 202
confidence: "first-pass"
extraction_method: "structured-local"
---

122
Chapter 3
Solving Problems by Searching
state; for example, each computation step in A∗expands a leaf node and adds its successors
to the tree. Thus, Figure 3.18, which shows a sequence of larger and larger search trees, can
be seen as depicting a path in the metalevel state space where each state on the path is an
object-level search tree.
Now, the path in Figure 3.18 has ﬁve steps, including one step, the expansion of Fagaras,
that is not especially helpful. For harder problems, there will be many such missteps, and a
metalevel learning algorithm can learn from these experiences to avoid exploring unpromis-
Metalevel learning
ing subtrees. The techniques used for this kind of learning are described in Chapter 23. The
goal of learning is to minimize the total cost of problem solving, trading off computational
expense and path cost.
3.6.6 Learning heuristics from experience
We have seen that one way to invent a heuristic is to devise a relaxed problem for which an
optimal solution can be found easily. An alternative is to learn from experience. “Experience”
here means solving lots of 8-puzzles, for instance. Each optimal solution to an 8-puzzle
problem provides an example (goal, path) pair. From these examples, a learning algorithm can
be used to construct a function h that can (with luck) approximate the true path cost for other
states that arise during search. Most of these approaches learn an imperfect approximation
to the heuristic function, and thus risk inadmissibility. This leads to an inevitable tradeoff
between learning time, search run time, and solution cost. Techniques for machine learning
are demonstrated in Chapter 19. The reinforcement learning methods described in Chapter 23
are also applicable to search.
Some machine learning techniques work better when supplied with features of a state
Feature
that are relevant to predicting the state’s heuristic value, rather than with just the raw state
description. For example, the feature “number of misplaced tiles” might be helpful in pre-
dicting the actual distance of an 8-puzzle state from the goal. Let’s call this feature x1(n).
We could take 100 randomly generated 8-puzzle conﬁgurations and gather statistics on their
actual solution costs. We might ﬁnd that when x1(n) is 5, the average solution cost is around
14, and so on. Of course, we can use multiple features. A second feature x2(n) might be
“number of pairs of adjacent tiles that are not adjacent in the goal state.” How should x1(n)
and x2(n) be combined to predict h(n)? A common approach is to use a linear combination:
h(n) = c1x1(n)+c2x2(n).
The constants c1 and c2 are adjusted to give the best ﬁt to the actual data across the randomly
generated conﬁgurations. One expects both c1 and c2 to be positive because misplaced tiles
and incorrect adjacent pairs make the problem harder to solve. Notice that this heuristic sat-
isﬁes the condition h(n)=0 for goal states, but it is not necessarily admissible or consistent.
Summary
This chapter has introduced search algorithms that an agent can use to select action sequences
in a wide variety of environments—as long as they are episodic, single-agent, fully observ-
able, deterministic, static, discrete, and completely known. There are tradeoffs to be made
between the amount of time the search takes, the amount of memory available, and the qual-
ity of the solution. We can be more efﬁcient if we have domain-dependent knowledge in the
