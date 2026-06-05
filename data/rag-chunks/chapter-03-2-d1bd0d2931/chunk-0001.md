---
chunk_id: "chapter-03-2-d1bd0d2931-chunk-0001"
source_id: "chapter-03-2-d1bd0d2931"
source_file: "Chapter 03 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1

Artificial intelligence

## Page 2

Introduction
• Problem-solving agent: 
• when the correct action to take is not immediately obvious, an agent may need to 
plan ahead: to consider a sequence of actions that form a path to a goal state. 
• The process it undertakes is called search.
• Problem-solving agents use atomic representations.
• Agents that use factored or structured representations of states are called planning 
agents and are discussed in Chapters 7 and 11.
• Informed algorithms: the agent can estimate how far it is from the goal
• uninformed algorithms: no such estimate is available.
2
This is a kind of goal-based agents that decide what to do by finding sequences of actions that
lead to desirable states.

## Page 3

• In this chapter, we will assume our agents always have access to 
information about the world, such as the map in Figure 3.1.
3

## Page 4

… Problem-Solving Agents
• The agent can follow this four-phase problem-solving process:
• 1. Goal formulation: The agent adopts the goal of reaching Bucharest. 
• Goals organize behavior by limiting the objectives and hence the actions to be 
considered.
• 2. Problem formulation: The agent devises a description of the states and 
actions necessary to reach the goal
• one good model is to consider the actions of traveling from one city to an adjacent city
• 3. Search: the agent simulates best sequences of actions in its model to get 
the goal
• Such a sequence is called a solution
• 4. Execution: The agent can now execute the actions in the solution, one at a 
time.
4
Formulate-> Search-> Execute

## Page 5

5
Example: Romania
On holiday in Romania; currently in Arad. Flight leaves tomorrow from
Bucharest
Formulate goal:
be in Bucharest
Formulate problem:
states: various cities actions: drive between cities
Find solution:
sequence of cities, e.g., Arad, Sibiu, Fagaras, Bucharest

## Page 6

Example: Romania
6

## Page 7
