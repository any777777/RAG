---
chunk_id: "book-ca4fca8dd8-chunk-0991"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 991
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.2
Non-Cooperative Game Theory
597
your partner will serve 10 years in prison. However, if you both testify against each other,
you’ll both get 5 years. Ali and Bo also know that if both refuse to testify they will serve
only 1 year each for the lesser charge of possessing stolen property. Now Ali and Bo face the
so-called prisoner’s dilemma: should they testify or refuse? Being rational agents, Ali and
Bo each want to maximize their own expected utility, which means minimizing the number
of years in prison—each is indifferent about the welfare of the other player. The prisoner’s
dilemma is captured in the following payoff matrix:
Ali:testify
Ali:refuse
Bo:testify
A = −5,B = −5
A = −10,B = 0
Bo:refuse
A = 0,B = −10
A = −1,B = −1
Now, put yourself in Ali’s place. She can analyze the payoff matrix as follows:
• Suppose Bo plays testify. Then I get 5 years if I testify and 10 years if I don’t, so in that
case testifying is better.
• On the other hand, if Bo plays refuse, then I go free if I testify and I get 1 year if I
refuse, so testifying is also better in that case.
• So no matter what Bo chooses to do, it would be better for me to testify.
Ali has discovered that testify is a dominant strategy for the game. We say that a strategy
Dominant strategy
s for player p strongly dominates strategy s′ if the outcome for s is better for p than the
Strong domination
outcome for s′, for every choice of strategies by the other player(s). Strategy s weakly dom-
inates s′ if s is better than s′ on at least one strategy proﬁle and no worse on any other. A
Weak domination
dominant strategy is a strategy that dominates all others. A common assumption in game the-
ory is that a rational player will always choose a dominant strategy and avoid a dominated ◀
strategy. Being rational—or at least not wishing to be thought irrational—Ali chooses the
dominant strategy.
It is not hard to see that Bo’s reasoning will be identical: he will also conclude that testify
is a dominant strategy for him, and will choose to play it. The solution of the game, according
to dominant strategy analysis, will be that both players choose testify, and as a consequence
both will serve 5 years in prison.
In a situation like this, where all players choose a dominant strategy, then the outcome
that results is said to be a dominant strategy equilibrium. It is an “equilibrium” because
Dominant strategy
equilibrium
no player has any incentive to deviate from their part of it: by deﬁnition, if they did so, they
could not do better, and may do worse. In this sense, dominant strategy equilibrium is a very
strong solution concept.
Going back to the prisoner’s dilemma, we can see that the dilemma is that the dominant
strategy equilibrium outcome in which both players testify is worse for both players than the
outcome they would get if they both refused to testify. The (refuse,refuse) outcome would
give both players just one year in prison, which would be better for both of them than the 5
years that each would serve if they chose the dominant strategy equilibrium.
Is there any way for Ali and Bo to arrive at the (refuse,refuse) outcome? It is certainly
an allowable option for both of them to refuse to testify, but it is hard to see how rational
agents could make this choice, given the way the game is set up. Remember, this is a non-
cooperative game: they aren’t allowed to talk to each other, so they cannot make a binding
agreement to refuse.
