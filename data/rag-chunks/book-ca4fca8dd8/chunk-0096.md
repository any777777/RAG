---
chunk_id: "book-ca4fca8dd8-chunk-0096"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 96
confidence: "first-pass"
extraction_method: "structured-local"
---

58
Chapter 2
Intelligent Agents
page 51. Moreover, when designing one piece of software, copies of which will belong to
different users, we cannot anticipate the exact preferences of each individual user. Thus, we
may need to build agents that reﬂect initial uncertainty about the true performance measure
and learn more about it as time goes by; such agents are described in Chapters 15, 17, and 23.
2.2.2 Rationality
What is rational at any given time depends on four things:
• The performance measure that deﬁnes the criterion of success.
• The agent’s prior knowledge of the environment.
• The actions that the agent can perform.
• The agent’s percept sequence to date.
This leads to a deﬁnition of a rational agent:
Deﬁnition of a
rational agent ▶
For each possible percept sequence, a rational agent should select an action that is ex-
pected to maximize its performance measure, given the evidence provided by the percept
sequence and whatever built-in knowledge the agent has.
Consider the simple vacuum-cleaner agent that cleans a square if it is dirty and moves to the
other square if not; this is the agent function tabulated in Figure 2.3. Is this a rational agent?
That depends! First, we need to say what the performance measure is, what is known about
the environment, and what sensors and actuators the agent has. Let us assume the following:
• The performance measure awards one point for each clean square at each time step,
over a “lifetime” of 1000 time steps.
• The “geography” of the environment is known a priori (Figure 2.2) but the dirt distri-
bution and the initial location of the agent are not. Clean squares stay clean and sucking
cleans the current square. The Right and Left actions move the agent one square ex-
cept when this would take the agent outside the environment, in which case the agent
remains where it is.
• The only available actions are Right, Left, and Suck.
• The agent correctly perceives its location and whether that location contains dirt.
Under these circumstances the agent is indeed rational; its expected performance is at least
as good as any other agent’s.
One can see easily that the same agent would be irrational under different circumstances.
For example, once all the dirt is cleaned up, the agent will oscillate needlessly back and forth;
if the performance measure includes a penalty of one point for each movement, the agent will
fare poorly. A better agent for this case would do nothing once it is sure that all the squares
are clean. If clean squares can become dirty again, the agent should occasionally check and
re-clean them if needed. If the geography of the environment is unknown, the agent will need
to explore it. Exercise 2.VACR asks you to design agents for these cases.
2.2.3 Omniscience, learning, and autonomy
We need to be careful to distinguish between rationality and omniscience. An omniscient
Omniscience
agent knows the actual outcome of its actions and can act accordingly; but omniscience is
impossible in reality. Consider the following example: I am walking along the Champs
Elys´ees one day and I see an old friend across the street. There is no trafﬁc nearby and I’m
