---
chunk_id: "book-ca4fca8dd8-chunk-1037"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1037
confidence: "first-pass"
extraction_method: "structured-local"
---

622
Chapter 17
Multiagent Decision Making
For example, there is an edge from {{1},{2,3,4}} to {{1},{2},{3,4}} because this latter
coalition structure is obtained from the former by dividing the coalition {2,3,4} into the
coalitions {2} and {3,4}.
The optimal coalition structure CS∗lies somewhere within the coalition structure graph,
and so to ﬁnd this, it seems we would have to evaluate every node in the graph. But consider
the bottom two rows of the graph—levels 1 and 2. Every possible coalition (excluding the
empty coalition) appears in these two levels. (Of course, not every possible coalition structure
appears in these two levels.) Now, suppose we restrict our search for a possible coalition
structure to just these two levels—we go no higher in the graph. Let CS′ be the best coalition
structure that we ﬁnd in these two levels, and let CS∗be the best coalition structure overall.
Let C∗be a coalition with the highest value of all possible coalitions:
C∗∈argmax
C⊆N ν(C).
The value of the best coalition structure we ﬁnd in the ﬁrst two levels of the coalition structure
graph must be at least as much as the value of the best possible coalition: sw(CS′) ≥ν(C∗).
This is because every possible coalition appears in at least one coalition structure in the ﬁrst
two levels of the graph. So assume the worst case, that is, sw(CS′) = ν(C∗).
Compare the value of sw(CS′) to sw(CS∗). Since sw(CS′) is the highest possible value
of any coalition structure, and there are n agents (n = 4 in the case of Figure 17.7), then the
highest possible value of sw(CS∗) would be nν(C∗) = n · sw(CS′). In other words, in the
worst possible case, the value of the best coalition structure we ﬁnd in the ﬁrst two levels of
the graph would be 1
n the value of the best, where n is the number of agents. Thus, although
searching the ﬁrst two levels of the graph does not guarantee to give us the optimal coalition
structure, it does guarantee to give us one that is no worse that 1
n of the optimal. In practice it
will often be much better than that.
17.4 Making Collective Decisions
We will now turn from agent design to mechanism design—the problem of designing the
right game for a collection of agents to play. Formally, a mechanism consists of
1. A language for describing the set of allowable strategies that agents may adopt.
2. A distinguished agent, called the center, that collects reports of strategy choices from
Center
the agents in the game. (For example, the auctioneer is the center in an auction.)
3. An outcome rule, known to all agents, that the center uses to determine the payoffs to
each agent, given their strategy choices.
This section discusses some of the most important mechanisms.
17.4.1 Allocating tasks with the contract net
The contract net protocol is probably the oldest and most important multiagent problem-
Contract net
protocol
solving technique studied in AI. It is a high-level protocol for task sharing. As the name
suggests, the contract net was inspired from the way that companies make use of contracts.
The overall contract net protocol has four main phases—see Figure 17.8. The process
starts with an agent identifying the need for cooperative action with respect to some task.
The need might arise because the agent does not have the capability to carry out the task
