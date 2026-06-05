---
chunk_id: "chapter-02-2-084f13b554-chunk-0008"
source_id: "chapter-02-2-084f13b554"
source_file: "New folder/Chapter 02 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 8
confidence: "first-pass"
extraction_method: "structured-local"
---

TABLE-DRIVEN-AGENT does do what we want, 
assuming the table is filled in correctly: 
it implements the desired agent function.
The key challenge for AI is to find out how to write programs that, to the extent possible, produce rational behavior from a smallish program rather than from a vast table.
Next, we will consider:
Simple reflex agents
Model-based reflex agents
Goal-based agents
Utility-based agents

40

… Agent programs

## Slide 41

41

Four basic types in order of increasing generality

Agent Types

All these can be turned into learning agents

## Slide 42

2.4.2 Simple reflex agents

These agents select actions on the basis of the current percept, ignoring the rest of the percept history.

Condition–action rule:
if car-in-front-is-braking then initiate-braking.

42

## Slide 43

43

… Simple reflex agents

## Slide 44

The agent will work only if the correct decision can be made on the basis of just the current percept—
that is, only if the environment is fully observable.
Even a little bit of unobservability can cause serious trouble (the condition might not fullfilled).

44

… Simple reflex agents

## Slide 45

Infinite loops are often unavoidable for simple reflex agents operating in partially observable environments.
Escape from infinite loops is possible if the agent can randomize its actions.
A randomized simple reflex agent might outperform a deterministic simple reflex agent.
Randomized behavior of the right kind can be rational in some multiagent environments. 
In single-ageint environments, randomization is usually not rational. 
It is a useful trick (randomization) that helps a simple reflex agent in some situations, 
but in most cases, we can do much better with more sophisticated deterministic agents.

45

… Simple reflex agents

## Slide 46

2.4.3 Model-based reflex agents

The most effective way to handle partial observability is for the agent to keep track of the part of the world it can’t see now.
the agent should maintain some sort of internal state that depends on the percept history and thereby reflects at least some of the unobserved aspects of the current state.

Updating this internal state information as time goes by requires two kinds of knowledge to be encoded in the agent program in some form: 
transition model : how the world changes over time
sensor model: how the state of the world is reflected in the agent’s percepts

46

An agent that uses such models is called a model-based agent.

## Slide 47

2.4.3 Model-based reflex agents: Ex
