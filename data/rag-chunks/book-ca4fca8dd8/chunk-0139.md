---
chunk_id: "book-ca4fca8dd8-chunk-0139"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 139
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 3
SOLVING PROBLEMS BY SEARCHING
In which we see how an agent can look ahead to ﬁnd a sequence of actions that will even-
tually achieve its goal.
When the correct action to take is not immediately obvious, an agent may need to plan
ahead: to consider a sequence of actions that form a path to a goal state. Such an agent is
called a problem-solving agent, and the computational process it undertakes is called search.
Problem-solving
agent
Search
Problem-solving agents use atomic representations, as described in Section 2.4.7—that
is, states of the world are considered as wholes, with no internal structure visible to the
problem-solving algorithms. Agents that use factored or structured representations of states
are called planning agents and are discussed in Chapters 7 and 11.
We will cover several search algorithms. In this chapter, we consider only the simplest
environments: episodic, single agent, fully observable, deterministic, static, discrete, and
known. We distinguish between informed algorithms, in which the agent can estimate how
far it is from the goal, and uninformed algorithms, where no such estimate is available.
Chapter 4 relaxes the constraints on environments, and Chapter 6 considers multiple agents.
This chapter uses the concepts of asymptotic complexity (that is, O(n) notation). Readers
unfamiliar with these concepts should consult Appendix A.
3.1 Problem-Solving Agents
Imagine an agent enjoying a touring vacation in Romania. The agent wants to take in the
sights, improve its Romanian, enjoy the nightlife, avoid hangovers, and so on. The decision
problem is a complex one. Now, suppose the agent is currently in the city of Arad and
has a nonrefundable ticket to ﬂy out of Bucharest the following day. The agent observes
street signs and sees that there are three roads leading out of Arad: one toward Sibiu, one to
Timisoara, and one to Zerind. None of these are the goal, so unless the agent is familiar with
the geography of Romania, it will not know which road to follow.1
If the agent has no additional information—that is, if the environment is unknown—then
the agent can do no better than to execute one of the actions at random. This sad situation
is discussed in Chapter 4. In this chapter, we will assume our agents always have access to
information about the world, such as the map in Figure 3.1. With that information, the agent
can follow this four-phase problem-solving process:
• Goal formulation: The agent adopts the goal of reaching Bucharest. Goals organize
Goal formulation
behavior by limiting the objectives and hence the actions to be considered.
1
We are assuming that most readers are in the same position and can easily imagine themselves to be as clueless
as our agent. We apologize to Romanian readers who are unable to take advantage of this pedagogical device.
