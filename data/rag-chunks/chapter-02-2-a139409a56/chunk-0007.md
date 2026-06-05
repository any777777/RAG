---
chunk_id: "chapter-02-2-a139409a56-chunk-0007"
source_id: "chapter-02-2-a139409a56"
source_file: "Chapter 02 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 7
confidence: "first-pass"
extraction_method: "structured-local"
---

34
Environment Characteristics
Property
Types
Description
Example
Observable
Fully / Partially
Complete vs. incomplete 
state info
Chess / Poker
Deterministic
Deterministic / Stochastic
Predictable outcomes vs. 
randomness
Sudoku / Dice games
Episodic
Episodic / Sequential
Independent tasks vs. 
linked decisions
Image classification / Chess
Static
Static / Dynamic
Changes only by agent vs. 
changing independently
Crossword / Self-driving
Discrete
Discrete / Continuous
Finite states & actions vs. 
infinite
Board games / Robot 
control
Number of Agents
Single / Multi-Agent
One agent vs. multiple 
agents
Maze solving / Soccer

## Page 35

35
… Properties of task environments

## Page 36

• Experiments are often carried out not for a single environment but 
for many environments drawn from an environment class. 
• For example, to evaluate a taxi driver in simulated traffic, we would want to 
run many simulations with different traffic, lighting, and weather conditions. 
• We are then interested in the agent’s average performance over the 
environment class.
36
… Properties of task environments

## Page 37

• agent = architecture + program
• The architecture
• makes the percepts from the sensors available to the program, 
• runs the program, 
• and feeds the program’s action choices to the actuators as they are generated.
37

## Page 38

2.4.1 Agent programs
• If the agent’s actions need to depend on the entire percept sequence, 
the agent will have to remember the percepts
38

## Page 39

• To build a rational agent, we as designers must construct a table that 
contains the appropriate action for every possible percept sequence.
• It is instructive to consider why the table-driven approach to agent 
construction is doomed to failure. 
• Let     be the set of possible percepts and let T be the lifetime of the agent 
(the total number of percepts it will receive). 
• The lookup table will contain               entries.
• The automated taxi has a lookup table with over 10^600,000,000,000 entries
• Even the lookup table for chess has (it turns out) at least 10^150 entries
• In comparison, the number of atoms in the observable universe is less than 
10^80
39
… Agent programs

## Page 40
