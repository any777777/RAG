---
chunk_id: "book-ca4fca8dd8-chunk-0987"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 987
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.2
Non-Cooperative Game Theory
595
One option is to adopt a convention before engaging in joint activity. A convention is
Convention
any constraint on the selection of joint plans. For example, the convention “stick to your
side of the court” would rule out plan 1, causing both partners to select plan 2. Drivers on a
road face the problem of not colliding with each other; this is (partially) solved by adopting
the convention “stay on the right-hand side of the road” in most countries; the alternative,
“stay on the left-hand side,” works equally well as long as all agents in an environment agree.
Similar considerations apply to the development of human language, where the important
thing is not which language each individual should speak, but the fact that a community all
speaks the same language. When conventions are widespread, they are called social laws.
Social law
In the absence of a convention, agents can use communication to achieve common
knowledge of a feasible joint plan. For example, a tennis player could shout “Mine!” or
“Yours!” to indicate a preferred joint plan. Communication does not necessarily involve a
verbal exchange. For example, one player can communicate a preferred joint plan to the other
simply by executing the ﬁrst part of it. If agent A heads for the net, then agent B is obliged to
go back to the baseline to hit the ball, because plan 2 is the only joint plan that begins with
A’s heading for the net. This approach to coordination, sometimes called plan recognition,
Plan recognition
works when a single action (or short sequence of actions) by one agent is enough for the other
to determine a joint plan unambiguously.
17.2 Non-Cooperative Game Theory
We will now introduce the key concepts and analytical techniques of game theory—the theory
that underpins decision making in multiagent environments. Our tour will start with non-
cooperative game theory.
17.2.1 Games with a single move: Normal form games
The ﬁrst game model we will look at is one in which all players take action simultaneously
and the result of the game is based on the proﬁle of actions that are selected in this way.
(Actually, it is not crucial that the actions take place at the same time; what matters is that no
player has knowledge of the other players’ choices.) These games are called normal form
games. A normal form game is deﬁned by three components:
Normal form game
• Players or agents who will be making decisions. Two-player games have received the
Player
most attention, although n-player games for n > 2 are also common. We give players
capitalized names, like Ali and Bo or O and E.
• Actions that the players can choose. We will give actions lowercase names, like one or
testify. The players may or may not have the same set of actions available.
• A payoff function that gives the utility to each player for each combination of actions
Payoﬀfunction
by all the players. For two-player games, the payoff function for a player can be repre-
sented by a matrix in which there is a row for each possible action of one player, and a
column for each possible choice of the other player: a chosen row and a chosen column
deﬁne a matrix cell, which is labeled with the payoff for the relevant player. In the two-
player case, it is conventional to combine the two matrices into a single payoff matrix,
Payoﬀmatrix
in which each cell is labeled with payoffs for both players.
To illustrate these ideas, let’s look at an example game, called two-ﬁnger Morra. In this
game, two players, O and E, simultaneously display one or two ﬁngers. Let the total number
