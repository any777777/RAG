---
chunk_id: "chapter-02-2-084f13b554-chunk-0006"
source_id: "chapter-02-2-084f13b554"
source_file: "New folder/Chapter 02 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 6
confidence: "first-pass"
extraction_method: "structured-local"
---

Static vs. dynamic: 
If the environment can change while an agent is deliberating, then we say the environment is dynamic for that agent; otherwise, it is static.
If the environment itself does not change with the passage of time but the agent’s performance score does, then we say the environment is semidynamic. 
Taxi driving is clearly dynamic
Crossword puzzles are static.
Chess, when played with a clock, is semidynamic.

31

… Properties of task environments

## Slide 32

Discrete vs. continuous: 
The discrete/continuous distinction applies to the state of the environment, to the way time is handled, and to the percepts and actions of the agent.
Chess has a discrete set of percepts and actions 
Taxi driving is a continuous-state and continuous-time problem:
the speed and location of the taxi and of the other vehicles sweep through a range of continuous values and do so smoothly over time. 
Known vs. unknown:
In a known environment, the outcomes for all actions are given. 
If the environment is unknown, the agent will have to learn how it works in order to make good decisions.

32

… Properties of task environments

## Slide 33

The distinction between known and unknown environments is not the same as the one between fully and partially observable environments. 
It is possible for a known environment to be partially observable: 
for example, in solitaire card games, I know the rules but am still unable to see the cards that have not yet been turned over. 
Conversely, an unknown environment can be fully observable:
in a new video game, the screen may show the entire game state but I still don’t know what the buttons do until I try them.

33

… Properties of task environments

The environment type largely determines the agent design
The real world is (of course) partially observable, stochastic, sequential, dynamic, continuous, multi-agent

## Slide 34

34

Environment Characteristics
