---
chunk_id: "book-ca4fca8dd8-chunk-0246"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 246
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 4.4
Search in Partially Observable Environments
151
7 
5 
6 
2 
1 
3 
6 
4 
8 
2 
[R,Dirty]
Right
[L,Clean]
7 
5 
Suck
Figure 4.17 Two prediction–update cycles of belief-state maintenance in the kindergarten
vacuum world with local sensing.
stochastic, continuous-state environments with the tools of probability theory, as explained in
Chapter 14.
In this section we will show an example in a discrete environment with deterministic
sensors and nondeterministic actions. The example concerns a robot with a particular state
estimation task called localization: working out where it is, given a map of the world and
Localization
a sequence of percepts and actions. Our robot is placed in the maze-like environment of
Figure 4.18. The robot is equipped with four sonar sensors that tell whether there is an
obstacle—the outer wall or a dark shaded square in the ﬁgure—in each of the four compass
directions. The percept is in the form of a bit vector, one bit for each of the directions north,
east, south, and west in that order, so 1011 means there are obstacles to the north, south, and
west, but not east.
We assume that the sensors give perfectly correct data, and that the robot has a correct
map of the environment. But unfortunately, the robot’s navigational system is broken, so
when it executes a Right action, it moves randomly to one of the adjacent squares. The
robot’s task is to determine its current location.
Suppose the robot has just been switched on, and it does not know where it is—its initial
belief state b consists of the set of all locations. The robot then receives the percept 1011
and does an update using the equation bo =UPDATE(1011), yielding the 4 locations shown
in Figure 4.18(a). You can inspect the maze to see that those are the only four locations that
yield the percept 1011.
Next the robot executes a Right action, but the result is nondeterministic. The new belief
state, ba =PREDICT(bo,Right), contains all the locations that are one step away from the lo-
cations in bo. When the second percept, 1010, arrives, the robot does UPDATE(ba,1010) and
ﬁnds that the belief state has collapsed down to the single location shown in Figure 4.18(b).
That’s the only location that could be the result of
UPDATE(PREDICT(UPDATE(b,1011),Right),1010).
With nondeterministic actions the PREDICT step grows the belief state, but the UPDATE step
shrinks it back down—as long as the percepts provide some useful identifying information.
Sometimes the percepts don’t help much for localization: If there were one or more long east-
west corridors, then a robot could receive a long sequence of 1010 percepts, but never know
