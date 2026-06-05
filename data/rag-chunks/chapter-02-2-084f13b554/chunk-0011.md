---
chunk_id: "chapter-02-2-084f13b554-chunk-0011"
source_id: "chapter-02-2-084f13b554"
source_file: "New folder/Chapter 02 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 11
confidence: "first-pass"
extraction_method: "structured-local"
---

Choosing the utility-maximizing course of action is a difficult task, requiring clever algorithms. 
Even with these algorithms, perfect rationality is usually unachievable in practice 
because of computational complexity. 
Can the designer always specify the utility function correctly? 
Chapters 16, 17, and 23 consider the issue of unknown utility functions in more depth.

55

… Utility-based agents: Challenges

## Slide 56

56

… Utility-based agents

## Slide 57

Any type of agent (model-based, goal-based, utility-based, etc.) can be built as a learning agent (or not).
The simplest cases involve learning directly from the percept sequence. 
Observation of pairs of successive states of the environment can allow the agent to learn “What my actions do” and “How the world evolves” in response to its actions.

57

2.4.6 Learning agents

## Slide 58

58

… Learning agents

(fixed)

They can learn to improve
Operate in initially unknown environments and become more competent
Four components:
Learning element: making improvements
Performance element:
it takes in percepts and decides on actions
Critic: It tells the learning element how well the agent is doing
Problem generator: It suggests actions that will lead to new and informative experiences

If the performance element had its way, it would keep doing the actions that are best, given what it knows, but if the agent is willing to explore a little and do some perhaps suboptimal actions in the short run, it might discover much better actions for the long run.

## Slide 59

Agents interact with environments through actuators and sensors
The agent function describes what the agent does in all circumstances The performance measure evaluates the environment sequence
A perfectly rational agent maximizes expected performance 
Agent programs implement (some) agent functions
PEAS descriptions define task environments 
Environments are categorized along several dimensions:
observable? deterministic? episodic? static? discrete? single-agent?
Several basic agent architectures exist:
reflex, model based, goal-based, utility-based

Summary
