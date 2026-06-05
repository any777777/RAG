---
chunk_id: "chapter-02-2-084f13b554-chunk-0003"
source_id: "chapter-02-2-084f13b554"
source_file: "New folder/Chapter 02 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

Consider the simple vacuum-cleaner agent, is it rational? That depends:
what the performance measure is, 
what is known about the environment, 
and what sensors and actuators the agent has. 
Let us assume the following:
The performance measure awards one point for each clean square at each time step, over a “lifetime” of 1000 time steps.
The “geography” of the environment is known a priori (Figure 2.2) but the dirt distribution and the initial location of the agent are not. 
Clean squares stay clean and sucking cleans the current square. 
The Right and Left actions move the agent one square except when this would take the agent outside the environment, in which case the agent remains where it is.
The only available actions are Right, Left, and Suck.
The agent correctly perceives its location and whether that location contains dirt.

16

… Rationality

Under these circumstances the agent is indeed rational; its expected performance is at least as good as any other agent’s.

## Slide 17

Irrational case

One can see easily that the same agent would be irrational under different circumstances.

For example, once all the dirt is cleaned up, the agent will oscillate needlessly back and forth;
if the performance measure includes a penalty of one point for each movement, the agent will fare poorly. 
A better agent for this case would do nothing once it is sure that all the squares are clean.

17

## Slide 18

2.2.3 Omniscience, learning, and autonomy

An omniscient (كلي المعرفة) agent knows the actual outcome of its actions and can act accordingly
omniscience is impossible in reality.
Our definition of rationality does not require omniscience, 
because the rational choice depends only on the percept sequence to date.
Doing actions in order to modify future percepts—sometimes called information gathering—is an important part of rationality and is covered in depth in Chapter 15.
A second example of information gathering is provided by the exploration that must be undertaken by a vacuum-cleaning agent in an initially unknown environment.

18

## Slide 19

A rational agent chooses whichever action maximizes the expected value of the performance measure given the percept sequence to date
Rational /= omniscient
	percepts may not supply all relevant information 
Rational /= clairvoyant ( does not know future)
	action outcomes may not be as expected Hence, rational /= successful
Rational	⇒	exploration, learning, autonomy

Rationality

## Slide 20
