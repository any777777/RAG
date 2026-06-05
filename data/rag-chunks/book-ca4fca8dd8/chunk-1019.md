---
chunk_id: "book-ca4fca8dd8-chunk-1019"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1019
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.2
Non-Cooperative Game Theory
613
experts. Part of the problem is anticipating what action the virus writers will try next.
Strategies: Game theory is very good at representing the idea that the other players’
strategies are initially unknown—as long as we assume all agents are rational. The theory
does not say what to do when the other players are less than fully rational. The notion of a
Bayes–Nash equilibrium partially addresses this point: it is an equilibrium with respect to
Bayes–Nash
equilibrium
a player’s prior probability distribution over the other players’ strategies—in other words, it
expresses a player’s beliefs about the other players’ likely strategies.
Chance: If a game depends on the roll of a die, it is easy enough to model a chance node
with uniform distribution over the outcomes. But what if it is possible that the die is unfair?
We can represent that with another chance node, higher up in the tree, with two branches for
“die is fair” and “die is unfair,” such that the corresponding nodes in each branch are in the
same information set (that is, the players don’t know if the die is fair or not). And what if we
suspect the other opponent does know? Then we add another chance node, with one branch
representing the case where the opponent does know, and one where the opponent doesn’t.
Utilities: What if we don’t know our opponent’s utilities? Again, that can be modeled
with a chance node, such that the other agent knows its own utilities in each branch, but we
don’t. But what if we don’t know our own utilities? For example, how do I know if it is
rational to order the chef’s salad if I don’t know how much I will like it? We can model that
with yet another chance node specifying an unobservable “intrinsic quality” of the salad.
Thus, we see that game theory is good at representing most sources of uncertainty—but
at the cost of doubling the size of the tree every time we add another node; a habit that quickly
leads to intractably large trees. Because of these and other problems, game theory has been
used primarily to analyze environments that are at equilibrium, rather than to control agents
within an environment.
17.2.5 Uncertain payoﬀs and assistance games
In Chapter 1 (page 22), we noted the importance of designing AI systems that can operate
under uncertainty about the true human objective. Chapter 15 (page 543) introduced a simple
model for uncertainty about one’s own preferences, using the example of durian-ﬂavored ice
cream. By the simple device of adding a new latent variable to the model to represent the
unknown preferences, together with an appropriate sensor model (e.g., observing the taste of
a small sample of the ice cream), uncertain preferences can be handled in a natural way.
Chapter 15 also studied the off-switch problem: we showed that a robot with uncertainty
about human preferences will defer to the human and allow itself to be switched off. In
that problem, Robbie the robot is uncertain about Harriet the human’s preferences, but we
model Harriet’s decision (whether or not to switch Robbie off) as a simple, deterministic
consequence of her own preferences for the action that Robbie proposes. Here, we generalize
this idea into a full two-person game called an assistance game, in which both Harriet and
Robbie are players. We assume that Harriet observes her own preferences θ and acts in
accordance with them, while Robbie has a prior probability P(θ) over Harriet’s preferences.
The payoff is deﬁned by θ and is identical for both players: both Harriet and Robbie are
maximizing Harriet’s payoff. In this way, the assistance game provides a formal model of the
idea of provably beneﬁcial AI introduced in Chapter 1.
In addition to the deferential behavior exhibited by Robbie in the off-switch problem—
which is a restricted kind of assistance game—other behaviors that emerge as equilibrium
