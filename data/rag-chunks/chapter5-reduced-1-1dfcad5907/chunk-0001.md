---
chunk_id: "chapter5-reduced-1-1dfcad5907-chunk-0001"
source_id: "chapter5-reduced-1-1dfcad5907"
source_file: "Chapter5_reduced-1.pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Slide 1

Artificial intelligence

1

## Slide 2

Games vs Search

Search – no adversary 
Solution is (heuristic) method for finding goal
Heuristics and CSP  techniques can find optimal solution
 Evaluation function: estimate of cost from start to goal through given node
Examples: path planning, scheduling activities

Games – adversary  
	Solution is strategy (strategy specifies move for every possible opponent reply).
Time limits force approximate solutions
Examples: chess, checkers, Othello, backgammon

2

## Slide 3

Types of Games

chess, checkers, go, othello | backgammon monopoly
battleships, blind tictactoe | bridge, poker, scrabble nuclear war

deterministic  	               chance

perfect information

imperfect information

Our focus:	deterministic, turn-taking, two-player, zero-sum games of perfect information
zero-sum game:	a participant's gain (or loss) is exactly balanced by the losses (or gains) of the other participant.
perfect information:	fully observable

3

## Slide 4

Two-player zero-sum games

4

## Slide 5

The Tic-Tac-Toe search space

What is the minimum search depth? 5 for max to win

What is the maximum search depth? 9 to fill the game

What is the branching factor? 9,8,7,.. Average 5

5

## Slide 6

Game Setup

Two players: MAX and MIN
MAX moves first and they take turns until the game is over.
Games as search:
initial state: e.g. starting board configuration
player(s): which player has the move in a state
action(s): set of legal moves in a state
result(s, a): the states resulting from a given move.
terminal-test(s): game over? (terminal states)
	utility(s,p):	value of terminal states, e.g., win (+1), lose (-1) and draw (0) in chess.
Players use search tree to determine next move.

6

## Slide 7

Optimal  strategies

Find the best strategy for MAX assuming an infallible MIN opponent.
Assumption: Both players play optimally.
Given a game tree, the optimal strategy can be determined by using the minimax value of each node:

MINIMAX(s)=  {
         UTILITY(s)
maxa  Actions(s) MINIMAX(RESULT(s,a)) mina  Actions(s) MINIMAX(RESULT(s,a))  
}

If s is a terminal
If PLAYER(s)=MAX If PLAYER(s)=MIN

7

## Slide 8

Two-ply game tree: minimax tree

MAX

A

B

C

D

3	12	8	2	4	6	14
Definition: ply = turn of a two-player game

5

2

3

2

2

3

a1

a2

a3

b1

b2

b3

c1

c2

c3

d1

d2

d3

MIN

8

## Slide 9

MAX

A

B

C

D

3	12	8	2	4	6	14	5	2

The minimax value at a min node is the minimum of backed-up values, because your opponent will do what’s best for them (and worst for you).

3

2

2

3

a1

a2

a3

b1

b2

b3

c1

c2

c3

d1

d2

d3

MIN

Two-ply game tree: minimax tree

9

## Slide 10

MAX

A

B

C

D

3

12

8

2

4

6

14

5

2

3
