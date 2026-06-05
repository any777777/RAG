---
chunk_id: "chapter-02-2-084f13b554-chunk-0005"
source_id: "chapter-02-2-084f13b554"
source_file: "New folder/Chapter 02 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 5
confidence: "first-pass"
extraction_method: "structured-local"
---

Fully observable vs. partially observable: 
If an agent’s sensors give it access to the complete state of the environment at each point in time, then we say that the task environment is fully observable. 
A task environment is effectively fully observable if the sensors detect all aspects that are relevant to the choice of action; 
relevance, in turn, depends on the performance measure.
If the agent has no sensors at all then the environment is unobservable. 
The agent’s goals may still be achievable, sometimes with certainty. (Ch 4: SEARCH IN COMPLEX ENVIRONMENTS)

27

## Slide 28

Single-agent vs. multiagent:
An agent solving a crossword puzzle by itself is clearly in a single-agent environment.
Chess is a competitive multiagent environment.
 The taxi-driving environment is a partially cooperative multiagent environment. 
Because avoiding collisions maximizes the performance measure of all agents.
It is also partially competitive because, for example, only one car can occupy a parking space.
Communication emerges as a rational behavior in multiagent environments.
in some competitive environments, randomized behavior is rational, 
because it avoids the dangers of predictability.

28

… Properties of task environments

## Slide 29

Deterministic vs. nondeterministic. 
If the next state of the environment is completely determined by the current state and the action executed by the agent(s), 
then we say the environment is deterministic; 
otherwise, it is nondeterministic (stochastic).
Taxi driving is clearly nondeterministic
We say that a model of the environment is stochastic if it explicitly deals with probabilities (e.g., “there’s a 25% chance of rain tomorrow”) 
and “nondeterministic” if the possibilities are listed without being quantified (e.g., “there’s a chance of rain tomorrow”).

29

… Properties of task environments

## Slide 30

Episodic vs. sequential:
In an episodic task environment, the agent’s experience is divided into episodes; the next episode does not depend on the actions taken in previous episodes.
For example, an agent that must spot defective parts on an assembly line (classification)
In sequential environments, the current decision could affect all future decisions.
Chess and taxi driving are sequential
Episodic environments are much simpler than sequential environments 
because the agent does not need to think ahead.

30

… Properties of task environments

## Slide 31
