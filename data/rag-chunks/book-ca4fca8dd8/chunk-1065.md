---
chunk_id: "book-ca4fca8dd8-chunk-1065"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1065
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
637
can we devise methods whereby separate subagents for robot navigation and robot obstacle
avoidance could cooperatively achieve a combined control system that is globally optimal?
Some basic results in this direction have been obtained (Guestrin et al., 2002; Russell and
Zimdars, 2003). The basic idea is that each subagent learns its own Q-function (a kind of
utility function; see Section 23.3.3) from its own stream of rewards. For example, a robot-
navigation component can receive rewards for making progress towards the goal, while the
obstacle-avoidance component receives negative rewards for every collision. Each global
decision maximizes the sum of Q-functions and the whole process converges to globally
optimal solutions.
The roots of game theory can be traced back to proposals made in the 17th century by
Christiaan Huygens and Gottfried Leibniz to study competitive and cooperative human in-
teractions scientiﬁcally and mathematically. Throughout the 19th century, several leading
economists created simple mathematical examples to analyze particular examples of compet-
itive situations.
The ﬁrst formal results in game theory are due to Zermelo (1913) (who had, the year
before, suggested a form of minimax search for games, albeit an incorrect one). Emile Borel
(1921) introduced the notion of a mixed strategy. John von Neumann (1928) proved that
every two-person, zero-sum game has a maximin equilibrium in mixed strategies and a well-
deﬁned value. Von Neumann’s collaboration with the economist Oskar Morgenstern led to
the publication in 1944 of the Theory of Games and Economic Behavior, the deﬁning book
for game theory. Publication of the book was delayed by the wartime paper shortage until a
member of the Rockefeller family personally subsidized its publication.
In 1950, at the age of 21, John Nash published his ideas concerning equilibria in general
(non-zero-sum) games. His deﬁnition of an equilibrium solution, although anticipated in the
work of Cournot (1838), became known as Nash equilibrium. After a long delay because
of the schizophrenia he suffered from 1959 onward, Nash was awarded the Nobel Memorial
Prize in Economics (along with Reinhart Selten and John Harsanyi) in 1994. The Bayes–Nash
equilibrium is described by Harsanyi (1967) and discussed by Kadane and Larkey (1982).
Some issues in the use of game theory for agent control are covered by Binmore (1982).
Aumann and Brandenburger (1995) show how different equilibria can be reached depending
on the knowleedge each player has.
The prisoner’s dilemma was invented as a classroom exercise by Albert W. Tucker in
1950 (based on an example by Merrill Flood and Melvin Dresher) and is covered extensively
by Axelrod (1985) and Poundstone (1993). Repeated games were introduced by Luce and
Raiffa (1957), and Abreu and Rubinstein (1988) discuss the use of ﬁnite state machines for
repeated games—technically, Moore machines. The text by Mailath and Samuelson (2006)
concentrates on repeated games.
Games of partial information in extensive form were introduced by Kuhn (1953). The
sequence form for partial-information games was invented by Romanovskii (1962) and inde-
pendently by Koller et al. (1996); the paper by Koller and Pfeffer (1997) provides a readable
introduction to the ﬁeld and describes a system for representing and solving sequential games.
The use of abstraction to reduce a game tree to a size that can be solved with Koller’s
technique was introduced by Billings et al. (2003). Subsequently, improved methods for
equilibrium-ﬁnding enabled solution of abstractions with 1012 states (Gilpin et al., 2008;
Zinkevich et al., 2008). Bowling et al. (2008) show how to use importance sampling to
