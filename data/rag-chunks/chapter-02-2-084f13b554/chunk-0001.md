---
chunk_id: "chapter-02-2-084f13b554-chunk-0001"
source_id: "chapter-02-2-084f13b554"
source_file: "New folder/Chapter 02 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Slide 1

Artificial intelligence

## Slide 2

Introduction

Our plan in this book is to use the concept of rationality to develop a small set of design principles for building successful agents—
systems that can reasonably be called intelligent.
The observation that some agents behave better than others leads naturally to the idea of a rational agent—
one that behaves as well as possible.
How well an agent can behave depends on the nature of the environment; 
some environments are more difficult than others.

2

## Slide 3

An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.

3

## Slide 4

… Agents and Environments

Example, A software agent:
receives file contents, network packets, and human input (keyboard/mouse/touchscreen/voice) as sensory inputs 
and acts on the environment by writing files, sending network packets, and displaying information or generating sounds. 
The environment could be everything—the entire universe! 
In practice it is just that part of the universe whose state we care about when designing this agent—
the part that affects what the agent perceives and that is affected by the agent’s actions.

4

## Slide 5

We use the term percept to refer to the content an agent’s sensors are perceiving.
An agent’s percept sequence is the complete history of everything the agent has ever perceived.
Mathematically speaking, we say that an agent’s behavior is described by the agent function 
that maps any given percept sequence to an action.
The agent function for an artificial agent will be implemented by an agent program.

5

… Agents and Environments

## Slide 6

?
agent

6

sensors

percepts

actions

environment

actuators
Agents include humans, robots, softbots, thermostats, etc. The agent function maps from percept histories to actions:
f : P∗ → A
The agent program runs on the physical architecture to produce f

Agents and Environment

## Slide 7

7

… Agents and Environments

## Slide 8

Chapter 2

8

Percepts: location and contents, e.g., [A, Dirty]
Actions: Left, Right, Suck, NoOp

Vacuum-Cleaner World

## Slide 9

9

… Agents and Environments

What is the right way to fill out the table? In other words, what makes an agent good or bad,
intelligent or stupid? We answer these questions in the next section.

## Slide 10

10

… Agents and Environments

## Slide 11
