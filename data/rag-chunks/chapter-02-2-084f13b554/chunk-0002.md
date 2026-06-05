---
chunk_id: "chapter-02-2-084f13b554-chunk-0002"
source_id: "chapter-02-2-084f13b554"
source_file: "New folder/Chapter 02 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

In a sense, all areas of engineering can be seen as designing artifacts that interact with the world; 
AI operates at the most interesting end of the spectrum, where:
the artifacts (object made by a human being)  have significant computational resources 
and the task environment requires nontrivial decision making.

11

… Agents and Environments

## Slide 12

A rational agent is one that does the right thing. 
Obviously, doing the right thing is better than doing the wrong thing, 
but what does it mean to do the right thing?

12

## Slide 13

2.2.1 Performance measures

“right thing”?
Consequentialism: we evaluate an agent’s behavior by its consequences. 
When an agent is put down in an environment, it generates a sequence of actions according to the percepts it receives. 
This sequence of actions causes the environment to go through a sequence of states. 
If the sequence is desirable, then the agent has performed well. 
This notion of desirability is captured by a performance measure that evaluates any given sequence of environment states.

13

## Slide 14

Machines do not have desires and preferences of their own; 
the performance measure is, initially at least, in the mind of the designer of the machine, 
or in the mind of the users the machine is designed for.
It can be quite hard to formulate a performance measure correctly. 
Consider, for example, the vacuum-cleaner agent
As a general rule, it is better to design performance measures according to what one actually wants to be achieved in the environment, rather than according to how one thinks the agent should behave.

14

… Performance measures

## Slide 15

What is rational at any given time depends on four things:
The performance measure that defines the criterion of success.
The agent’s prior knowledge of the environment.
The actions that the agent can perform.
The agent’s percept sequence to date.

A definition of a rational agent:
For each possible percept sequence, a rational agent should select an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.

15

2.2.2 Rationality

## Slide 16
