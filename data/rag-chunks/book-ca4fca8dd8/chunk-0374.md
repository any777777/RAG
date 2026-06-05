---
chunk_id: "book-ca4fca8dd8-chunk-0374"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 374
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 229

Section 7.2
The Wumpus World
229
PIT
1
2
3
4
1
2
3
4
START
Stench
Stench
B
r
ee
z
e
Gold
PIT
PIT
B
r
ee
z
e
B
r
ee
z
e
B
r
ee
z
e
B
r
ee
z
e
B
r
ee
z
e
Stench
Figure 7.2 A typical wumpus world. The agent is in the bottom left corner, facing east
(rightward).
• Environment: A 4×4 grid of rooms, with walls surrounding the grid. The agent al-
ways starts in the square labeled [1,1], facing to the east. The locations of the gold and
the wumpus are chosen randomly, with a uniform distribution, from the squares other
than the start square. In addition, each square other than the start can be a pit, with
probability 0.2.
• Actuators: The agent can move Forward, TurnLeft by 90◦, or TurnRight by 90◦. The
agent dies a miserable death if it enters a square containing a pit or a live wumpus. (It
is safe, albeit smelly, to enter a square with a dead wumpus.) If an agent tries to move
forward and bumps into a wall, then the agent does not move. The action Grab can be
used to pick up the gold if it is in the same square as the agent. The action Shoot can
be used to ﬁre an arrow in a straight line in the direction the agent is facing. The arrow
continues until it either hits (and hence kills) the wumpus or hits a wall. The agent has
only one arrow, so only the ﬁrst Shoot action has any effect. Finally, the action Climb
can be used to climb out of the cave, but only from square [1,1].
• Sensors: The agent has ﬁve sensors, each of which gives a single bit of information:
– In the squares directly (not diagonally) adjacent to the wumpus, the agent will
perceive a Stench.1
– In the squares directly adjacent to a pit, the agent will perceive a Breeze.
– In the square where the gold is, the agent will perceive a Glitter.
– When an agent walks into a wall, it will perceive a Bump.
– When the wumpus is killed, it emits a woeful Scream that can be perceived any-
where in the cave.
The percepts will be given to the agent program in the form of a list of ﬁve symbols;
for example, if there is a stench and a breeze, but no glitter, bump, or scream, the agent
program will get [Stench,Breeze,None,None,None].
1
Presumably the square containing the wumpus also has a stench, but any agent entering that square is eaten
before being able to perceive anything.

## Page 230
