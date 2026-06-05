---
chunk_id: "book-ca4fca8dd8-chunk-0115"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 115
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 68

68
Chapter 2
Intelligent Agents
Agent
Environment
Sensors
What action I
should do now
Condition-action rules
Actuators
What the world
is like now
Figure 2.9 Schematic diagram of a simple reﬂex agent. We use rectangles to denote the
current internal state of the agent’s decision process, and ovals to represent the background
information used in the process.
visual input to establish the condition we call “The car in front is braking.” Then, this triggers
some established connection in the agent program to the action “initiate braking.” We call
such a connection a condition–action rule,6 written as
Condition–action
rule
if car-in-front-is-braking then initiate-braking.
Humans also have many such connections, some of which are learned responses (as for driv-
ing) and some of which are innate reﬂexes (such as blinking when something approaches the
eye). In the course of the book, we show several different ways in which such connections
can be learned and implemented.
The program in Figure 2.8 is speciﬁc to one particular vacuum environment. A more
general and ﬂexible approach is ﬁrst to build a general-purpose interpreter for condition–
action rules and then to create rule sets for speciﬁc task environments. Figure 2.9 gives the
structure of this general program in schematic form, showing how the condition–action rules
allow the agent to make the connection from percept to action. Do not worry if this seems
trivial; it gets more interesting shortly.
An agent program for Figure 2.9 is shown in Figure 2.10.
The INTERPRET-INPUT
function generates an abstracted description of the current state from the percept, and the
RULE-MATCH function returns the ﬁrst rule in the set of rules that matches the given state
description. Note that the description in terms of “rules” and “matching” is purely concep-
tual; as noted above, actual implementations can be as simple as a collection of logic gates
implementing a Boolean circuit. Alternatively, a “neural” circuit can be used, where the logic
gates are replaced by the nonlinear units of artiﬁcial neural networks (see Chapter 22).
Simple reﬂex agents have the admirable property of being simple, but they are of limited
intelligence. The agent in Figure 2.10 will work only if the correct decision can be made on
▶
the basis of just the current percept—that is, only if the environment is fully observable.
6
Also called situation–action rules, productions, or if–then rules.

## Page 69
